# ========================================================================
# Copyright 2017 Emory University
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
__author__ = 'Jinho D. Choi'

def generate(bigrams, init_word, n=20):
    def generate_aux(sentences, sentence, overall_prob, curr_word, curr_prob):
        sentence.append(curr_word)
        overall_prob += curr_prob
        next_list = bigrams.get(curr_word, None)

        if len(sentence) >= n or next_list is None:
            sentences.append((sentence, overall_prob))
        else:
            for next_word, next_prob in next_list:
                generate_aux(sentences, sentence[:], overall_prob, next_word, next_prob)

    sentences = []
    generate_aux(sentences, [], 0.0, init_word, 0.0)
    return sentences

bigrams = {'John': [('bought', 0.6), ('took', 0.4)], 'Mary': [('studies', 0.3), ('came', 0.7)]}
sentences = generate(bigrams, 'John')
print(sentences)
