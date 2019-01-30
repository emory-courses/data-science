from typing import List


def generate_html_files(url_exam: str, url_class: str, html_dir: str):
    """
    Generates one HTML file per program (e.g., QTM) under the `html/` directory
    that displays the exam and class information together for that program.
    :param url_exam: the URL to the exam schedule page.
    :param url_class: the URL to the class schedule page.
    :param html_dir: the directory path where the HTML files are to be generated.
    """
    # TODO: to be updated
    pass


def print_exam_schedule(course_ids: List[str]):
    """
    Prints the exam schedules of the input courses.
    :param course_id: `<program><number>-<section>` (e.g., `QTM385-1`)
    """
    # TODO: to be updated
    for course_id in course_ids:
        print(course_id)


if __name__ == '__main__':
    url_exam = 'http://registrar.emory.edu/faculty-staff/exam-schedule/spring-2019.html'
    url_class = 'http://atlas.college.emory.edu/class-schedules/spring-2019.php'
    html_dir = 'html/'

    generate_html_files(url_exam, url_class, html_dir)
    print_exam_schedule(['AAS100-1', 'QTM385-1'])
