# AWS Setup

Amazon Web Services (AWS) allows you to easily launch computing resources in the cloud.  It provides many services to handle storage (EBS or S3) and computing (EC2 or EMR).  With EC2 we can launch virtual machines that will run in a data center.  These will generally be more powerful machines than our local computers and we can launch one large machine or many machines in a cluster (machines that do distributed computing leveraging a framework like Hadoop or Spark).  AWS also offers a simple UI to write MapReduce code for Hadoop through their EMR offering.  This allows you to not have to maintain a cluster, but just submit a task to an existing cluster.

There are a few steps necessary to get going on AWS.

1. [Claiming your GA credit](#claiming-your-ga-credit)
1. [Creating an AWS account](#creating-an-account)
1. [Retrieving your access keys](#retrieving-your-key-pairs)
1. [Generating a key pair for EC2](#creating-a-key-pair-for-ec2)
1. [SSH to EC2](#ssh-to-ec2)
1. [Launching a Spark Cluster](#launching-a-spark-cluster)

Please note that almost all of these steps are extensively demonstrated in the [slides](./gads23_aws.pdf).


### Claiming your GA credit

As part of your course, General Assembly has given each of you a **$250 AWS credit**, which you can spend on launching boxes, spinning up clusters, deploying websites, storing files, hosting databases and so on.

Your teacher will provide you with a **secret link** to your credit. Please claim your credit well ahead of class, so you're good to go when the times come to login to AWS.

One important warning, if you launch an AWS service, you will be billed. Even if you log out and turn off your computer, you might have several boxes still running in the cloud, adding $$ to your bill. Make sure to kill all services before you stop working, as these numbers can add up. Even more important, never share your AWS keys with anyone, let alone storing them in a public repository like github. For a good laugh read [My $2375 Amazon EC2 Mistake](http://www.devfactor.net/2014/12/30/2375-amazon-mistake/) and you'll be warned enough.

### Creating an account

Please visit [AWS](http://aws.amazon.com).  In the upper right hand side you'll see a login box, you can login here with your Amazon credentials.

Once you've logged in, above the dashboard you'll see a box that lists a region (i.e. U.S. East Virginia or U.S. West Oregon).  This tells us which Amazon datacenter our services will launch in. This may be useful for optimizing performance as we will likely want to ensure that our data and computing resources as well as different nodes in our system are in the same region.

Please select U.S. East Virginia if it is not selected.


### Retrieving your key pairs

- In the right corner select 'Your Name', and then 'Security Credentials'
- Now on the left hand side select Users
- Here you can create a user by selecting 'Create User'.  Create a user with your name.  When prompted download the `credentials.csv` file
- Click on the User you just created, and click on 'Attach Policy'. From the list of policies select `AdministratorAccess` and click attach policy on the bottom right.


### Creating a key pair for EC2

- From the main dashboard, select EC2
- On the left hand side, select KeyPairs, and then create a new one.
- You can name and save the `.pem` locally wherever you'd like (we'll use `~/.aws/ga.pem`)
- Once you've downloaded it, find it locally and run `chmod 600 <keypair_file>.pem`, which sets the proper permissions.


### Launching new EC2 instance

An _EC2 instance_ is just a computer on which you can run your applications.  For example, you could launch an instance to host your Flask website.

- On the ec2 management console go to instances tab on the left
- Select 'Launch Instances'
- Select the first AMI (Amazon Linux AMI)
- Select 'Review and Launch' and then Launch (keep all the defaults)
- On the 'Select Key Pair' screen, select the keypair name your created earlier (should be the default)
- Choose the checkbox (I acknowledge...) and click 'Launch Instances'


### SSH to EC2

To login to your local machine, follow the steps below.

#### Linux and Mac
- Return to the instances tab on the EC2 dashboard
- Select the instance you created (wait until Instance State is 'running' and Statuc Checks are green)
- Right click, and select 'Connect'
- Follow the instructions to ssh into your instance.

You should be able to copy the ssh command  directly from that screen to your terminal. Should like something like:

    ssh -i myKeyPair.pem ec2-user@11.123.123.11

#### Windows
- Download `putty` and `puttygen` from the [PuTTY Download Page](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
- Follow instructions on [Connecting to Your Linux Instance from Windows Using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html?console_help=true).
- After you launch your instance, you can connect to it and use it the way that you'd use a computer sitting in front of you.


#### On your EC2 instance

When you're ssh'ed into your instance, you can use the usual unix commands you're used to (supposed you launched a unix machine).

```sh
ls  # look around in current folder - this is empty
cd /  # go to root folder
ls  # look around there - that's pretty full
cd ~  # go back to home folder
```

You can create a python file and run it.

```sh
echo print \"hello world" > hello.py
python hello.py
```

You should be able to install package easily.

```sh
pip install --upgrade pip
sudo pip install pandas
sudo pip install numpy
```

To copy a file from your local machine to your EC2 instance, go to your local machine, to the folder of your file, and type

```sh
scp -i myKeyPair.pem readme.md ec2-user@11.123.123.11:~  # copies readme.md to the EC2's ~ folder
```

Or, vice versa, downloading a file from the instance to your local machine:

```sh
scp -i myKeyPair.pem ec2-user@11.123.123.11:~/hello.py .  # downloads hello.py from the EC2's ~ folder
```

#### web hosting

If you set up the right permissions in your AWS console, you should be able to run your Flask site on your ec2 instance, and access the website at the same IP address

    http://11.123.123.11


### Launching a Spark Cluster

Amazon EMR simplifies big data processing, providing a managed Hadoop framework that makes it easy, fast, and cost-effective to distribute and process vast amounts of your data across dynamically scalable Amazon EC2 instances. You can also run other popular distributed frameworks such as Spark and Presto in Amazon EMR, and interact with data in other AWS data stores such as Amazon S3 and Amazon DynamoDB.

- From your AWS console open the EMR Dashboard
- Choose 'Create Cluster'
- Edit the following sections:
  - *Cluster Configuration*: give your cluster a name
  - *Software Configuration*:
    - *Release*: Choose 'emr-4.0.0'
    - *Applications*: Choose 'All Applications'
  - *Hardware Configuration*: 3 is a typical number of instances
  - *Security and Access*: select your key pair (see the [above section](#creating-a-key-pair-for-ec2))
- That's it! Click on 'Create Cluster' at the bottom of the page
- Wait for the status to become "Waiting"
- On the cluster details page find "Master public DNS", click on the ssh link.

Please follow the prompted instructions. You will ssh into your master node by typing something along the lines of

    ssh -i ~/.aws/ga.pem hadoop@ec2-52-22-146-230.compute-1.amazonaws.com

The console will ask a security question. Type `yes`.

When ssh'ed into your master node, follow the steps under [Hadoop](./hadoop.md) and [Spark](./spark.md) to get some experience with HDFS and PySpark, respectively.

More information on launching a Spark cluster on AWS can be found on
- [Apache Spark on Amazon EMR](http://aws.amazon.com/elasticmapreduce/details/spark/)
- [Create a Cluster With Spark](https://docs.aws.amazon.com/ElasticMapReduce/latest/ReleaseGuide/emr-spark-launch.html)

