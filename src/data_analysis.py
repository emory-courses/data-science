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
from collections import Counter

import math
from fuzzywuzzy import fuzz
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


def term_to_str(term):
    year = term[0]
    if term[1] == 1: t = 'Spring'
    elif term[1] == 6: t = 'Summer'
    elif term[1] == 9: t = 'Fall'
    else: t = ''
    return t, year


def is_research_course(catalog):
    return catalog != '130R' and 'R' in catalog


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


def course_by_instructor(course_info, lastname, include_research=False):
    """
    :param course_info:
    :param lastname: the last name of the professor.
    :param include_research: if True, include research courses; otherwise, exclude them.
    :return: a dictionary where the key is the course number and
             the value is the number of terms that the professor `lastname` taught that course.
    """
    def match(c):
        return c.instructor[0] == lastname and \
               (include_research or not is_research_course(c.catalog))

    courses = {(*c.term, c.subject, c.catalog) for c in course_info if match(c)}
    return Counter([t[2:] for t in courses])


def courses_by_instructors(course_info, include_research=False):
    d = {}
    for c in course_info:
        if include_research or not is_research_course(c.catalog):
            key = c.instructor
            val = (*c.term, c.subject, c.catalog)
            if key in d: d[key].add(val)
            else: d[key] = {val}

    return {k: Counter([t[2:] for t in v]) for k, v in d.items()}


def professor_frequency(inst_course_dict):
    """
    :param inst_course_dict: the output of courses_by_instructors.
    :return: the counter where the key is (subject, catalog) and the value is its frequency count with respect to professors.
    """
    return Counter([k for v in inst_course_dict.values() for k in v.keys()])


def when_did_prof_x_start_teaching_cs_at_emory(course_info, lastname=None, firstname=None, threshold=75):
    """
    :param course_info:
    :param lastname: the last name of the professor.
    :param firstname: the first name of the professor.
    :param threshold:
    :return: if both lastname and firstname are None, the list of all instructors with their first terms.
             if only lastname is provided, the list of all instructors with the last name with their first terms.
             if only firstname is provided, the list of all instructors with the first name with their first terms.
    """
    def match(instructor):
        l = not lastname or fuzz.ratio(lastname.lower(), instructor[0].lower()) >= threshold
        f = not firstname or fuzz.ratio(firstname.lower(), instructor[1].lower()) >= threshold
        return l and f

    # both lastname and firstname are provided
    if lastname and firstname:
        n = next((c for c in course_info if match(c.instructor)), None)
        return [(*n.instructor, *term_to_str(n.term))] if n else []

    # only lastname or firstname is provided
    inst = {}

    for c in course_info:
        key = c.instructor
        if match(key) and key not in inst:
            inst[key] = term_to_str(c.term)

    return [(*k, *v) for k, v in inst.items()]


def what_is_prof_x_special_courses(course_info, lastname):
    """
    :param course_info: the output of load_course_info.
    :param lastname: the last name of the professor.
    :return: a dictionary where the key is (subject, catalog) and value is its TF-IDF score.
    """
    inst_course_dict = courses_by_instructors(course_info)
    prof_freq = professor_frequency(inst_course_dict)
    prof_courses = course_by_instructor(course_info, lastname)  # this is inefficient
    N = len(prof_freq)

    for k, v in prof_courses.items():
        prof_courses[k] *= math.log(N / prof_freq[k])

    return prof_courses


def main():
    csv_file = '../dat/cs_courses_2008_2018.csv'
    course_info = load_course_info(csv_file)
    d = enrollment_by_term(course_info)
    d = enrollment_by_academic_year(course_info)
    d = instructor_by_term(course_info)

    lastname = 'Choi'
    insts = when_did_prof_x_start_teaching_cs_at_emory(course_info, lastname=lastname)
    for inst in insts: print(inst)

    firstname = 'Shun Yang'
    insts = when_did_prof_x_start_teaching_cs_at_emory(course_info, firstname=firstname)
    for inst in insts: print(inst)

    print(course_by_instructor(course_info, 'Choi'))

if __name__ == '__main__':
    main()






