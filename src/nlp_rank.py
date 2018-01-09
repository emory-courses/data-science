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
import bibtexparser
import os

__author__ = 'Jinho D. Choi'


def crawl_aclbib(map_file, out_dir):
    """
    Crawl bib files from the ACL Anthology.
    :param map_file: '../dat/aclbib_map.tsv'
    :param out_dir: '../dat/aclbib/'
    """
    fin = open(map_file)

    for line in fin:
        l = line.split()

        if l and l[2] == 'Y':
            bib = l[0]
            out = os.path.join(out_dir, bib)
            if os.path.isfile(out): continue
            url = os.path.join('http://www.aclweb.org/anthology', bib[0], bib[:3], bib)

            print(url)
            dat = urlopen(url).read()
            fout = open(out, 'wb')
            fout.write(dat)



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
    crawl_aclbib('../dat/aclbib_map.tsv', '../dat/aclbib/')