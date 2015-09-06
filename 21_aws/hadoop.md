# Hadoop

1. [What is Hadoop](#what-is-hadoop)
1. [Launching your cluster](#launching-your-cluster)
1. [Download data](#download-data)
1. [HDFS](#hdfs)


### What is Hadoop

Hadoop is an open-source project containing a MapReduce job scheduler and a distributed filesystem (HDFS).  Both are open-sourced versions of Google projects.  Hadoop sets itself apart from similar systems by integrating computing and storage.  Instead of pulling data on to a computing cluster, compute tasks are sent to the data.  Tasks are completed where the data lives.  Please see the [Further Reading](../further_reading.md#distributed-systems) section for additional papers on this.

Please refer to the presentation on MapReduce for more information on the mapreduce paradigm.

We will cover here some details of the Hadoop File System (HDFS).

### Launching your cluster

Please refer to the [AWS Setup](./aws.md) section to learn how to configure AWS and launch a Spark cluster.

### Download data

Before exploring hadoop and spark, let's download some data to our master node.

To download the San Francisco crime dataset.

```sh
wget https://www.dropbox.com/s/0jmyga0i8r1wesq/train.tsv?dl=0
ls  # see local files
mv "train.tsv?dl=0" train.tsv  # rename to better name
```


To download the MovieLens dataset: _"10 million ratings and 100,000 tag applications applied to 10,000 movies by 72,000 users"_.

```sh
wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
unzip ml-10m.zip
ls  # see local files
ls ml-10M100K/  # see local files in subfolder
```

Note that all unix commands work just fine on your instance.

```sh
ls
cd ml-10M100K
ls
cat movies.dat | head
cat movies.dat | wc -l
cd ~
```

### HDFS

The Hadoop File System (HDFS) is a distributed filesystem that serves as the backbone of Hadoop.  HDFS is easily scalable: more storage is just more machines.  Furthermore, data is replicated across many machines so data is available even with disk or node failures.  Hadoop lets us access files on the special filesystem (which coexists with the local files) using similar command line tools.

Caveats:

- All files are append only - no updates or edits.
- All data is replicated, so if any machine fails no data is lost (but also larger storage overhead)

You might need to initialize hadoop first, since you could otherwise run into an error if you type any of the following commands (such as `hadoop fs -ls`).  Since we'll be using pyspark, you might want to run `pyspark` first, only to terminate it again right after launch.  Just type `pyspark` and then `exit()`, and you're good.  (For more on Spark, see our [spark](./spark.md) section.)

Let's move our data from our instance to the hadoop file system, which will distribute it across the nodes.

```sh
hadoop fs -put ml-10M100K/movies.dat movies.dat
hadoop fs -put ml-10M100K/ratings.dat ratings.dat
hadoop fs -put train.tsv train.tsv
```

You could alternatively use `-copyFromLocal`. Also note that `hdfs dfs` is an equivalent command.
```sh
# these commands are all equivalent
hadoop fs -put train.tsv train.tsv
hadoop fs -copyFromLocal train.tsv
hdfs dfs -put train.tsv train.tsv
hdfs dfs -copyFromLocal train.tsv
```

The hadoop commands are very similar to those of unix. Simply use `hadoop fs -<flag>`. Please see the [offical reference](http://hadoop.apache.org/docs/r2.7.0/hadoop-project-dist/hadoop-common/FileSystemShell.html) for a full list of commands.

To list files, we have something similar to `ls`.

```sh
hadoop fs -ls
```

We see something like
```sh
[hadoop@ip-172-31-22-155 ~]$ hadoop fs -ls
Found 4 items
drwxr-xr-x   - hadoop hadoop          0 2015-09-06 15:27 .sparkStaging
-rw-r--r--   1 hadoop hadoop     522197 2015-09-06 15:29 movies.dat
-rw-r--r--   1 hadoop hadoop  265105635 2015-09-06 15:29 ratings.dat
-rw-r--r--   1 hadoop hadoop  126500415 2015-09-06 15:30 train.tsv
```

To cat files, we type
```sh
hadoop fs -cat train.tsv
hadoop fs -cat train.tsv | head
hadoop fs -cat train.tsv | less
```

When your files are stored in HDFS, we can load them in Spark.

