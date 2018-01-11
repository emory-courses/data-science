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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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




# url = 'http://registrar.emory.edu/faculty-staff/exam-schedule/spring-2018.html'
# r = requests.get(url)
# top = BeautifulSoup(r.text, 'html.parser')
# tbody = top.find('tbody')
# schedule = {}
#
# for tr in tbody.find_all('tr'):
#     tds = tr.find_all('td')
#     meet = tds[0].string
#     day = tds[1].string
#     date = tds[2].string
#     time = tds[3].string
#     schedule[meet] = (day, date, time)

#
# url = 'http://registrar.emory.edu/faculty-staff/exam-schedule/spring-2018.html'
# schedule = read_exam_schedule(url)
# for k,v in schedule:
#     print('%10s: %s' % (k, v))


# url = 'http://atlas.college.emory.edu/schedules/index.php'
# s = requests.session()
# r = s.get(url)
# r = s.get(url, params={'select': 'QTM'})
#
# url = 'http://atlas.college.emory.edu/schedules/index.php'
# s = requests.session()
# r = s.get(url)
# print(r.text)
#
# url = 'http://atlas.college.emory.edu/schedules/index.php'
# r = s.get(url, params={'select': 'QTM'})
# print(r.text)

# read_exam_schedule(url)

wd = webdriver.Chrome()
url = 'https://www.usnews.com/best-colleges/search?_mode=table&page=91&_page=91'

wd.get(url)
print(wd.page_source)
wd.quit()


# WebDriverWait(wd, 10).until(expected_conditions.visibility_of_all_elements_located((By.ID, 'search-application-results-view')))

