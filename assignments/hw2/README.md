Data Analysis
=====

## Getting Started

* Create a package called `hw2` under the `qtm385` project.
* Copy [`hw2.py`](hw2.py) and [`cs_courses_2008_2018.csv`](https://raw.githubusercontent.com/emory-courses/data-science/master/course/data_analysis/res/cs_courses_2008_2018.csv) under the `hw2` package.


## Task 1

Complete the `course_trend` function in `hw2.py` that takes `course_info` and returns a dictionary where the key is a course ID (e.g., `CS170`) and the value is the likelihood of that course being offered in the Fall and Spring terms; in other words, the value is a tuple of two floats (e.g., `(0.4, 0.6)`) where the first and the second floats represent the likelihoods of the Fall and Spring terms being offered, respectively.

```python
def course_trend(course_info):
    """
    :param course_info: the output of load_course_info().
    :return: a dictionary where the key is a course ID and the value is the likelihood of that course being offered in the Fall and Spring terms. 
    """
    trend = dict()
    # TODO: to be filled
    return trend
```

In your report, describe how you measure the likelihoods.


## Task 2

Complete the `special_topics` function in `hw2.py` that takes `course_info` and returns a dictionary where the key is a professor name (e.g., 'Jinho D Choi') and the value is the list of the professor's special graduate courses ranked in descending order.

```python
def special_topics(course_info):
    """
    :param course_info: the output of load_course_info().
    :return: a dictionary where the key is a professor name (e.g., 'Jinho D Choi') and the value is the professor's
             special graduate courses excluding research courses ranked in descending order.
    """
    topics = dict()
    # TODO: to be filled
    return topics
```

In your report, describe how you rank each professor's graduate courses.


## Task 3

Complete the `vector_plot` function in `hw2.py` that that takes `course_info` and creates vectors for all professors with respect to their graduate courses and plot them into a 2D space using t-SNE.

```python
def vector_plot(course_info):
	# TODO: to be filled
    pass
```

Note that t-SNE may produce different results every time you run.
Include several plots in your reports and explain which ones make sense.
Also, discard instructors who have not taught any graduate course.


## Submission

* Make sure that your `hw2.py` runs as expected before submitting.
* Write a report and save it as `hw2.pdf` under the `hw2` package.
* Add the `hw2` package to git:
  * `hw2/hw2.py`
  * `hw2/hw2.pdf`
* Commit and push your changes to Github.
* Submit: https://canvas.emory.edu/courses/57068/assignments/209631