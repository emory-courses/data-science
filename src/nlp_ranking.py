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
import os
import re
import glob
import codecs
from types import SimpleNamespace

import bibtexparser
import matplotlib.pyplot as plt
import requests
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

__author__ = 'Jinho D. Choi'


# =================================== BIB Collection ===================================

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


def crawl_aclbib(bib_map, bib_dir, out_dir):
    """
    Crawl bib files from ACL Anthology.
    :param bib_map: the output of load_map().
    :param bib_dir: the output directory where the bib files are already stored.
    :param out_dir: the output directory where the bib files will be stored.
    """
    re_bib = re.compile('<a href="([A-Z]\d\d-\d\d\d\d\.bib)">bib</a>')
    acl = 'http://www.aclweb.org/anthology'
    out_files = []

    print('===== Crawl bib files from ACL Anthology =====')

    for k, v in bib_map.items():
        if os.path.isfile(os.path.join(bib_dir, k+'.bib')): continue    # skip if already downloaded
        out_file = os.path.join(out_dir, k+'.bib')
        out_files.append(out_file)
        fout = open(out_file, 'w')
        print(out_file)

        root_url = os.path.join(acl, k[0], k[:3])            # http://www.aclweb.org/anthology/P/P17
        r = requests.get(os.path.join(root_url, k+'.bib'))   # http://www.aclweb.org/anthology/P/P17/P17-1.bib
        text = r.text.strip()

        if text.startswith('@'):    # bib collection is provided
            fout.write(r.text)
        else:                       # bib files are provided individually per papers
            r = requests.get(root_url)

            for bib in re_bib.findall(r.text):
                if bib[:6] in bib_map: continue     # skip specially handled workshops (e.g., CoNLL)
                rs = requests.get(os.path.join(root_url, bib))
                fout.write(rs.text)

        fout.close()

    return out_files


def clean_bibs(in_files, out_dir):
    def get_id(key):
        if key in entry:
            m = re_id.search(entry.pop(key))
            if m: return m.group(1)
        return None

    re_id = re.compile('([A-Z]\d\d-\d\d\d\d)')

    print('===== Clean bib files =====')
    out_files = []

    for in_file in in_files:
        out_file = os.path.join(out_dir, os.path.basename(in_file))
        out_files.append(out_file)
        print(out_file)

        fin = open(in_file)
        bib = bibtexparser.loads(fin.read())
        entries = []

        for entry in bib.entries:
            if 'author' not in entry: continue
            ID = get_id('url')
            if ID is None: ID = get_id('link')
            else: del entry['link']
            if ID is None:
                print(entry['ID'])
            else:
                entry['ID'] = ID
                entries.append(entry)

        db = BibDatabase()
        db.entries = entries
        writer = BibTexWriter()
        with open(out_file, 'w') as bout:
            bout.write(writer.write(db))

    return out_files


def extract_paper_links(bib_files, wget_file):
    print('===== Clean paper links =====')
    fout = open(wget_file, 'w')
    for bib_file in bib_files:
        print(bib_file)
        fin = open(bib_file)
        bib = bibtexparser.loads(fin.read())
        for entry in bib.entries:
            fout.write('wget http://anthology.aclweb.org/%s.pdf\n' % (entry['ID']))
    fout.close()


def save_tacl_bib(txt_file, year, volume):
    def name(n):
        t = n.split()
        return t[-1]+', '+' '.join(t[:-1]) if len(t) > 1 else n.strip()

    entries = []
    d = None
    for i, line in enumerate(open(txt_file)):
        line = line.strip()
        j = i % 3
        if j == 0:
            authors = ' and '.join([name(n) for n in line[9:].split(';')]).strip()
            d = {'ID': line[:8],
                 'ENTRYTYPE': 'article',
                 'author': authors,
                 'journal': 'Transactions of the Association for Computational Linguistics',
                 'year': str(year),
                 'volume': str(volume)}
        elif j == 1:
            d['title'] = line
            entries.append(d)

    db = BibDatabase()
    db.entries = entries
    writer = BibTexWriter()
    with open(txt_file+'.bib', 'w') as bout:
        bout.write(writer.write(db))


def collect_bibs(rank_dir):
    MAP_FILE = os.path.join(rank_dir, 'dat/bib_map.tsv')
    TMP_DIR = os.path.join(rank_dir, 'tmp')
    BIB_DIR = os.path.join(rank_dir, 'bib')
    WGET_FILE = os.path.join(rank_dir, 'wget.sh')

    bib_map = load_map(MAP_FILE)
    in_files = crawl_aclbib(bib_map, BIB_DIR, TMP_DIR)
    # in_list = ['/Users/jdchoi/Git/nlp-ranking/tmp/S17-2.bib']
    bib_files = clean_bibs(in_files, BIB_DIR)
    # bib_files = [os.path.join(BIB_DIR, os.path.basename(p)) for p in glob.glob(os.path.join(TMP_DIR, '*.bib'))]
    extract_paper_links(bib_files, WGET_FILE)


# =================================== BIB Processing ===================================

def load_bibs(bib_map, bib_dir):
    """
    Populate `bib_map` with the list of bib entries.
    :param bib_map: the output of load_map().
    :param bib_dir: the input directory where the bib files are stored.
    """
    re_pages = re.compile('(\d+)-{1,2}(\d+)')

    def parse_name(name):
        if ',' in name:
            n = name.split(',')
            if len(n) == 2: return n[1].strip() + ' ' + n[0].strip()
        return name

    def get(entry):
        entry['author'] = [parse_name(name) for name in entry['author'].split(' and ')]
        return entry

    def valid(entry, weight):
        if weight == 1.0:
            if 'pages' in entry:
                m = re_pages.search(entry['pages'])
                return m and int(m.group(2)) - int(m.group(1)) > 4
            return False

        return 'author' in entry

    for k, v in bib_map.items():
        fin = open(os.path.join(bib_dir, k+'.bib'))
        bib = bibtexparser.loads(fin.read())
        v.entries = [get(entry) for entry in bib.entries if valid(entry, v.weight)]
        # print('%10s: %5d' % (k, len(v.entries)))


def extract_emails(txt_dir):
    """
    :param txt_dir: the input directory containing all text files.
    :return: a dictionary where the key is the publication ID and the value is the list of authors' email addresses.
    """
    for text_file in glob.glob(os.path.join(txt_dir, '*.txt')):
        fin = codecs.open(text_file, encoding='utf-8')
        abstract = False

        for line in fin:
            line = line.strip().lower()
            if line == 'abstract':
                abstract = True
                break
            elif line == 'introduction':
                abstract = True
                break

        if not abstract:
            print(text_file)



# =================================== Exercises ===================================

def publications_per_author(bib_map):
    """
    :param bib_map: the output of load_map().
    :return: a dictionary where the key is an author name and the value is a list of author's publications.
    """
    d = {}

    for k, v in bib_map.items():
        for entry in v.entries:
            for author in entry.author:
                e = (entry['title'], entry['year'], v.weight)
                d.setdefault(author, []).append(e)

    return d


def rank_authors_by_publications(author_pub, weighted=True):
    """
    :param author_pub: the output of publications_per_author()
    :param weighted: if True, rank the authors by weighted publication scores; otherwise, by publication counts.
    :return: the ranked list of authors with their publication scores in descending order.
    """
    def count(pubs):
        return sum(pub[2] for pub in pubs) if weighted else len(pubs)   # pub[2]: weight

    return sorted([(k, count(v)) for k, v in author_pub.items()], key=lambda x: x[1], reverse=True)


def plot_scores_by_year(author_pub, name, weighted=True):
    """
    :param author_pub: the output of the publications_per_author()
    :param name: the full name of the author (e.g., Jinho D. Choi)
    :param weighted: if True, use weighted publication scores; otherwise,
    :return:
    """
    d = {}
    for pub in author_pub[name]:
        year = pub[1]
        score = pub[2] if weighted else 1
        if year in d: d[year] += score
        else: d[year] = score

    xs, ys = zip(*[(k, v) for k, v in sorted(d.items())])
    plt.scatter(xs, ys)
    plt.plot(xs, ys)
    plt.grid(b='on')
    plt.show()








if __name__ == '__main__':
    collect_bibs('/Users/jdchoi/Git/nlp-ranking')


    MAP_FILE = '/Users/jdchoi/Git/nlp-ranking/dat/bib_map.tsv'
    BIB_DIR = '/Users/jdchoi/Git/nlp-ranking/bib/'
    TXT_DIR = '/Users/jdchoi/Git/nlp-ranking/txt/'

    # acl_map = load_map(MAP_FILE)
    # load_bibs(acl_map, BIB_DIR)

    # extract_emails(TXT_DIR)


    # extract_paper_urls(acl_map, '/Users/jdchoi/Git/nlp-ranking/txt', '/Users/jdchoi/Git/nlp-ranking/wget.sh')


    # check_bibs(acl_map)

    # save_tacl_bib('/Users/jdchoi/Git/nlp-ranking/Q17.txt', 2017, 5)

    # clean_tacl_bib('/Users/jdchoi/Git/nlp-ranking/dat/aclbib/Q16.bib', '/Users/jdchoi/Git/nlp-ranking/Q16.bib', 'Q16-10')

    # crawl_aclbib(acl_map, BIB_DIR)
    # author_pub = publications_per_author(acl_map)
    # extract_paper_urls(acl_map, WGET_FILE)




