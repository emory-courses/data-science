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
import re

RE_NUMBER = re.compile('your expression')
RE_DATE = re.compile('your expression')


def norm_number(s):
    """
    :param s: the input string
    :return: the input string where all numbers are converted into their digit-forms.
    """
    return s


def norm_date(s):
    """
    :param s: the input string
    :return: the input string where all dates are standarized.
    """
    return s