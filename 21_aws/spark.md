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

It is also possible to launch an **ipython notebook** on your master node, and use pyspark just from within your browser as you are used to.  Unfortunately, AWS's software packages change rapidly, and versions do not always align.  In the current setup, this would require quite some configuration.  We will stick therefore with the regular python interface, but you are free to experiment with the ipython notebook.  You could start your experiment by checking out [gadatascience.com](http://www.gadatascience.com/scaling/pyspark.html) or [this post](https://gist.github.com/iamatypeofwalrus/5183133).

Assuming you have successfully launched your spark cluster, ssh'ed into your master node and downloaded data to the Hadoop filesystem, you are ready to launch PySpark and experiment with parallel computing.

To launch pyspark, type:

```sh
pyspark
```

You'll see a bunch of text, including:

    Python 2.6.9 (unknown, Apr  1 2015, 18:16:00)
    [GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.

    [...]

    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 1.4.1
          /_/

    Using Python version 2.6.9 (unknown, Apr  1 2015 18:16:00)
    SparkContext available as sc, HiveContext available as sqlContext.

Once we've opened up `pyspark` we have access to the `sc` object which gives access to `SparkContext`.  SparkContext gives us access to functions to interact with the Spark environment, for example loading data from HDFS.  The `sqlContext` gives access to the `HiveContext`.

Hive is a data warehouse system for Hadoop to handle querying data on HDFS. Hive presents a SQL-like language (HiveQL) to query the data and translates this into MapReduce jobs. Most importantly you can use SQL skills without learning how to write a MR program.  HiveQL shares much of its syntax from MySQL.  See [Hive DDL](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL) for more information.

Note that this is python 2.6 (!). You are free to upgrade to version 2.7 or 3.x, but it might cause dependency conflicts.

Since this is not ipython, with cannot use the question mark to retrieve information anymore (e.g, `sc?`). Instead, we could print the doc string as follows.

```python
>>> print sc.__doc__

    Main entry point for Spark functionality. A SparkContext represents the
    connection to a Spark cluster, and can be used to create L{RDD} and
    broadcast variables on that cluster.
```

RDD stands for _Resilient Distributed Datasets_ and is the core abstraction of Apache Spark.  It's a collection of records that are partitioned across the machines of the cluster. It supports many common data manipulation operations.


### Simple example

The `parallelize` command distributes a large dataset across its nodes.

```python
>>> nums = sc.parallelize(xrange(1000000))
>>> nums
PythonRDD[1] at RDD at PythonRDD.scala:43
```

Note that `sc.parallize` returns an RDD object. You can call `take` to show its first entries.

```python
>>> nums.take(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Most of the usual pandas functions work here as well.

```python
>>> nums.count()
1000000
>>> nums.min(), nums.max()
(0, 999999)
>>> nums.mean()
499999.5
```

Let's show the beyond-simplest implementation of mapreduce:

```python
>>> n = nums.map(lambda x: 3 * x)  # multiply all numbers by 3
>>> n
PythonRDD[6] at RDD at PythonRDD.scala:43
>>> n.take(10)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
>>> n.reduce(lambda a, b: a + b)  # sum all numbers
1499998500000
```

Let's filter all primes from the data.

```python
>>> def isprime(x):
...    x = abs(int(x))  # ensure a non-negative integer
...    if x <= 1:
...        return False
...    for i in xrange(2, int(x ** .5) + 1):
...        if x % i == 0:
...            return False
...    return True
...
>>> isprime(17)
True
>>> isprime(18)
False
>>> primes = nums.filter(isprime)
>>> primes.take(10)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> primes.count()
78498
```

Let's get our hands on some real data.


### Data exploration

Let's load the data.  Make sure you already had [copied the data into HDFS](./hadoop.md#download-data) earlier.

```python
>>> movies = sc.textFile('movies.dat')
>>> ratings = sc.textFile('ratings.dat')
```

Spark supports many of the common data operations you may want: `count`, `filter`, `groupBy`, etc. As we saw earlier for MapReduce, Spark supports as well a `map` function, similar to the map function on a Pandas dataframe, performing some function on every row of the dataset, and a `reduce` function to aggregate the values.

```python
>>> movies.take(3)
[u'1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy', u'2::Jumanji (1995)::Adventure|Children|Fantasy', u'3::Grumpier Old Men (1995)::Comedy|Romance']
>>> ratings.take(3)
[u'1::122::5::838985046', u'1::185::5::838983525', u'1::231::5::838983392']
```

The format is

    id::title (year)::tag|tag|tag[|...]  # movies.dat
    user_id::movie_id::rating::timestamp  # ratings.dat


#### Exercises

- How many movies do we have?
- How many ratings do we have?
- How many movies are tagged with Horror?
- How can I keep the movie names with the tags? Find all horror movies with their tags.
- Find all movies that contain horror and comedy

<!-- - How can we count the number of movies per category? -->
<!-- *_HINT:_ You can't ... what's missing?* -->

All answers are in [spark_solutions.md](./spark_solutions.md#data-exploration).


### Keys

How many movies came out each year?  To answer this, we would like something analogous to the usual `GROUPBY` statement.  In spark, this is done by `keyBy` and `reduceByKey`.

    # for a movie 'Toy Story (1995)', key by the year '1995'
    >>> movie_by_year = movies.keyBy(lambda x: x.split('::')[1][-5:-1])
    >>> movie_by_year.take(3)
    [(u'1995', u'1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy'), (u'1995', u'2::Jumanji (1995)::Adventure|Children|Fantasy'), (u'1995', u'3::Grumpier Old Men (1995)::Comedy|Romance')]
    >>> n_movies_by_year = movie_by_year.map(lambda (key, value): (key, 1))
    >>> n_movies_by_year.take(3)
    [(u'1995', 1), (u'1995', 1), (u'1995', 1)]
    >>> n_movies_by_year = n_movies_by_year.reduceByKey(lambda a, b: a + b)
    >>> n_movies_by_year.take(3)
    [(u'1953', 55), (u'1946', 38), (u'1920', 5)]

You could also do the above in one statement by

    >>> movies.map(lambda x: (x.split('::')[1][-5:-1], 1)).reduceByKey(lambda a, b: a + b).take(3)

You might want to sort the output chronologically.

    >>> n_movies_by_year.sortByKey()
    [(u'1915', 1), (u'1916', 2), (u'1917', 2)]

Or you'd like to sort the output by the number of movies each year.  We will swap the key and value for this, and sort descendingly.

    >>> n_movies_by_year.map(lambda x: x[::-1]).sortByKey(False).take(3)
    [(441, u'2002'), (405, u'2000'), (403, u'2001')]

<!--
Fortunately, we also have the good ol' `groupBy` statement.

    >>> groups = movies.groupBy(lambda x: x.split('::')[1][-5:-1])  # group by year
    >>> groups.take(2)
    [(u'1953', <pyspark.resultiterable.ResultIterable object at 0x2a98150>), (u'1946', <pyspark.resultiterable.ResultIterable object at 0x2a98350>)]
    >>> groups.count()

    >>> groups = movies.groupBy(lambda x: x.split('::')[1][-5:-1]).collect()  # group by year
 -->

### Joining

Spark also support a `join` operation, but first we need to key our datasets on something to join on.  We'll key by movie_id.

```python
keyed_ratings = ratings.keyBy(lambda x: x.split("::")[1])
keyed_movies = movie.keyBy(lambda x: x.split('::')[0])
```

Now we can join our datasets.

```python
joined = keyed_movies.join(keyed_ratings)
```

The `joined` of above is again a `PythonRDD` object and was created very quickly.  It only starts computing when we actually try to retrieve information from it.

```python
>>> joined
PythonRDD[225] at RDD at PythonRDD.scala:43
>>> joined.take(3)  # this will take some time
[(u'2712', (u'2712::Eyes Wide Shut (1999)::Drama', u'12::2712::3::959868176')), (u'2712', (u'2712::Eyes Wide Shut (1999)::Drama', u'35::2712::4.5::1133600969')), (u'2712', (u'2712::Eyes Wide Shut (1999)::Drama', u'40::2712::3::945877098'))]
```

Note that joining two keyed datasets return a single keyed dataset where each row is a tuple where the first value is the `key` and the second value is *another* tuple.  In the second tuple the first value is the matched row from dataset 1 and the second is the matched row from dataset 2.  Note that the key appears no less than _three_ times in the row: once in the key place, and twice in the tuple.

    row = (key, (dataset_1_row, dataset_2_row))

In the following exercises, we only care about a small amount of this data: the movie, the user, the category and rating.  So let's create a simpler dataset that just stores that

```python
>>> def createMovieRow(joined_row):
...     """Given a row in the joined dataset, return `(title, [tags], user, rating)`"""
...     movie_row = joined_row[1][0]
...     ratings_row = joined_row[1][1]
...     title, tags = movie_row.split("::")[1:3]
...     tags = tags.split("|")
...     user, _, rating = ratings_row.split("::")[0:3]
...     rating = float(rating)
...     return title, tags, user, rating
...
>>> data = joined.map(createMovieRow)
>>> data.take(3)
[(u'One Fine Day (1996)', [u'Drama', u'Romance'], u'41', 1.0), (u'One Fine Day (1996)', [u'Drama', u'Romance'], u'65', 3.0), (u'One Fine Day (1996)', [u'Drama', u'Romance'], u'182', 3.0)]
```

Note, by the way, that the order of the `take` output is not determined.  Running the same command again might lead to a different output.

```python
>>> data.take(3)
[(u'August Evening (2007)', [u'Drama'], u'16929', 3.5), (u'August Evening (2007)', [u'Drama'], u'51033', 5.0), (u'August Evening (2007)', [u'Drama'], u'67385', 3.5)]
```

Great, you're all set to nail the following exercises!


#### Exercises

- How many reviews per movie do we have?
- How many reviews per movie do we have on average?
- (*) What is the distribution of average ratings per movie?  _Hint_: in the map phase, you should extract movie, rating and count per movies, and in the reduce phase you would sum all ratings and counts, and then finally divide the ratings by the count.  It works best if you map your data in a nested tuple, e.g., `(key, (rating, count))`.

All answers are in [spark_solutions.md](./spark_solutions.md#joining).


### `flatMap`

If we want to know how many reviews per category we have, or what the avarage rating per category is, we might want to use a method called `flatMap`.  This method "flattens" the return lists into a single list.  In our example, we would dissect all tags and create a longer list of all tags, and then reduce by tag to get our desired statistic.

<!--
[(u'One Fine Day (1996)', [u'Drama', u'Romance'], u'41', 1.0), (u'One Fine Day (1996)', [u'Drama', u'Romance'], u'65', 3.0), (u'One Fine Day (1996)', [u'Drama', u'Romance'], u'182', 3.0)]
 -->

```python
>>> tags = data.flatMap(lambda x: x[1])  # list all tags sequentially
>>> tags.take(20)
[u'Drama', u'Drama', u'Drama', u'Drama', u'Drama', u'Drama', u'Drama', u'Drama', u'Crime', u'Drama', u'Musical', u'Crime', u'Drama', u'Musical', u'Crime', u'Drama', u'Musical', u'Crime', u'Drama', u'Musical']
```

Let's count the number of reviews per tag.

```python
>>> counts = tags.map(lambda x: (x, 1))
>>> reviews_per_tag = counts.reduceByKey(lambda a, b: a + b)
>>> reviews_per_tag.take(3)
[(u'Mystery', 630944), (u'Romance', 1901883), (u'Drama', 4344198)]
```

#### Excercise

- Compute the average rating per tag. _Hint:_ keep track of both the summed ratings per tag and the count per tag.  Use nested tuples like before.

All answers are in [spark_solutions.md](./spark_solutions.md#flatmap).


### Sample datasets

Spark on AWS comes with some sample datasets that are stored on S3.  This dataset seems to be a log of IP calls.  Try to read (and reproduce) the following code and understand what each step does.

```python
>>> data = sc.textFile("s3n://elasticmapreduce/samples/pig-apache/input")
>>> data.take(1)
[u'66.249.67.3 - - [20/Jul/2009:20:12:22 -0700] "GET /gallery/main.php?g2_controller=exif.SwitchDetailMode&g2_mode=detailed&g2_return=%2Fgallery%2Fmain.php%3Fg2_itemId%3D15741&g2_returnName=photo HTTP/1.1" 302 5 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"']
>>> data.count()
239344
>>> data.map( lambda x: x.split()[0] ).take(10)  # Get first 10 IP addresses
[u'66.249.67.3', u'66.249.67.3', u'64.233.172.17', u'74.125.74.193', u'192.168.1.198', u'192.168.1.198', u'192.168.1.198', u'66.249.67.3', u'66.249.67.3', u'66.249.67.3']
```

Let's get a count of hits per IP using MapReduce. Note that `collect()` returns all the values, rather than the top so many as `take()` does.

```python
>>> data.map(lambda x: (x.split()[0], 1)).reduceByKey(lambda a, b: a + b).collect()
[(u'59.100.212.98', 7), (u'173.12.69.206', 6), (u'41.202.90.97', 6), ...]

# Alternatively Use the Built-In aggregation functions
>>> ips = data.map(lambda x: x.split()[0])

# Using GroupBy
>>> ips.groupBy(lambda x: x).map(lambda kv: (kv[0], len(kv[1]))).collect()

# Using keyBy and countValuesByKey
>>> ips.keyBy(lambda x: x).countValuesByKey()

# Using countByValue()
>>> ips.countByValue()
```


### Machine Learning

Spark has a common library for machine learning functionality called [mllib](http://spark.apache.org/docs/0.9.0/mllib-guide.html), however the functionality is still sparse.  Additionally, there have been efforts to integrate scikits-learn and Spark [example](https://gist.github.com/MLnick/4707012), [spylearn](https://github.com/ogrisel/spylearn)

Spark has some advantages for machine learning in that it can support multiple passes over a dataset in-memory, a vital operation for machine learning algorithms that require iteration.


