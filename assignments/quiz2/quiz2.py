def load_course_info(csv_file):
    with open(csv_file) as fin:
        reader = csv.reader(fin)
        course_info = [info(row) for i, row in enumerate(reader) if not skip(i, row)]
    
    return course_info


def instructor_by_academic_year(course_info):
    # TODO: to be filled
    pass


if __name__ == '__main__':
    csv_file = 'cs_courses_2008_2018.csv'
    course_info = load_course_info(csv_file)
    instructor_by_academic_year(course_info)
