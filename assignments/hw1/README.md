Data Aggregation
=====

## Getting Started

* Create a package called `hw1` under the `qtm385` project.
* Copy [`hw1.py`](hw1.py) under the `hw1` package.
* Copy [`html/`](html) (including [`index.html`](html/index.html)) under the `hw1` package.

## Task 1

* Update the `generate_html_files` function to generate one HTML file per program (e.g., QTM) under the `html/` directory that displays the exam and class information together for that program:
  * Once the HTML files are generated, all links in [`index.html`](html/index.html) should be active.
  * Feel free to use any contents in [`data_aggregation.ipynb`](../../course/data_aggregation/data_aggregation.ipynb).

## Task 2

* Update the `print_exam_schedule` function that takes a course ID and prints the exam schedule of that course:
  * The format of a course ID: `<program><number>-<section>` (e.g., `QTM385-1`).
  * The output format: `(<day>, <date>, <time>)` (e.g., ``).

  
  Add or create all necessary contents (e.g., packages, constants, functions) to run `quiz1.py` that replicates the results from the class.


Complete the 

Currently, `extract_exam_schedule` and `extract_class_schedule` function do not normalize the class meeting time into military time correctly for afternoon classes.  Update the functions such that it shows correct military time for afternoon classes.

* Add all necessary contents (e.g., packages, constants, functions) to run `quiz1.py` that replicates the results from the class.
* Update the `extract_exam_schedule` function to properly normalize the meeting times for afternoon classes.
* Save the printed output to `quiz1/quiz1.txt`.


## Submission

* Add the `quiz1` package to git:
  * `quiz1/quiz1.py`
  * `quiz1/quiz1.txt`
* Commit and push your changes to Github.
* Canvas: https://canvas.emory.edu/courses/57068/assignments/204706