# ========================================================================
# Copyright 2018 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import glob
import json

import os
import requests
import sys
from bs4 import BeautifulSoup
from requests.exceptions import ChunkedEncodingError

__author__ = 'Jinho D. Choi'


def extract_sp500():
    url = 'https://en.wikipedia.org/wiki/List_of_S&P_500_companies'
    r = requests.get(url)
    html = BeautifulSoup(r.text, 'html.parser')
    table = html.find('table')
    sp500 = {}

    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if tds:
            symbol = tds[0].find('a').string.strip()
            d = {}
            d['company']    = tds[1].find('a').string.strip()
            d['sector']     = tds[3].string.strip()
            d['industry']   = tds[4].string.strip()
            d['address']    = tds[5].find('a').string.strip()
            d['cik']        = tds[7].string.strip()
            sp500[symbol] = d

    return sp500



if __name__ == '__main__':
    # sp500 = extract_sp500()
    # json.dump(sp500, open('sp500_20180115.json', 'w'))

    apikey = sys.argv[1]
    date = '20180115'
    outdir = '../dat/sp500'
    js = json.load(open('../dat/sp500_20180115.json'))
    syms = set([os.path.basename(c)[:-13] for c in glob.glob(os.path.join(outdir, '*.csv'))])

    for symbol in js:
        if symbol in syms: continue
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&datatype=csv&outputsize=full&symbol=%s&apikey=%s' % (symbol, apikey)

        try:
            r = requests.get(url)
            csvfile = os.path.join(outdir, '%s_%s.csv' % (symbol, date))
            fout = open(csvfile, 'w')
            fout.write(r.text)
            print(symbol)
        except ChunkedEncodingError:
            print('Error: '+symbol)


    #
    # symbol = 'LNT'
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&datatype=csv&outputsize=full&symbol=%s&apikey=%s' % (symbol, apikey)
    # try:
    #     r = requests.get(url)
    #     print(r.text)
    # except ChunkedEncodingError:
    #     print('NO FOUND')
    #
    # print('still got it')

