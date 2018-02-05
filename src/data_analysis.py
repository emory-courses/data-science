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
import csv
from types import SimpleNamespace

import matplotlib.pyplot as plt

__author__ = 'Jinho D. Choi'


def plot_dict(d):
    xs, ys = zip(*[(k, v) for k, v in sorted(d.items())])
    plt.scatter(xs, ys)
    plt.plot(xs, ys)
    plt.grid(b='on')
    plt.show()


def term_to_year(term):
    """
    :param term: a tuple of (year, term_id).
    """
    return term[0] if term[1] == 9 else term[0] - 1


def term_str(term):
    year = term[0]
    if term[1] == 1: t = 'Spring'
    elif term[1] == 6: t = 'Summer'
    elif term[1] == 9: t = 'Fall'
    return '%s, %d' % (t, year)


def load_course_info(csv_file):
    def skip(i, row):
        return i == 0 or int(row[11]) == 0 or row[12].strip() == '' or row[14].strip() != 'Active'

    def info(row):
        # term is normalized to (year, term_id) (e.g., 5181 -> (2018, 1))
        # term_id = 1: Spring, 6: Summer, 9: Fall
        r = row[0]
        term = (2000 + int((int(r) - 5000) / 10), int(r[-1]))

        # name = lastname,firstname
        r = row[12].split(',')
        instructor = (r[0].strip(), r[1].strip())

        return SimpleNamespace(
            term=term,
            subject=row[3].strip(),
            catalog=row[4].strip(),
            section=row[5].strip(),
            title=row[6].strip(),
            min_hours=int(row[8]),
            max_hours=int(row[9]),
            enrollment=int(row[11]),
            instructor=instructor)

    with open(csv_file) as fin:
        reader = csv.reader(fin)
        course_info = [info(row) for i, row in enumerate(reader) if not skip(i, row)]

    return course_info


def enrollment_by_term(course_info):
    enroll = {}
    for c in course_info:
        term = c.term

    return enroll


def enrollment_by_academic_year(course_info, regular=True, research=True, undergraduate=True, graduate=True):
    enroll = {}
    for c in course_info:
        catalog = c.catalog

        # research courses include 'R' in the catalog, except for '130R'
        if catalog != '130R' and 'R' in catalog:
            if not research: continue
        elif not regular:
            continue

        # undergraduate courses are < 500
        if int(catalog[0]) < 5:
            if not undergraduate: continue
        elif not graduate:
            continue

        year = term_to_year(c.term)
        enroll[year] = enroll.get(year, 0) + c.enrollment

    return enroll


def instructor_by_term(course_info):
    inst = {}
    for c in course_info:
        if c.term in inst:
            inst[c.term].add(c.instructor)
        else:
            inst[c.term] = {c.instructor}

    return inst





if __name__ == '__main__':
    csv_file = '../dat/cs_courses_2008_2018.csv'
    course_info = load_course_info(csv_file)
    d = enrollment_by_term(course_info)
    d = enrollment_by_academic_year(course_info)
    d = instructor_by_term(course_info)






