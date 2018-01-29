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
import re
import csv
import numpy as np
import matplotlib.pyplot as plt
from newsapi import NewsApiClient


from detect_peaks import detect_peaks


__author__ = 'Jinho D. Choi'

with open('../dat/statistical_analysis/AAPL_20180115.csv') as fin:
    info = []

    for i, row in enumerate(csv.reader(fin)):
        if i == 0: continue  # skip the header
        date = row[0]
        close = float(row[4])
        info.append((date, close))

info.sort()
begin_date = '2017-00-00'
end_date = '2018-00-00'
threshold = 0.5
sub = [t for t in info if begin_date <= t[0] < end_date]

dates, closes = zip(*sub)
plt.plot(dates, closes, c='green')

peaks = detect_peaks(closes, mpd=10)
peaks = [sub[i] for i in peaks]
plt.scatter(*zip(*peaks), c=['blue']*len(peaks))

valleys = detect_peaks(closes, valley='True', mpd=10)
valleys = [sub[i] for i in valleys]
plt.scatter(*zip(*valleys), c=['red']*len(valleys))

plt.xticks(rotation='vertical', fontsize=6)
plt.grid(b='on')
plt.show()


# newsapi = NewsApiClient(api_key='f5ee86288ae641f4bf67579cfaf190a6')
#
# # f5ee86288ae641f4bf67579cfaf190a6
#
#
# all_articles = newsapi.get_everything(q='apple',
#                                       sources='cnbc',
#                                       # domains='bbc.co.uk,techcrunch.com',
#                                       from_parameter='2017-01-01',
#                                       to='2017-12-31',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=10)
#
# print(all_articles)