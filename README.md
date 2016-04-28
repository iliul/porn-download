
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

## Set a proxy
```
$ python porndl.py -x 122.227.199.178:9999 http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c
```

## Auto-set proxy
```
$ python porndl.py -a http://email.91dizhi.at.gmail.com.9h4.space/view_video.php?viewkey=10dbdc2e848c104e5f3c
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
    -d | --debug                        Show traceback and other debug info.
```

# TODO
- [x] add auto choice an chinese proxy
- [x] add http proxy
- [ ] add download progress bar
- [ ] support more sites

# References
1. **you-get** -- [https://github.com/soimort/you-get](https://github.com/soimort/you-get)
1. **proxy module** -- [https://github.com/soimort/you-get/pull/1063](https://github.com/soimort/you-get/pull/1063)
