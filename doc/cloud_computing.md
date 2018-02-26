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

* Open a terminal and go to the directory where your key pair is saved. Enter the `ssh` command you just copied on the terminal:

   ```
   cd /Users/jdchoi/workspace
   ssh -i jdchoi.pem ubuntu@ec2-xx-xxx-xx-x.compute-1.amazonaws.com
   ```

* Say `yes` for the connection (this appears only for the first time):

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

## Configure Python on the EC2 instance

* Python 3.5.x is already installed on AWS Ubuntu machines.

   ```
   ubuntu@ip-172-31-69-246:~$ python3
   Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
   [GCC 5.4.0 20160609] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   ```

* 
   