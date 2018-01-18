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
import requests
from bs4 import BeautifulSoup

__author__ = 'Jinho D. Choi'


# wd = webdriver.Chrome()
# url = 'https://www.usnews.com/best-colleges/search?_mode=table&page=91&_page=91'
#
# wd.get(url)
# print(wd.page_source)
# wd.quit()


# WebDriverWait(wd, 10).until(expected_conditions.visibility_of_all_elements_located((By.ID, 'search-application-results-view')))

