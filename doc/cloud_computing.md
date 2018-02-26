## Create an EC2 instance

* Login to your AWS account.
* Click the `Launch Instance` button on the `Instances` page.
* Choose the instance type of `Ubuntu Server 16.04 LTS (HVM)`.
* Choose the `t2.micro` machine that is free-tier eligible.  This instance type can be reconfigured later on.
* Click the `Review and Launch` button.
* When you click the `Launch` button, it will ask you to choose a key pair.  Create a new key pair (e.g., `jdchoi.pem`) and save it to your local machine.  You will not be able download this key pair again so remember where you save it.  DO NOT DISTRIBUTE THIS IN ANY PUBLIC DOMAIN. Anyone with this key pair will be able to give serious damages to your AWS account.

## Connect to the EC2 instance

* Go to the `Instances` page.

* Select the instance you just created.

* Click the `Connect` button and copy the `ssh` command at the bottom.  It should look something like:

   ```
   ssh -i "jdchoi.pem" ubuntu@ec2-xx-xxx-xx-x.compute-1.amazonaws.com
   ```

* Open a terminal and go to the directory where your key pair is saved (e.g., `/Users/jdchoi/workspace`). Enter the `ssh` command you just copied on the terminal:

   ```
   $ cd /Users/jdchoi/workspace
   $ ssh -i jdchoi.pem ubuntu@ec2-xx-xxx-xx-x.compute-1.amazonaws.com
   ```

* Say `yes` to make the connection (this appears only for the first time):

   ```
   Are you sure you want to continue connecting (yes/no)? yes
   ```

* If you see the following welcome prompt, you are successfully logged into your own EC2 instance:

   ```
   Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-1049-aws x86_64)
   
    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

     Get cloud support with Ubuntu Advantage Cloud Guest:
       http://www.ubuntu.com/business/services/cloud
   ```

## Configure the Python Environment

* Update `apt-get`, that is a [package management](https://help.ubuntu.com/community/AptGet/Howto?action=show&redirect=AptGet) tool for Ubuntu:

   ```
   $ sudo add-apt-repository ppa:deadsnakes/ppa
   $ sudo apt-get update
   ```

* Install python 3.6:

   ```
   $ sudo apt-get install python3.6
   ```

* Install `pip`:

   ```
   $ sudo apt-get install python-pip
   ```

* Install `virtualenv`:

   ```
   $ sudo apt-get install python-virtualenv
   ```

* Create a virtual environment for python 3.6:

   ```
   $ virtualenv --python=/usr/bin/python3.6 ~/env
   ```
   
* Activate the virtual environment you just created:

   ```
   $ source env/bin/activate
   ```

* Check the default python version

   ```
   (env) $ python --version
   Python 3.6.4
   ```

## Synchronize Source Codes

* Open another terminal and go to the local directory where your key pair is saved (e.g., `/Users/jdchoi/workspace`):

   ```
   $ cd /Users/jdchoi/workspace
   ```

* Create a directory called `src` in that directory:

   ```
   $ mkdir src
   ```
   
* Go to the `src` directory and create a file called `hello.py` using the following commands:

   ```
   $ cd src
   $ echo "print('Hello World')" > hello.py
   ```

* Go to the upper level directory:

   ```
   $ cd ..
   ```

* Synchronize the `src` directory with your EC2 instance:

   ```
   $ rsync -avz --delete --exclude=.DS_Store -e "ssh -i jdchoi.pem" src ubuntu@ec2-xx-xxx-xx-x.compute-1.amazonaws.com:/home/ubuntu
   ```
   
* Go back to the terminal that is connected to the EC2 instance, and check the `src` directory you just synchronized:

   ```
   $ ls -la src
   ```
   
* Run `hello.py`:

   ```
   python src/hello.py
   ```
   
## Download Public Data

* Download the [`aclweb-txt-180214.tgz`](https://s3.amazonaws.com/elit-public/nlp-ranking/aclweb-txt-180214.tgz):

   ```
   wget https://s3.amazonaws.com/elit-public/nlp-ranking/aclweb-txt-180214.tgz
   ```

* Uncompress the downloaded file:

   ```
   tar -zxvf aclweb-txt-180214.tgz
   ```

* There should be the `txt` folder created from this uncompression:

   ```
   ls -la txt
   ``` 

