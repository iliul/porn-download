
# Porndl

[Porndl](https://github.com/iliul/porndl) is a tiny command-line utility to download videos from the **91porn  site**(:underage:).

# Getting Start

## Prerequisites

* [Python3](https://www.python.org/downloads/)
* [lxml](https://pypi.python.org/pypi/lxml/3.6.0)
* [requests](https://pypi.python.org/pypi/requests/)
* [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)

## Install via pip
```
$ git clone git@github.com:iliul/porndl.git
$ pip3 install -r requirements.txt
```

## Set a http proxy
```
$ python porndl.py -x 122.227.199.178:9999 http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c
```

## Set a socks proxy
```
$ python porndl.py -s 192.168.8.125:1080 1 http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c
```

## Auto-set proxy
```
$ python porndl.py -a http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c
```

## Example
```
(py3k) root@Ubuntu Server:~/code/porndl# python porndl.py http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c
【Stairway-to-the-neighbor-stripped-fuck-Squirt-retransmission】     下载完成     42400.02 KB / 42400.02 KB
```

# Usage
```
Usage: porndl [OPTION]... [URL]...

Startup options:
    -V | --version                      Print version and exit.
    -h | --help                         Print help and exit.
    
Download options:
    -o | --output-dir <PATH>            Set output directory.
    -a | --auto-proxy                   Auto choice an Chinese HTTP proxy.
    -c | --cookies <COOKIES_FILE>       Load cookies.txt or cookies.sqlite.
    -x | --http-proxy <HOST:PORT>       Use an HTTP proxy for downloading.
    -s | --socks-proxy <HOST:PORT>      Use an SOCKS proxy for downloading.
    -d | --debug                        Show traceback and other debug info.
```

# TODO
- [x] support auto choice an chinese proxy
- [x] support http proxy
- [x] support socks proxy
- [x] support download progress bar
- [ ] support more sites

# References
1. **you-get** -- [https://github.com/soimort/you-get](https://github.com/soimort/you-get)
1. **proxy module** -- [https://github.com/soimort/you-get/pull/1063](https://github.com/soimort/you-get/pull/1063)
