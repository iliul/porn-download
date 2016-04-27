#!/usr/bin/env python

import re
import os
import sys
import wget
import random
import requests
from bs4 import BeautifulSoup
from urllib import request, parse

OUTDIR = "."
URL = "http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c"
COOKIES = "-b language=cn_CN;watch_times=0"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"

def download_video(url, path, title, ext):
    response = requests.get(url)
    outfile = '{}/{}.{}'.format(path, title, ext)
    if response.status_code == 200:
        with open(outfile, 'wb') as f:
            f.write(response.content)
    return True

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
    
    proxies = {}
    extractor_proxy = pick_a_chinese_proxy()
    #proxies['http'] = 'http://{}'.format(extractor_proxy)
    print("Using Chinese proxy {}".format(extractor_proxy))

    r = requests.get(url, proxies=proxies)
    html = r.content.decode('utf-8')
    
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

    ret = requests.get(jsonurl, proxies=proxies)
    data = ret.content.decode('utf-8')
    resp = re.search("^file=(.*)&domainUrl.*", data)

    assert resp
    print("decode : {resp}".format(resp=resp.group(1)))
    print("unquote : {resp}".format(resp=parse.unquote(resp.group(1))))

    download_url = parse.unquote(resp.group(1))
    if download_video(download_url, OUTDIR, title, 'mp4'):    
        print('download successful !!!')

    #filename = wget.download(parse.unquote(resp.group(1)))
    #filename = wget.download(parse.unquote('http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'))

if __name__ == "__main__":
    get_html(URL)

