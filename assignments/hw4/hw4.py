from bs4 import BeautifulSoup
import requests

def get_schedule(url):
    r = requests.get(url)

    html = BeautifulSoup(r.text, 'html.parser')
    tbody = html.find('tbody')
    schedule = []

    for tr in tbody.find_all('tr'):
        tds = tr.find_all('td')
        class_time = tds[0].string.strip()
        exam_day = tds[1].string.strip()
        exam_date = tds[2].string.strip()
        exam_time = tds[3].string.strip()
        schedule.append([class_time, exam_day, exam_date, exam_time])

    return schedule


def lambda_handler(event, context):
    url = 'http://registrar.emory.edu/faculty-staff/exam-schedule/spring-2019.html'
    schedule = get_schedule(url)
    return schedule
