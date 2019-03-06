University Ranking
=====

## Task 1: Email Extraction

Out of 16,321 entries in [`email_map.tsv`](https://github.com/elitcloud/nlp-ranking/blob/master/dat/email_map.tsv), 2,513 of them show mismatches between the number of authors and email addresses ([`email_mismatch.tsv`](https://github.com/elitcloud/nlp-ranking/blob/master/dat/email_mismatch.tsv)).

* Write a program that extracts the missing email addresses from the [text files](https://drive.google.com/open?id=16zdXAltl1H8LnXOGT4AIPe9iG8KjKAx5).
* Update the third column of `email_map.tsv` with the extracted email addresses, where the addresses are delimited by `;`.
* Prioritize your updates to recent non-workshop publications.

## Task 2: Institution Weighting

For each publication, weight individual institutions in terms of their contributions to the publication.

* Write a program that measures the number of times that each institute appears in the email list divided by the total number of email addresses in each publication.
* Come up with your own weighting scheme that makes sense to you.
* Make sure to use the top-level domain name.  For instance, given the email list `[jinho@mathcs.emory.edu, choi@emory.edu]`, your program should give `emory.edu:1.0`, not `mathcs.emory.edu:0.5;emory.edu:0.5`.
* Update the fourth column of `email_map.tsv` with the weights, where the institution and its weight are delimited by `:` and (institution, weight) pairs are delimited by `;`.


## Submission

* Create a package called `hw3` under the `qtm385` project.
* Under the `hw3` package:
  * Create `hw3.py` including all necessary codes to accomplish the above two tasks.
  * Save your `email_map.tsv`.
  * Write a report `hw3.pdf` describing your approach to make `email_map.tsv` as complete as possible.
* Commit and push your changes to your repository.