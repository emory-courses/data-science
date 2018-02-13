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
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

__author__ = 'Jinho D. Choi'

url = 'https://raw.githubusercontent.com/emory-courses/data-science/master/dat/courses/qtm-spring-2018.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
schedule = soup.find('div', {'id': 'exam_schedule-landing-page'})

for t in schedule.find_all('div', {'class': 'schedules'}):
    print(t)






# html = driver.page_source
#
# fout = open('qtm-spring-2018.html', 'w')
# fout.write(html)




#

#
#
#
#
# # constants
# BIB_DIR = '/Users/jdchoi/Desktop/bibs/'
#
# # read bib file
# # read_bibs(BIB_DIR)
#
#
#
# def comment_threads_list_by_video_id(client, **kwargs):
#   # See full sample for function
#   kwargs = remove_empty_kwargs(**kwargs)
#
#   response = client.commentThreads().list(
#     **kwargs
#   ).execute()
#
#   return print_response(response)
#
# comment_threads_list_by_video_id(client,
#     part='snippet,replies',
#     videoId='m4Jtj2lCMAA')