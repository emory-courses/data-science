Homework 0: Getting Started
=====

## Python

* Install [Python 3.6.x](https://www.python.org/downloads/) or above.
* Note that lower versions of Python will not be compatible to this course.


## Git Repository

* Login to [Github](https://github.com) (create an account if you do not have one). 
* Create a new repository called `qtm385` and make it PRIVATE.
* From the `Settings` menu, add the TA as collaborators of this repository.
  * Han He: `hankcs`
* Clone the repository on your local machine:
  ```bash
  $ git clone https://github.com/your_id/qtm385.git
  ```


## PyCharm

* Install [PyCharm](https://www.jetbrains.com/pycharm/download/). You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Lauch PyCharm and create a new project:
   * Select `Pure Python` on the left pane.
   * Choose the `qtm385` directory you just created.
   * Choose an interpreter that is `3.6.x` or above.
   * Click the gear button on the righthand side and select `Create VirtualEnv`. Give `env` as name and choose the `qtm385/env` directory as location.
   * Click the `Create` button at the bottom.
* Install `requests`:
  * Open the `Preferences` pane from the menu and search for `Project Interpreter`.
  * Click the `+` sign at the bottom of the `Project Interpreter` pane.
  * Search for `requests` and click the `Install Package` button.
* Create a python package called `src/hw0`.
* Create the python file [`hw0.py`](src/hw0.py) under the `hw0` package and paste the following code:
   ```python
   import requests

   r = requests.get('http://www.cs.emory.edu/~choi')
   print(r)
   ```
* Run the program by clicking `[Run -> Run]`.
* If you see the following output on the console, your program runs successfully.

   ```
   <Response [200]>
   ```

## Jupyter Notebook

* Install [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html).
* On a terminal, go to the `qtm385` directory.
* Enter the following command to activate the virtualenv:

   ```bash
   $ env/bin/activate
   ```

* Enter the following command to launch Jupyter Notebook:

   ```bash
   (env) $ jupyter notebook
   ```

* On the web-browser where it is launched, create a new notebook and followed the steps in [getting_started.ipyn](../blob/master/doc/getting_started.ipynb).

## Submission

* Run the following code:
   ```python
   import requests

   r = requests.get('http://www.mathcs.emory.edu/~choi')
   print(r.text)
   ```
* Save the output to `hw0.html`.
* Submit `hw0.html` to https://canvas.emory.edu/courses/41979/assignments/105880

