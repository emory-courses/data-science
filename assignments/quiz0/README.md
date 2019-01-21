Getting Started
=====

## Python

* Install [Python 3.6.x](https://www.python.org/downloads/) or above.
* Note that lower versions of Python will not be compatible to this course.


## Git Repository

* Login to [Github](https://github.com) (create an account if you do not have one). 
* Create a new repository called `qtm385` and make it PRIVATE.
* From the `Settings` menu, add the TA as collaborators of this repository.
  * Han He: `hankcs`.


## PyCharm

* Install [PyCharm](https://www.jetbrains.com/pycharm/download/) on your local machine.
  * The following instructions assume that you have "PyCharm 2018.3.3 Professional Edition".
  * You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Create a new project:
  * Click `Check out from Version Control` and select `Git`.
  * Click `Log in to Github` and enter your Github ID and password. If you are using two-factor authentication, login with your [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).
  * Enter your repository URL (e.g., `https://github.com/your_id/qtm385.git`) and clone it.  Make sure the directory name is `qtm385`.
* Setup the interpreter:
  * Go to `[Preferences - Project: qtm385 - Project Interpreter]`.
  * Click the gear button on the righthand side and select `Add`.
  * In the prompted window, select `Virtualenv Environment` and choose `Python 3.6.x` as the base interpreter.
* Install a package:
  * Go to `[Preferences - Project: qtm385 - Project Interpreter]`.
  * Click the `+` sign at the bottom.
  * Search and install for the `requests` package.
* Create a new package:
  * At any step, if it prompts you to add a new file/package to git, click `Add`.
  * Create a python package called `quiz0`.
  * Create a python file called [`quiz0.py`](src/quiz0.py) under the `quiz0` package and copy all the code. 
  * Run `quiz0` by clicking `[Run -> Run]`.
  * If `quiz0.html` is created under the `quiz0` package, your program runs successfully.


## Jupyter Notebook

* Install [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html).
* On a terminal, go to the `qtm385` directory.
* Enter the following command to activate the virtualenv:
  ```
  $ source venv/bin/activate
  ```
* Enter the following command to launch Jupyter Notebook:
  ```
  (venv) $ jupyter notebook
  ```
* On the web-browser where it is launched, choose the `quiz0` directory.
* Create a new notebook called `quiz0` and run the following code:
  ```python
  import requests
  r = requests.get('http://www.cs.emory.edu/~choi')
  print(r)
  ```
* If you see `<Response [200]>`, your notebook runs successfully.


## Submission

* From PyCharm, add the followings to git by right clicking on those files and choosing `[Git - Add]`:
  * `quiz0/quiz0.html`
  * `quiz0/quiz0.ipynb`
  * `quiz0/quiz0.py`
* Once the files are added to git, they should turn into green. If not, restart PyCharm and add the files again.
* Create a file called `.gitignore` under the `qtm385` directory and copy the followings:
  ```
  .idea/
  venv/
  */.ipynb_checkpoints/
  ```
* Commit and push your changes to Github:
  * Right click on `qtm385`, choose `[Git - Commit Directory]`, enter a message (e.g., "Submit quiz 0."), and click `[Commit and Push]`.
  * Make sure ones in `.gitignore` are not getting pushed to Github.
* Check if the above files are properly pushed to Github.
* Submit the address of your `qtm385` repository (e.g., https://github.com/your_id/qtm385.git): https://canvas.emory.edu/courses/57068/assignments/201526
