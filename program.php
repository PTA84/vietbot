<?php
    $stt_engine = $_POST["stt_engine"]; //You have to get the form data
    $tts_engine = $_POST["tts_engine"];
    $hass_url = $_POST["hass_url"];
    $file = fopen('configurationSettings.yaml', 'w+'); //Open your .txt file
    ftruncate($file, 0); //Clear the file to 0bit
	fwrite($file,"stt_engine: ");
    fwrite($file, $stt_engine ."\n");
    fwrite($file,"tts_engine: ");
    fwrite($file, $tts_engine ."\n");
    fwrite($file,"hass_url: ");
    fwrite($file, $hass_url ."\n");
    fclose($file ); //Finally close our .txt
    die(header("Location: ".$_SERVER["HTTP_REFERER"]));
?>