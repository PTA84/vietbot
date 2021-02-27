import requests
import json
import sqlite3 as lite
import os
import yaml
import time
from termcolor import colored



def get_config(request):
    stream = open('config.yaml','r')
    a = yaml.load(stream,Loader=yaml.SafeLoader)
    stream.close()
    a = a[request]
    return a
reminder = get_config('reminder')

def set_config(topic,state):
    file_name = "config.yaml"
    with open(file_name) as f:
        doc = yaml.safe_load(f)
    doc[topic] = state
    with open(file_name, 'w') as f:
        yaml.safe_dump(doc, f, default_flow_style=False)

def get_request(request):
    stream = open('request.yaml','r')
    a = yaml.load(stream,Loader=yaml.SafeLoader)
    stream.close()
    a = a[request]
    return a

def get_response(response):
    stream = open('response.yaml','r')
    a = yaml.load(stream,Loader=yaml.SafeLoader)
    stream.close()
    a = a[response]
    return a

        
def info_user():
    if os.path.exists('usin.db'):
        os.remove('usin.db')
    usin = lite.connect('usin.db',check_same_thread=False)
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS link_music_youtube (
                                            link1 text,
                                            link2 text,
                                            link3 text,
                                            link4 text,
                                            link5 text,
                                            link6 text,
                                            link7 text,
                                            link8 text,
                                            link9 text,
                                            link10 text,
                                            link11 text
                                            ); """
    if usin is not None: 
        cur2 = usin.cursor()
        cur2.execute(sql_create_projects_table)
    return usin
def data_init():
    if os.path.exists('hassdata.db'):
        os.remove('hassdata.db')
    con1 = lite.connect('hassdata.db',check_same_thread=False)
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS HASSINFO (
                                            entity_id_ex text,
                                            domain_ex text,
                                            friendly_name_ex text
                                            ); """
    if con1 is not None: 
        cur = con1.cursor()
        cur.execute(sql_create_projects_table)

    return con1

def data_command_init():

    con2 = lite.connect('command.db',check_same_thread=False)
    sql_command_table = """ CREATE TABLE IF NOT EXISTS customcommand (
                                            Command text,
                                            entity_id text,
                                            service text
                                            ); """
    if con2 is not None: 
        cur = con2.cursor()
        cur.execute(sql_command_table)
    return con2





        

