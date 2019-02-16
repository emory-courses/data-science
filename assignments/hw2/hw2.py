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


def course_trend(course_info):
    """
    :param course_info: the output of load_course_info().
    :return: a dictionary where the key is a course ID (e.g., 'CS170') and
             the value is the likelihood of each course being offered in the Fall and Spring terms (e.g., (0.3, 0.7).
    """
    trend = dict()
    # TODO: to be filled
    return trend


def special_topics(course_info):
    """
    :param course_info: the output of load_course_info().
    :return: a dictionary where the key is a professor name (e.g., 'Jinho D Choi') and the value is the professor's
             special graduate courses excluding research courses ranked in descending order.
    """
    topics = dict()
    # TODO: to be filled
    return topics


def vector_plot(course_info):
    """
    :param course_info: the output of load_course_info().
    """
    pass


if __name__ == '__main__':
    csv_file = 'cs_courses_2008_2018.csv'
    course_info = load_course_info(csv_file)
    trend = course_trend(course_info)
    topics = special_topics(course_info)
    vector_plot(course_info)
