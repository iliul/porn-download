#!/usr/bin/env python3

import re
import os
import sys
import wget
import getopt
import requests
from urllib import request, parse

proxies = {}

__version__ ="V1.0.0"
script_name = "porndl"
URL = "http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c"
COOKIES = "-b language=cn_CN;watch_times=0"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"

def download_video_by_url(url, path, title, ext):
    response = requests.get(url)
    outfile = '{}/{}.{}'.format(path, title, ext)
    if response.status_code == 200:
        with open(outfile, 'wb') as f:
            f.write(response.content)
    return True

def pick_a_chinese_proxy():

    import random
    from bs4 import BeautifulSoup
    
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

def get_html(urls):
    
    for url in urls:
        if url.startswith('https://'):
            url = url[8:]
        if not url.startswith('http://'):
            url = 'http://' + url

    if auto_proxy:
        extractor_proxy = pick_a_chinese_proxy()
        proxies['http'] = 'http://{}'.format(extractor_proxy)
        print("Using Chinese proxy {}".format(extractor_proxy))

    r = requests.get(url, proxies=proxies)
    html = r.content.decode('utf-8')

    r = re.search(r'^(.*)/\w+', url)
    assert r
    domain = r.group(1)
    if domain and traceback:
        print('domain : {}'.format(domain))
    
    r = re.search("so.addVariable\(\'file\',\'(.*)\'\);\n{1,10}", html)
    assert r
    vid = r.group(1)
    if vid and traceback:
        print('vid : {}'.format(vid))

    r = re.search("so.addVariable\(\'max_vid\',\'(.*)\'\);\n{1,10}", html)
    assert r
    max_vid = r.group(1)
    if max_vid and traceback:
        print('max_vid : {}'.format(max_vid))

    r = re.search("so.addVariable\(\'seccode\',\'(.*)\'\);\n{1,10}", html)
    assert r
    seccode = r.group(1)
    if seccode and traceback:
        print('seccode : {seccode}'.format(seccode=seccode))

    r = re.search("so.addVariable\(\'mp4\',\'(.*)\'\);\n{1,10}", html)
    assert r
    mp4 = r.group(1)
    if mp4 and traceback:
        print('mp4 : {}'.format(mp4))

    r = re.search(r'<title>\W{1,10}(.*)\n.*</title>', html)
    assert r
    title = r.group(1).replace(' ', '-')
    if title and traceback:
        print('title : {}'.format(title))

    jsonurl = domain + "/getfile.php?VID=" + vid + "&mp4=" + mp4 + "&seccode=" + seccode + "&max_vid=" + max_vid
    if jsonurl and traceback:
        print('jsonurl : {}'.format(jsonurl))

    ret = requests.get(jsonurl, proxies=proxies)
    data = ret.content.decode('utf-8')
    resp = re.search("^file=(.*)&domainUrl.*", data)
    assert resp

    download_url = parse.unquote(resp.group(1))
    if traceback:
        print("Real URLs : {}".format(download_url))

    try:
        if download_video_by_url(download_url, output_dir, title, 'mp4') and traceback:    
            print('download successful !!!')
    except KeyboardInterrupt:
        if traceback:
            raise
        else:
            sys.exit(1)
    finally:
        print('Processing download successful !!!')

    #filename = wget.download(parse.unquote(resp.group(1)))
    #filename = wget.download(parse.unquote('http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'))

def print_info():
    return True

def parse_args(script_name, **kwargs):

    help = 'Usage: %s [OPTION]... [URL]...\n\n' % script_name
    help += '''Startup options:
    -V | --version                      Print version and exit.
    -h | --help                         Print help and exit.
    \n'''
    help += '''Download options:
    -o | --output-dir <PATH>            Set output directory.
    -a | --auto-proxy                   Auto choice an Chinese HTTP proxy.
    -c | --cookies <COOKIES_FILE>       Load cookies.txt or cookies.sqlite.
    -x | --http-proxy <HOST:PORT>       Use an HTTP proxy for downloading.
    -d | --debug                        Show traceback and other debug info.
    '''

    short_opts = 'Vhdac:o:x:'
    opts = ['version', 'help', 'debug', 'auto-proxy', 'cookies=', 'output-dir=', 'http-proxy=']

    # Get options and arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        print(err)
        print("try 'porndl --help' for more options")
        sys.exit(2)

    global traceback
    global auto_proxy
    global output_dir

    output_dir = '.'
    traceback = False
    auto_proxy = False

    for o, a in opts:
        if o in ("-V", "--version"):
            print('porndl version : {}'.format(__version__))
            sys.exit()
        elif o in ("-h", "--help"):
            print(help)
            sys.exit()
        elif o in ('-c', '--cookies'):
            print('cookies is {}'.format(a))
        elif o in ('-d', '--debug'):
            traceback = True
        elif o in ('-a', '--auto-proxy'):
            auto_proxy = True
        elif o in ("-o", "--output-dir"):
            output_dir = a
        elif o in ("-x", "--http-proxy"):
            proxies['http'] = 'http://' + a
        else:
            print("try 'porndl --help' for more options")
            sys.exit(2)

    if not args:
        print(help)
        sys.exit()

    get_html(args)

def main(**kwargs):
    parse_args('porndl', **kwargs)

if __name__ == "__main__":
    main()
