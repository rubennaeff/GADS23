# Apache Spark

Apache Spark is a distributed data processing system written in Scala. It builds on the ideas of map-reduce (fault-tolerant distributed data processing on commodity machines) with the addition of caching data between processing operations and smart construction of job dependencies for scheduling and error recovery.

- [Apache Spark](https://spark.incubator.apache.org/)
- [Apache Spark on Amazon EMR](http://aws.amazon.com/elasticmapreduce/details/spark/)


### Preparing your cluster

We assume you have completed the following steps:
- [Setup AWS](./aws.md)
- [Launch a Spark Cluster](./aws.md#launching-a-spark-cluster)
- [Download data to HDFS](./hadoop.md#download-data)


### PySpark

Most importantly for us, Spark supports a Python API to write Python Spark jobs or interact with data on cluster through a shell.

It is also possible to launch an ipython notebook on your master node, and use spark just from within your browser as you are used to.  Unfortunately, AWS's software packages change rapidly, and versions do not always align.  In the current setup, this would require quite some configuration.  We will stick therefore with the regular python interface, but you are free to experiment with the ipython notebook.  You could start your experiment by checking out [gadatascience.com](http://www.gadatascience.com/scaling/pyspark.html).

Assuming you have successfully launched your spark cluster, ssh'ed into your master node and downloaded data to the Hadoop filesystem, you are ready to launch PySpark and experiment with parallel computing.

To launch pyspark, type:

```sh
pyspark
```

You'll see a bunch of text, ending with:

```sh
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.4.1
      /_/

Using Python version 2.6.9 (unknown, Apr  1 2015 18:16:00)
SparkContext available as sc, HiveContext available as sqlContext.
```

Once we've opened up `pyspark` we have access to the `sc` object which gives access to `SparkContext`.  SparkContext gives us access to functions to interact with the Spark environment, for example loading data from HDFS.  The `sqlContext` gives access to the `HiveContext`.

Hive is a data warehouse system for Hadoop to handle querying data on HDFS. Hive presents a SQL-like language (HiveQL) to query the data and translates this into MapReduce jobs. Most importantly you can use SQL skills without learning how to write a MR program.  HiveQL shares much of its syntax from MySQL.  See [Hive DDL](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL) for more information.

Note that this is python 2.6 (!). You are free to upgrade to version 2.7 or 3.x, but it might cause dependency conflicts.

Since this is not ipython, with cannot use the question mark to retrieve information anymore (e.g, `?sc`). Instead, we could print the doc string as follows.

```python
>>> print sc.__doc__

    Main entry point for Spark functionality. A SparkContext represents the
    connection to a Spark cluster, and can be used to create L{RDD} and
    broadcast variables on that cluster.
```

RDD stands for _Resilient Distributed Datasets_ and is the core abstraction of Apache Spark.  It's a collection of records that are partitioned across the machines of the cluster. It supports many common data manipulation operations.


### Data exploration

Let's load the data.  Make sure you already had [copied the data into HDFS](./hadoop.md#download-data) earlier.

```python
data = sc.textFile('train.tsv')
<!-- data = sc.textFile('hdfs:// ...') -->
print data.count()  # count number of samples
data.take(1)  # show first sample
```

Spark supports many of the common data operations you may want: `count`, `filter`, `groupBy`, etc.

As for MapReduce, Spark supports as well
- a `map` function, similar to the map function on a Pandas dataframe, performing some function on every row of the dataset, and
- a `reduce` function to aggregate the values.


```python
movie_data = sc.textFile('movies.dat')
ratings_data = sc.textFile('ratings.dat')
```

Let's answer some simpler questions first ...

```python
# How many movies do we have?
movie_data.count()

# How many ratings do we have?
ratings_data.count()

# How many movies are tagged with Horror?
tags = movie_data.map( lambda x : x.split("::")[-1] )
tags.filter( lambda tag: 'Horror' in tag ).count()

# How can I keep the movie names with the tags?
tags = movie_data.map( lambda x : (x.split("::")[1], x.split("::")[-1]) )
tags.filter( lambda (movie, tag): 'Horror' in tag ).take(20)
```

#### Exercises

- Find all movies that contain horror and comedy

_Exercise:_

Using the IP example above, how can we count the number of movies per category?

```python
#TODO(you)
```
*_HINT:_ You can't ... what's missing?*


### `keyBy` and `join`

Spark also support a `join` operation, but first we need to *key* our datasets on something to join on.

```python
keyed_ratings = ratings_data.keyBy(lambda x: x.split("::")[1])
keyed_movies = movie_data.keyBy(lambda x: x.split('::')[0])
```

Then we can join our datasets.  Joining two keyed datasets return a single keyed dataset where each row is a tuple where the first value is the `key` and the second value is *another* tuple.  In the second tuple the first value is the matched row from dataset 1 and the second is the matched row from dataset 2.

```python
row = ( <key> , (dataset_1_row, dataset_2_row))
joined = keyed_movies.join(keyed_ratings) # This will take some time
```

We only care about a small amount of this data, the movie, the user, the category and rating.  So let's create a simpler dataset that just stores that

```python
def createMovieRow( joined_row ):
    movie_row = joined_row[1][0]
    ratings_row = joined_row[1][1]
    title = movie_row.split("::")[1]
    tags = movie_row.split("::")[-1]
    user = ratings_row.split("::")[0]
    rating = float(ratings_row.split("::")[2])
    return (title, tags, user, rating)

data = joined.map(createMovieRow)
```

#### Exercises

```python
# How many reviews per movie
#TODO(you)

# How many reviews per tag
#TODO(you)

# How many average users per movie
#TODO(you)


### `flatMap`

```python
# Compute the average rating per tag
tag_ratings = data.flatMap( lambda x: [(tag, x[-1]) for tag in x[1].split("|")] )
tag_ratings.groupBy(lambda x : x[0])
           .map( lambda (tag, ratings):
                  (tag, sum(r[1] for r in ratings)/len(ratings)))
           .collect()

```

### Machine Learning

Spark has a common library for machine learning functionality called [mllib](http://spark.apache.org/docs/0.9.0/mllib-guide.html), however the functionality is still sparse.  Additionally, there have been efforts to integrate scikits-learn and Spark [example](https://gist.github.com/MLnick/4707012), [spylearn](https://github.com/ogrisel/spylearn)

Spark has some advantages for machine learning in that it can support multiple passes over a dataset in-memory, a vital operation for machine learning algorithms that require iteration.


<!-- ```python
#Load Data
data = sc.textFile("s3n://elasticmapreduce/samples/pig-apache/input")

#Preview data
data.take(1)

# Count data points
data.count()

# Get first 10 IP addresses
data.map( lambda x: x.split()[0] ).take(10)

# Get Count Of Hits Per IP using Map/Reduce

data.map(lambda x: (x.split()[0], 1)).reduceByKey(lambda a, b : a + b).collect()

# Alternatively Use the Built-In aggregation functions

ips = data.map(lambda x: x.split()[0])

# Using GroupBy
ips.groupBy(lambda x: x).map( lambda kv: (kv[0], len(kv[1]))).collect()

# Using .keyBy and .countValuesByKey
ips.keyBy(lambda x: x).countValuesByKey()

# Using .countByValue()
ips.countByValue()
```
 -->

<!-- ### Movie Lens Dataset

#### Getting the data
First get the MovieLens Dataset, "10 million ratings and 100,000 tag applications applied to 10,000 movies by 72,000 users"

```sh
wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
unzip ml-10m.zip
```

Next move the ml-10m directory to HDFS.

```sh
hadoop fs -put ml-10M100K/movies.dat movies.dat
```
 -->
<!--
ephemeral-hdfs/bin/hadoop fs -copyFromLocal ml-10M100K/ .
-->

<!--
#### Loading in PySpark

```sh
spark/bin/pyspark
```

Loading the data

 -->

