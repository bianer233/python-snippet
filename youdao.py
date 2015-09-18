#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-04-03 21:12:16
# @Function: 有道翻译命令行版
# @Author  : BeginMan

import os
import sys
import urllib
import urllib2
reload(sys)
sys.setdefaultencoding("utf-8")
import json as json
# import simplejson as json
import platform
import datetime

API_KEY = 'yours'
KEYFORM = 'yours'

def GetTranslate(txt):
    url = 'http://fanyi.youdao.com/openapi.do'
    data = {
    'keyfrom': KEYFORM,
    'key': API_KEY,
    'type': 'data',
    'doctype': 'json',
    'version': 1.1,
    'q': txt
    }
    data = urllib.urlencode(data)
    url = url+'?'+data
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    result = json.loads(response.read())
    return result

def Sjson(json_data):
    query = json_data.get('query','')               # 查询的文本
    translation = json_data.get('translation','')   # 翻译
    basic = json_data.get('basic','')               # basic 列表
    sequence = json_data.get('web',[])              # 短语列表
    phonetic,explains_txt,seq_txt,log_word_explains = '','','',''

    # 更多释义
    if basic:
        phonetic = basic.get('phonetic','')         # 音标
        explains = basic.get('explains',[])         # 更多释义 列表
        for obj in explains:
            explains_txt += obj+'\n'
            log_word_explains += obj+','    
    # 句子解析
    if sequence:
        for obj in sequence:
            seq_txt += obj['key']+'\n'
            values = ''
            for i in obj['value']:
                values += i+','
            seq_txt += values+'\n'

    print_format = '*'*40+'\n'
    print_format += u'查询对象:  %s [%s]\n' %(query,phonetic)   
    print_format += explains_txt
    print_format += '-'*20+'\n'+seq_txt
    print_format += '*'*40+'\n'
    print print_format

def main():
    while True:
        txt = raw_input(u'请输入要查询的文本：\n')
        if txt:
            Sjson(GetTranslate(txt))

if __name__ == '__main__':
    main()