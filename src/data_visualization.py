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
from types import SimpleNamespace

__author__ = 'Jinho D. Choi'


def load_institutes(institute_file):
    fin = open(institute_file)
    d = {}

    for line in fin:
        l = list(map(str.strip, line.split('\t')))
        d[l[1]] = SimpleNamespace(name=l[0], url=l[1], city=l[2], state=l[3])

    fin.close()
    return d


def load_scores(email_file):
    """
    :param email_file: email_map.tsv.
    :return: a dictionary whose key is the publication ID and the value is the list of (inst_domain, score) pairs.
    """
    fin = open(email_file)
    d = {}

    for line in fin:
        l = list(map(str.strip, line.split('\t')))
        if l[-1] != '_':
            scores = []
            d[l[0]] = scores
            for s in l[-1].split(';'):
                t = s.split(':')
                scores.append((t[0], float(t[1])))

    fin.close()
    return d


def measure_scores(inst_map, score_map):
    """
    :param inst_map: the output of load_institutes().
    :param score_map: the output of load_scores().
    :return: a list of institute namespaces where the score field contains the total score of that institute from their publications.
    """
    for pub_id, v in score_map.items():
        for domain, score in v:
            d = domain.split('.')
            for i in range(len(d)-2, -1, -1):
                uid = '.'.join(d[i:])
                if uid in inst_map:
                    inst_map[uid].score += score
                    break

    return [inst for url, inst in inst_map.items() if inst.score > 0.0]


def measure_state_scores(inst_scores):
    """
    :param inst_scores: the output of measure_scores().
    :return: a dictionary where the key is the State ID and the value is the total score of that state w.r.t. their publications.
    """
    states = {}

    for inst in inst_scores:
        states[inst.state] = states.get(inst.state, 0) + inst.score

    return states



if __name__ == '__main__':
    EMAIL_FILE = '/Users/jdchoi/Git/nlp-ranking/dat/email_map.tsv'
    score_map = load_scores(EMAIL_FILE)
    print(len(score_map))

    INSTITUTE_FILE = '/Users/jdchoi/Git/nlp-ranking/dat/us_institutes.tsv'
    inst_map = load_institutes(INSTITUTE_FILE)
    print(len(inst_map))

    inst_scores = measure_scores(inst_map, score_map)
    print(len(inst_scores))

    state_scores = measure_state_scores(inst_scores)
    for k, v in sorted(state_scores.items()):
        print("['%s', %f]," % (k, v))