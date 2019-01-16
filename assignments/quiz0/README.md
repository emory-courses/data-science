Getting Started
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
  ```
  $ git clone https://github.com/your_id/qtm385.git
  ```
* Copy [`.gitignore`](.gitignore) and paste under the `qtm385` directory.


## PyCharm

* Install [PyCharm](https://www.jetbrains.com/pycharm/download/). You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Lauch PyCharm and create a new project:
   * Select `Pure Python` on the left pane.
   * Choose the `qtm385` directory you just cloned.
   * Choose an interpreter that is `3.6.x` or above.
   * Click the gear button on the righthand side and select `Create VirtualEnv`. Give `env` as name and choose the `qtm385/env` directory as location.
   * Click the `Create` button at the bottom.
* Install `requests`:
  * Open the `Preferences` pane from the menu and search for `Project Interpreter`.
  * Click the `+` sign at the bottom of the `Project Interpreter` pane.
  * Search for `requests` and click the `Install Package` button.
* Create a python package called `src/quiz0`.
* Copy [`quiz0.py`](src/quiz0.py) under the `quiz0` package.
* Run the program by clicking `[Run -> Run]`.
* If `quiz0.html` is created under the `quiz0` package, your program runs successfully.


## Jupyter Notebook

* Install [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html).
* On a terminal, go to the `qtm385` directory.
* Enter the following command to activate the virtualenv:

   ```
   $ source env/bin/activate
   ```

* Enter the following command to launch Jupyter Notebook:

   ```bash
   (env) $ jupyter notebook
   ```

* On the web-browser where it is launched, choose the `src/quiz0` directory.
* Create a new notebook called `quiz0` and run the following code:
  ```python
  import requests
  r = requests.get('http://www.cs.emory.edu/~choi')
  print(r)
   ```
* If you see `<Response [200]>`, your notebook runs successfully.


## Submission

* From PyCharm, add the `quiz0` package to git, commit, and push your changes to Github.
* Make sure you DO NOT add the `env` directory to git.
* Check if the `quiz0` package is correctly pushed to Github.
* Submit the address of your `qtm385` repository (e.g., `https://github.com/your_id/qtm385.git`): https://canvas.emory.edu/courses/57068/assignments/201526