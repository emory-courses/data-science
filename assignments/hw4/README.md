Exam Schedule on the Cloud
=====

## Task 0: Getting Started

* Create a package called `hw4` under the `qtm385` project.
* Copy everything in [`hw4`](.) to your `hw1` package.  This allows you to call the installed packages in the AWS lambda envorinment.

## Task 1: Lambda Functiion

Create an AWS lambda function that takes a course ID and returns its final exam schedule.  The input and output follow the same format as the ones specified in the [homework 1](../hw1):

* Course ID: `<program><number>-<section>` (e.g., `QTM385-1`).
* Output: `(<day>, <date>, <time>)` (e.g., `('Thursday', '2-May', '3:00 P.M - 5:30 P.M')`).

Once you are done, compress everything under your `hw4` as a zip file (e.g., `hw4.zip`) and upload to the lambda function.

## Task 2: API Gateway

Connect the lambda function from Task 1 to an API gateway such that it takes a course ID as a parameter in the endpoint URL and returns the exam schedule as the HTTP response.
The endpoint URL would look something like follows:

```
https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/spring2019
```

The URL must accept a course ID as follows:

```
https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/spring2019?course=QTM385-1
```


## Submission

* Create a package called `hw4` under the `qtm385` project.
* Under the `hw4` package:
  * Create `hw4.py` and include all the codes necessary for the lambdda function.
  * Create `README.md` and describe the steps you follow for this homework.
* Commit and push your changes to your repository.
* Submit your endpoint URL to canvas: https://canvas.emory.edu/courses/57068/assignments/217664