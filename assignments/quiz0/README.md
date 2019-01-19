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
  * You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Create a new project:
  * Click `Check out from Version Control` and select `Github`.
  * Select `Password` as the auth type and enter your Github ID and password. If you are using two-factor authentication, select `Token` as the auth type and enter your [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).
  * Enter your repository URL (e.g., `https://github.com/your_id/qtm385.git`) and clone the repository.  Make sure the directory name is `qtm385`.
* Install a plugin:
  * Go to `[Preferences - Plugins]`.
  * Search and install the `.ignore` plugin.
* Setup the interpreter:
  * Go to `[Preferences - Project: qtm385 - Project Interpreter]`.
  * Click the gear button on the righthand side, then click `Add...`. In the prompted window select `Virtualenv Environment`.
  * Change the default `venv` to `env` directory as the location, and choose `Python 3.6.x` as the base interpreter.
* Install a package:
  * Go to `[Preferences - Project: qtm385 - Project Interpreter]`.
  * Click the `+` sign at the bottom.
  * Search and install for the `requests` package.
* Create a new package:
  * Right click on `qtm385`, choose `New - Python Package`, and create a package called `quiz0`. If it prompts to add it to git, click `Yes`.
  * Create a python file called [`quiz0.py`](src/quiz0.py) under the `quiz0` package and copy all the code. If it prompts you to add it to git, click `Yes`.
  * Run `quiz0` by clicking `[Run -> Run]`.
  * If `quiz0.html` is created under the `quiz0` package, your program runs successfully.
* Add `.gitignore`:
  * Right click on `qtm385`, choose `[New - .ignore file - .gitignore file]`, and generate an empty file.
  * Copy the following to `.gitignore`:
    ```
    env/
    */.ipynb_checkpoints/
    ```

## Jupyter Notebook

* Install [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html).
* On a terminal, go to the `qtm385` directory.
* Enter the following command to activate the virtualenv:
  ```
  $ source env/bin/activate
  ```
* Enter the following command to launch Jupyter Notebook:
  ```
  (env) $ jupyter notebook
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

* From PyCharm, add the followings to git by right click on those files and choose `[Git - Add]`:
  * `quiz0/quiz0.html`
  * `quiz0/quiz0.ipynb`
  * `quiz0/quiz0.py`
* Make sure the `env/` or `.ipynb_checkpoints/` directories are ignored by git.
* Commit and push your changes to Github:
  * Right click on `qtm385`, choose `[Git - Commit Directory]`, enter a message (e.g., "Submit quiz 0."), and click `[Commit and Push]`.
* Check if the above files are properly pushed to Github.
* Submit the address of your `qtm385` repository (e.g., https://github.com/your_id/qtm385.git): https://canvas.emory.edu/courses/57068/assignments/201526
