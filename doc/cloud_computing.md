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

## Synchronize Local/Remote Directories

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

## Confiure a Security Group

* Open the [EC2 dashboard](https://console.aws.amazon.com/ec2) and go to the `Security Groups` page.
* Click the `Create Security Group` button and give an appropriate group name and a description:
  * Security group name: qtm385
  * Description: Practical approaches to Data Science
* Click the `Add Rule` button and add the following two rules:
  * Type: HTTP, Protocol: TCP, Port Range: 80, Source: Anywhere.
  * Type: Custom TCP Rule, Protocol: TCP, Port Range: 5000, Source: Anywhere.
* Click the 'Create' button.
* Go to the `Instances` page and click the EC2 instance you created.
* Click `Actions -> Networking -> Change Security Groups`.
* Choose the security group you just created and click `Assign Security Groups`.


## Configure an Elastic IP

* Go to the `Elastic IPs` page and click `Allocate new address`.
* Click `Allocate` to create a new elastic IP.
* Choose the IP you just created and click `Actions -> Associate address`.
* Choose the instance you created and click `Associate`.


## Setup a Web Server

* Connect to the EC2 instance using `ssh` on a terminal. Note that your domain name now should include the elastic IP you just created:

   ```
   $ ssh -i "jdchoi.pem" ubuntu@ec2-xx-xxx-xx-x.compute-1.amazonaws.com

   ```

* Install the Apache web server:

   ```
   $ sudo apt-get install apache2
   ```

* Check the status of the web server:

   ```
   $ sudo service apache2 status
   apache2.service - LSB: Apache2 web server
    Loaded: loaded (/etc/init.d/apache2; bad; vendor preset: enabled)
   Drop-In: /lib/systemd/system/apache2.service.d
            └─apache2-systemd.conf
    Active: inactive (dead) since Wed 2018-02-28 17:56:14 UTC; 5s ago
      Docs: man:systemd-sysv-generator(8)
   Process: 11434 ExecStop=/etc/init.d/apache2 stop (code=exited, status=0/SUCCESS)
   Process: 11148 ExecStart=/etc/init.d/apache2 start (code=exited, status=0/SUCCESS)    
   ```

* Start the web server:

   ```
   sudo service apache2 restart
   ```

* Check the status again and make sure the web server is active:

   ```
   $ sudo service apache2 status
   apache2.service - LSB: Apache2 web server
    Loaded: loaded (/etc/init.d/apache2; bad; vendor preset: enabled)
   Drop-In: /lib/systemd/system/apache2.service.d
            └─apache2-systemd.conf
    Active: active (running) since Wed 2018-02-28 17:59:18 UTC; 29s ago
      Docs: man:systemd-sysv-generator(8)
   Process: 11434 ExecStop=/etc/init.d/apache2 stop (code=exited, status=0/SUCCESS)
   Process: 11479 ExecStart=/etc/init.d/apache2 start (code=exited, status=0/SUCCESS)
     Tasks: 55
    Memory: 6.3M
       CPU: 64ms
    CGroup: /system.slice/apache2.service
            ├─11496 /usr/sbin/apache2 -k start
            ├─11499 /usr/sbin/apache2 -k start
            └─11500 /usr/sbin/apache2 -k start
   ```

* Go to the `Instances` page, click the EC2 instance you created, copy the public DNS, and paste to a web browser. If you see the **Apache2 Ubuntu Default Page**, the web server is running correctly.

* Go to the `/var/www/html/` directory:

   ```
   cd /var/www/html/
   ```

* Update `index.html` to something else:

   ```html
   <h2>Jinho Choi</h2>
   Professor of Computer Science at Emory University
   ```

* Refresh the page on the web browser.


## Setup a Web Framework

* Activate the virtual environment if it is not already:

   ```
   $ source ~/env/bin/activate
   ```

* Install [Flask](http://flask.pocoo.org/docs/0.12/quickstart/

   ```
   $ pip install Flask
   ```
   
* Create a python file called `hello.py` and paste the following code:

   ```python
   @app.route("/")
   def hello():
       return "Hello World!"
   ```

* Indicate `hello.py` as the default app for Flask:

   ```
   $ FLASK_APP=hello.py
   ```

* Run Flask:

   ```
   $ flask run --host=0.0.0.0
   ```

* Open a browser and type the following URL with your public IP:

   ```
   http://xx.xx.xx.xx:5000
   ```


## Create an Interactive Webpage

* Create a directory called `templates`:

   ```
   $ mkdir templates
   $ cd templates
   ```

* Create a file called `form.html` under the `templates` directory:

   ```
   <form method="POST">
       <input name="text">
       <input type="submit">
   </form>
   ```

* Create  `form.py` above the `templates` directory:

   ```python
   from flask import Flask, request, render_template

   app = Flask(__name__)
	
   @app.route('/')
   def form():
       return render_template('form.html')
	
   @app.route('/', methods=['POST'])
   def form_post():
       text = request.form['text']
       s = [render_template('form.html')]
       s.append('<p>')
       s.append(text.upper())
       s.append('</p>')
       return '\n'.join(s)
   ```

* Run Flask:

   ```
   $ FLASK_APP=form.py
   $ flask run --host=0.0.0.0
   ```