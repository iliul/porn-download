#!/usr/bin/env python

import re
import os
import sys
import requests
import random
from bs4 import BeautifulSoup
from urllib import request, parse

COOKIES="-b language=cn_CN;watch_times=0"
URL="http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=24bfc9f6c5ecad37daf7"
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"

def pick_a_chinese_proxy():
    content = request.urlopen(
        "http://www.proxynova.com/proxy-server-list/country-cn/").read()
    soup = BeautifulSoup(content, 'lxml')
    all_proxies = []
    for row in soup.find_all('tr')[1:]:
        try:
            ip = row.find_all('span', {'class' : 'row_proxy_ip'})[0].text.strip()
            port = row.find_all('td')[1].text.strip()
            cur_proxy = "{}:{}".format(ip, port)
            all_proxies.append(cur_proxy)
        except:
            pass
    return random.choice(all_proxies)

def get_html(url):
    '''
    r = requests.get(url)
    #print(r.content.decode('utf-8'))

    html = r.content.decode('utf-8')
    with open('./data','w') as f:
        f.write(html)
    '''

    with open('./data', 'r') as f:
        html = f.read()
        r = re.search("so.addVariable\(\'file\',\'(.*)\'\);\n{1,10}", html)
        vid = r.group(1)
        if vid:
            print('vid : {vid}'.format(vid=vid))

        r = re.search("so.addVariable\(\'max_vid\',\'(.*)\'\);\n{1,10}", html)
        max_vid = r.group(1)
        if max_vid:
            print('max_vid : {max_vid}'.format(max_vid=max_vid))

        r = re.search("so.addVariable\(\'seccode\',\'(.*)\'\);\n{1,10}", html)
        seccode = r.group(1)
        if seccode:
            print('seccode : {seccode}'.format(seccode=seccode))

        r = re.search("so.addVariable\(\'mp4\',\'(.*)\'\);\n{1,10}", html)
        mp4 = r.group(1)
        if mp4:
            print('mp4 : {mp4}'.format(mp4=mp4))

        r = re.search(r'<title>\W{1,10}(.*)\n.*</title>', html)
        title = r.group(1).replace(' ', '-')
        if title:
            print('title : {title}'.format(title=title))

    jsonurl = "http://email.91dizhi.at.gmail.com.9h4.space" + "/getfile.php?VID=" + vid + "&mp4=" + mp4 + "&seccode=" + seccode + "&max_vid=" + max_vid
    print('jsonurl : {jsonurl}'.format(jsonurl=jsonurl))

    """
    proxies = {}
    ret = requests.get(jsonurl, proxies=proxies)
    print(ret.content.decode('utf-8'))
    with open('./link', 'w') as x:
        x.write(ret.content.decode('utf-8'))
    """

    with open('./link', 'r') as x:
        data = x.read()
    resp = re.search("^(.*)&domainUrl.*", data)
    if resp:
        print("decode : {resp}".format(resp=resp.group(1)))
        print("unquote : {resp}".format(resp=parse.unquote(resp.group(1))))

if __name__ == "__main__":
    get_html(URL)

    extractor_proxy = pick_a_chinese_proxy()
    print("Using Chinese proxy {}".format(extractor_proxy))

    qq = "http://www.qq.com"
    facebook = "http://www.facebook.com"
    #proxies = {"http" : "sock5://192.168.8.125:1080"}
    proxies = {}
    proxies['http'] = "http://" + pick_a_chinese_proxy()
    print(proxies)

    ret = requests.get(qq, proxies=proxies)
    print(ret.status_code)
    #print('text : %s' % ret.text)
    #print(ret.headers)
    #print(ret.request.headers)
