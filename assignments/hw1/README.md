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

* Update the `print_exam_schedule` function that takes a list of course IDs and prints the exam schedules of those courses:
  * The format of each course ID: `<program><number>-<section>` (e.g., `QTM385-1`).
  * The output format: `(<day>, <date>, <time>)` (e.g., `('Thursday', '2-May', '3:00 P.M - 5:30 P.M')
`).
* Feel free to use any contents in [`data_aggregation.ipynb`](../../course/data_aggregation/data_aggregation.ipynb).


## Submission

* Make sure that your `hw1.py` runs as expected before submitting.
  * Do not modify `__main__`; we will use this to test your program.
* Add the `hw1` package to git:
  * `hw1/hw1.py`
  * `hw/html/*.html`
* Commit and push your changes to Github.
* Canvas: https://canvas.emory.edu/courses/57068/assignments/206291