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
import os
import re
from types import SimpleNamespace
import bibtexparser
import requests

__author__ = 'Jinho D. Choi'


def load_map(map_file):
    """
    :param map_file: ../dat/aclbib_map.tsv
    :return: a dictionary where the key is the conference/journal ID and the value is a namespace of (weight, title).
    """
    fin = open(map_file)
    d = {}

    for i, line in enumerate(fin):
        l = line.split('\t')
        if l:
            key = l[0]
            d[key] = SimpleNamespace(weight=float(l[1]), title=l[2])

    return d


def crawl_aclbib(acl_map, out_dir):
    """
    :param acl_map: the output of load_map().
    :param out_dir: the output directory where the bib files are stored.
    """
    re_bib = re.compile('<a href="([A-Z]\d\d-\d\d\d\d\.bib)">bib</a>')
    acl = 'http://www.aclweb.org/anthology'

    for k, v in acl_map.items():
        out = os.path.join(out_dir, k+'.bib')
        if os.path.isfile(out): continue    # skip if already downloaded
        fout = open(out, 'w')
        print(out)

        root_url = os.path.join(acl, k[0], k[:3])            # http://www.aclweb.org/anthology/P/P17
        r = requests.get(os.path.join(root_url, k+'.bib'))   # http://www.aclweb.org/anthology/P/P17/P17-1.bib
        text = r.text.strip()

        if text.startswith('@'):
            fout.write(r.text)
        else:   # bib files are provided individually
            r = requests.get(root_url)

            for bib in re_bib.findall(r.text):
                if bib[:6] in acl_map: continue     # skip workshops handled separately (e.g., CoNLL)
                rs = requests.get(os.path.join(root_url, bib))
                fout.write(rs.text)


def load_bibs(acl_map, bib_dir):
    """
    Populate `acl_map` with the list of bib entries.
    :param acl_map: the output of load_map().
    :param out_dir: the input directory where the bib files are stored.
    """
    entries = []

    for k, v in acl_map.items():
        fin = open(os.path.join(bib_dir, k+'.bib'))
        bib = bibtexparser.loads(fin.read())
        ent = [entry for entry in bib.entries if 'author' in entry]
        # print('%10s: %5d' % (os.path.basename(bib_file), len(ent)))
        v.entries = ent

    return entries


def parse_authors(entry):
    return [author.strip() for author in entry['author'].split(' and ')]


def publications_per_author(acl_map):
    """
    :param acl_map: the output of load_map().
    :return: a dictionary where the key is an author name and the value is a list of author's publications.
    """
    d = {}

    for k, v in acl_map.items():
        for entry in v.entries:
            for author in parse_authors(entry):
                e = (entry['title'], entry['year'], v.weight)
                if author in d:
                    d[author].append(e)
                else:
                    d[author] = [e]

    return d


def rank_author_by_publications(author_pub, weighted=True):
    """
    :param author_pub: the output of publications_per_autho
    :param weighted: if True, rank the authors by weighted publications.
    :return: the ranked list of author with their scores in descending order.
    """
    pass

# filename = 'http://www.aclweb.org/anthology/P/P17/P17-1.bib'
#
# url = urlopen(filename)
#
# bib = bibtexparser.loads(url.read())
# ent = [entry for entry in bib.entries if 'author' in entry]
# entries.extend(ent)
#
#
#
#
# print(html.read())

if __name__ == '__main__':
    MAP_FILE = '/Users/jdchoi/Git/nlp-ranking/dat/aclbib_map.tsv'
    acl_map = load_map(MAP_FILE)

    OUT_DIR = '/Users/jdchoi/Git/nlp-ranking/dat/aclbib/'
    crawl_aclbib(acl_map, OUT_DIR)

    load_bibs(acl_map, OUT_DIR)
    print(sum([len(e.entries) for e in acl_map.values()]))

    author_pub = publications_per_author(acl_map)
    for t in author_pub['Choi, Jinho']: print(t)