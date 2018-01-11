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
import requests
from bs4 import BeautifulSoup

__author__ = 'Jinho D. Choi'

TIME = re.compile('(\d{1,2}:\d\d)\s+([A-Za-z]+)')

def get_key(time, day):
    return (time, day)


def read_exam_schedule(url):
    r = requests.get(url)
    top = BeautifulSoup(r.text, 'html.parser')
    tbody = top.find('tbody')
    schedule = {}

    for tr in tbody.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) != 4: continue

        m = TIME.match(tds[0].string.strip())
        if m:
            key = get_key(m.group(1), m.group(2))
            day = tds[1].string.strip()
            date = tds[2].string.strip()
            time = tds[3].string.strip()

            schedule[key] = (day, date, time)

    return schedule




url = 'http://registrar.emory.edu/faculty-staff/exam-exam_schedule/spring-2018.html'
r = requests.get(url)
print(r)

html = BeautifulSoup(r.text, 'html.parser')
tbody = html.find('tbody')
exam_schedule = {}

for tr in tbody.find_all('tr'):
    tds  = tr.find_all('td')
    meet = tds[0].string
    day  = tds[1].string
    date = tds[2].string
    time = tds[3].string
    exam_schedule[meet] = (day, date, time)

for k, v in exam_schedule.items():
    print('%10s: %s' % (k, str(v)))

m = TIME.match('8:00 MW')
print('Time: %s, Day: %s' % (m.group(1), m.group(2)))
m = TIME.match('12:30 TThF')
print('Time: %s, Day: %s' % (m.group(1), m.group(2)))

m = TIME.match('Math*')
print(m)