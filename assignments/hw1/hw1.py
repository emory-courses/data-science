from typing import List


def generate_html_files(url_exam: str, url_class: str):
    """
    Generates one HTML file per program (e.g., QTM) under the `html/` directory
    that displays the exam and class information together for that program.
    :param url_exam: the URL to the exam schedule page.
    :param url_class: the URL to the class schedule page.
    """
    # TODO: to be updated
    pass


def print_exam_schedule(course_id: str):
    """

    :param course_id:
    :return:
    """



if __name__ == '__main__':
    url_exam = 'http://registrar.emory.edu/faculty-staff/exam-schedule/spring-2019.html'
    url_class = 'http://atlas.college.emory.edu/class-schedules/spring-2019.php'

    generate_html_files(url_exam, url_class)

