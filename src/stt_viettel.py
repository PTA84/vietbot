#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
using pip:
    pip install pyaudio websocket-client
Example usage:
    python stt_viettel.py
"""

# [START speech_transcribe_streaming_mic]
from __future__ import division
import re
import sys
import pyaudio
from six.moves import queue
import time
from termcolor import colored
import websocket
from websocket import ABNF
import logging
import threading
import time
import json
from termcolor import colored

# from mutagen.mp3 import MP3
import gih
from urllib.request import urlretrieve
logging.basicConfig(
    level=logging.DEBUG, format="%(levelname)s: [%(asctime)s] - %(processName)s - %(message)s")

logger = logging.getLogger(__name__)

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
STREAMING_LIMIT = gih.get_config('stt_timeout')
CHANNELS = 1
volume = gih.get_config('volume')
viettel_token=gih.get_config('viettel_token')
def get_current_time():
    return int(round(time.time() * 1000))


class AsrStreamingClient(object):
    def __init__(self, asr_streaming_url, token, rate, channel):
        content_type = "audio/x-raw,+layout=(string)interleaved,+rate=(int){},+format=(string)S16LE,+channels=(int){}" \
            .format(rate, channel)
        hc_uid = "8ed3ac06-a17b-4aea-b654-e4591ebc5a0e"
        hc_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyYTNhZWZkODIxYzc0ZDk3YTk3ZDVkNTY4MDMyZTczNCIsImlhdCI6MTYwODExNjUzNSwiZXhwIjoxOTIzNDc2NTM1fQ.a7BTdZVydhvtzMoKeqDlKswli0SmEVPOwiiEG72GTJw"
        # dest_uri = "{}?content-type={}&token={}&hc_uid={}&hc_token={}".format(asr_streaming_url, content_type, token)
        dest_uri = "{}?content-type={}&token={}&hc_uid={}&hc_token={}".format(asr_streaming_url, content_type, token, hc_uid, hc_token)
        logger.debug("Generated websocket uri: " + dest_uri)

        def on_open():
            self.on_open()

        def on_data(app, data, opcode, fin):
            self.on_data(app, data, opcode, fin)

        def on_error(ws, err):
            self.on_error(ws, err)

        def on_close(ws):
            self.on_close(ws)

        self.ws = websocket.WebSocketApp(dest_uri,
                                         on_open=on_open(),
                                         on_data=on_data,
                                         on_error=on_error,
                                         on_close=on_close)
        self.ws_thread = threading.Thread(target=self.ws.run_forever)
        self.ws_thread.start()
        self.closed = False
        self.output_queue = queue.Queue()

    def get_responses_queue(self):
        return self.output_queue

    def on_open(self):
        logger.debug("Connected to ASR streaming server")

    def on_close(self, ws):
        logger.debug("WS client closed")
        self.closed = True

    def on_error(self, ws, error):
        logger.error(error)
        self.closed = True

    def send(self, msg, binary=False):
        if binary:
            self.ws.send(msg, opcode=ABNF.OPCODE_BINARY)
            logger.debug(f"Sending buffer of size: {len(msg)}")
        else:
            self.ws.send(msg, opcode=ABNF.OPCODE_TEXT)

    def on_data(self, app, data, opcode, fin):
        if opcode == ABNF.OPCODE_BINARY:
            logger.debug("Received binary message from server.")
        elif opcode == ABNF.OPCODE_TEXT:
            logger.debug("Received text message from server: {}".format(data))
            resp = json.loads(data)
            if resp['status'] == 0 and 'result' in resp and resp['result']['final']:
                self.output_queue.put(resp)
            elif resp['status'] != 0:
                self.output_queue.put(resp)

        elif opcode == ABNF.OPCODE_CLOSE:
            logger.debug("Received close message from server: {}".format(data))
            self.close()

    def close(self):
        try:
            self.send('EOS')
        except:
            pass
        self.ws.close()
        self.ws_thread.join()
        self.closed = True

    def is_closed(self):
        return self.closed


def get_resp(resq_queue):
    try:
        resp = resq_queue.get_nowait()
        if resp is None:
            return resp
        elif resp['status'] == 0 and 'result' in resp and resp['result']['final']:
            return resp
        else:
            raise RuntimeError(f"STT exception: status={resp['status']}, msg={resp['msg']}")
    except queue.Empty:
        pass
    return None


class VoiceCommandClient(object):
    def __init__(self, asr_streaming_url, token, chunks, rate, channels, timeout=STREAMING_LIMIT):
        self.asr_streaming_url = asr_streaming_url
        self.token = token
        self.chunks = chunks
        self.rate = rate
        self.channels = channels
        self.timeout = timeout

    def listen_for_command(self):
        asr_client = AsrStreamingClient(self.asr_streaming_url, self.token, self.rate, self.channels)
        asr_client_closed_time = None

        with MicrophoneStream(self.rate, self.chunks, self.channels) as stream:
            audio_generator = stream.generator()
            for buff in audio_generator:
                try:
                    if asr_client_closed_time is None:
                        asr_client.send(buff, binary=True)
                    elif get_current_time()-asr_client_closed_time > self.timeout:
                        logger.error('ASR client closed but does not return any message')
                        break
                    resp = get_resp(asr_client.get_responses_queue())
                    if resp is not None:
                        asr_client.close()
                        return resp
                except websocket.WebSocketConnectionClosedException as e:
                    asr_client_closed_time = get_current_time()
                    pass #server closed
                except Exception as e:
                    logger.warning('Exception occurred: {}'.format(e))
        try:
            asr_client.close()
        except:
            pass
        return {"status": 1, "msg": "STATUS_NOSPEECH"}


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk, channels):
        self._rate = rate
        self._chunk = chunk
        self._channels = channels

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True
        self.start_time = get_current_time()

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=self._channels, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            if get_current_time() - self.start_time > STREAMING_LIMIT:
                self.start_time = get_current_time()
                # data == 'interrupt'
                break
                # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)


def listen_print_loop(responses):
    """Iterates through server responses and prints them.
    The responses passed is a generator that will block until a response
    is provided by the server.
    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.
    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    # keywords=gih.get_config('keywords')    
    # stopwords=gih.get_request('request_pause')    
    for response in responses:
        print(response)
        return response


def main():
    api_url = 'wss://vtcc.ai/voice/api/asr/v1/ws/decode_online'
    token = viettel_token
    asr_client = VoiceCommandClient(api_url, token, CHUNK, RATE, CHANNELS, timeout=STREAMING_LIMIT)
    current_result = asr_client.listen_for_command()
    print(current_result)    
    current_status=current_result['status']
    if current_status == 0:
    # In ra thông tin của Dictionary
    # In ra một giá trị trong Dictionary
        is_final = current_result['result']['final']
        if is_final == True:
            test_result = current_result['result']['hypotheses']['transcript_normed']
            print(colored('[BOT-STT-FPT]: '+str(test_result),'green'))
            return str(test_result)
    else:
        pass
    # return 1

def run_thread(func):
    t = threading.Thread(target = func, args = ())
    t.start()


if __name__ == '__main__':
    main()
