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
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
import bibtexparser
import os
import re

__author__ = 'Jinho D. Choi'


def crawl_aclbib(map_file, out_dir):
    """
    Crawl bib files from the ACL Anthology.
    :param map_file: '../dat/aclbib_map.tsv'
    :param out_dir: '../dat/aclbib/'
    """
    acl = 'http://www.aclweb.org/anthology'
    fin = open(map_file)

    for i, line in enumerate(fin):
        if i == 0: continue  # skip the header
        l = line.split()

        if l and l[2] == 'Y':
            bib = l[0]
            out = os.path.join(out_dir, bib)
            if os.path.isfile(out): continue
            url = os.path.join(acl, bib[0], bib[:3], bib)

            print(url)
            dat = urlopen(url).read()
            fout = open(out, 'wb')
            fout.write(dat)


def merge_aclbib(root_url, out_dir):
    r = re.compile('<a href="([A-Z]\d\d-\d\d\d\d\.bib)">bib</a>')
    out = os.path.join(out_dir, os.path.basename(root_url)+'.bib')
    fout = open(out, 'wb')

    for line in urlopen(root_url):
        m = r.search(str(line))
        if m:
            bib = m.group(1)
            url = os.path.join(root_url, bib)
            print(url)
            try:
                dat = urlopen(url).read()
                fout.write(dat)
            except HTTPError as e:
                print(e.code)
            except URLError as e:
                print(e.args)


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
    # crawl_aclbib('../dat/aclbib_map.tsv', '../dat/aclbib/')
    merge_aclbib('http://www.aclweb.org/anthology/Q/Q14', '../dat/aclbib/')