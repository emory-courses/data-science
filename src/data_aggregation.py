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
import json
import re
import requests
from bs4 import BeautifulSoup

__author__ = 'Jinho D. Choi'

TIME = re.compile('(\d{1,2}):(\d\d)\s*([AaPp]\.?\s*[Mm]\.?)?')


def norm_time(hour, minute, period):
    h = int(hour)
    m = int(minute)

    if period:
        p = period[0].upper()
        if p == 'P': h += 12

    return h * 100 + m


def norm_days(days):
    DAYS = [('M', 0), ('TU', 1), ('W', 2), ('TH', 3), ('F', 4)]
    days = days.upper()
    b = ['0'] * 5

    for d, i in DAYS:
        if d in days:
            b[i] = '1'
            days = days.replace(d, '')

    if 'T' in days:
        b[1] = '1'
        days = days.replace('T', '')

    return int(''.join(b), 2)


def course_title(section):
    a = section.find('a')
    t = a.text.split()
    return t[0], ' '.join(t[1:])


def course_days(section):
    days = [day.string.strip() for day in section.find_all('span', {'class': 'day'})]
    return ''.join(days) if days else '-'


def course_time(section):
    time = section.find('div', {'class': 'time'}).string
    if time:
        t = TIME.findall(time)
        return norm_time(*t[0]), norm_time(*t[1])
    else:
        return -1, -1


def course_location(section):
    loc = section.find('div', {'class': 'location'}).string
    return loc if loc else '-'


def course_instructors(section):
    its = [inst.string.strip() for inst in section.find_all('div', {'class': 'instructor'}) if inst.string]
    return '; '.join(its).strip() if its else '-'


def extract_exam_schedule(url):
    r = requests.get(url)
    html = BeautifulSoup(r.text, 'html.parser')
    tbody = html.find('tbody')
    schedule = {}

    for tr in tbody.find_all('tr'):
        tds = tr.find_all('td')
        t = tds[0].string.split()

        if len(t) == 2:
            time = None
            m = TIME.match(t[0])
            if m: time = norm_time(m.group(1), m.group(2), m.group(3))
            days = norm_days(t[1])

            if time and days:
                if time < 700: time += 1200
                key  = (time, days)
                day  = tds[1].string.strip()
                date = tds[2].string.strip()
                time = tds[3].string.strip()
                schedule[key] = (day, date, time)

    return schedule


def extract_course_info(term_id):
    url = 'http://atlas.college.emory.edu/schedules/index.php'
    s = requests.session()
    s.get(url, params={'t': term_id})
    programs = ['QTM']
    course_info = {}

    for program in programs:
        r = s.get(url, params={'select': program})
        html = BeautifulSoup(r.text, 'html.parser')
        for course in html.find_all('div', {'class': 'course'}):
            course_number = course.find('h3').string
            for section in course.find_all('li', {'class': 'section'}):
                section_id, title = course_title(section)
                days = norm_days(course_days(section))
                time = course_time(section)
                location = course_location(section)
                instructors = course_instructors(section)
                course_info[(course_number, section_id)] = (title, days, time, location, instructors)

    return course_info


if __name__ == '__main__':
    url = 'http://registrar.emory.edu/faculty-staff/exam-schedule/spring-2018.html'
    exam_schedule = extract_exam_schedule(url)
    course_info = extract_course_info('5181')
    course_exam = {}

    for k, v in course_info.items():
        days = v[1]
        time = v[2]
        key = (time[0], days)

        if key in exam_schedule:
            course_exam['-'.join(k)] = exam_schedule[key]

    jsonfile = '../dat/courses/course_exam_spring_2018.json'

    with open(jsonfile, 'w') as fout:
        json.dump(course_exam, fout)

    with open(jsonfile) as fin:
        d = json.load(fin)

    for k, v in d.items():
        print(k, v)
