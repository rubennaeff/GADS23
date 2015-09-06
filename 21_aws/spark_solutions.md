# Apache Spark

### Solutions to exerices

```python
>>> movies = sc.textFile('movies.dat')
>>> ratings = sc.textFile('ratings.dat')
>>> movies.take(3)
[u'1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy', u'2::Jumanji (1995)::Adventure|Children|Fantasy', u'3::Grumpier Old Men (1995)::Comedy|Romance']
>>> ratings.take(3)
[u'1::122::5::838985046', u'1::185::5::838983525', u'1::231::5::838983392']
```

### Data Exploration

- How many movies do we have?

```python
>>> movies.count()
10681
```

- How many ratings do we have?

```python
>>> ratings.count()
10000054
```

- How many movies are tagged with Horror?

```python
>>> tags = movies.map(lambda x: x.split("::")[-1])
>>> tags.filter(lambda tag: 'Horror' in tag).count()
1013
```

- How can I keep the movie names with the tags? Find all horror movies with their tags.

```python
>>> tags = movies.map(lambda x: x.split("::")[1:3])
>>> tags.filter(lambda (movie, tag): 'Horror' in tag).take(3)
[[u'Dracula: Dead and Loving It (1995)', u'Comedy|Horror'], [u'Copycat (1995)', u'Crime|Drama|Horror|Mystery|Thriller'], [u'Seven (a.k.a. Se7en) (1995)', u'Crime|Horror|Mystery|Thriller']]

# alternatively, you could have done
>>> tags = movies.map(lambda x: (x.split("::")[1], x.split("::")[-1]))  # less efficient
```

- Find all movies that contain horror and comedy

```python
>>> tag = movies.map(lambda x: x.split("::")[1:3])
>>> favs = tag.filter(lambda (movie, tag): 'Horror' in tag and 'Comedy' in tag)
>>> favs.take(3)
[[u'Dracula: Dead and Loving It (1995)', u'Comedy|Horror'], [u'From Dusk Till Dawn (1996)', u'Action|Comedy|Horror|Thriller'], [u'Mute Witness (1994)', u'Comedy|Horror|Thriller']]
# Let's print without the tags
>>> favs.map(lambda (movie, tag): movie).take(3)
```


### Joining

- How many reviews per movie do we have?

```python
>>> data.map(lambda x: (x[0], 1)).reduceByKey(lambda a, b: a + b).take(3)
[(u'Hot to Trot (1988)', 89), (u'Free Radicals (B\xf6se Zellen) (2003)', 6), (u'Soul Assassin (2001)', 8)]
```

- How many reviews per movie do we have on average?

```python
>>> data.map(lambda x: (x[0], 1)).reduceByKey(lambda a, b: a + b).map(lambda x: x[1]).mean()
936.68546272011986
```

- (*) What is the distribution of average ratings per movie?  _Hint_: in the map phase, you should extract movie, rating and count per movies, and in the reduce phase you would sum all ratings and counts, and then finally divide the ratings by the count.  It works best if you map your data in a nested tuple, e.g., `(key, (rating, count))`.

```python
>>> d = data.map(lambda x: (x[0], (x[3], 1)))
>>> d.take(3)
[(u'Leatherheads (2008)', (3.5, 1)), (u'Leatherheads (2008)', (4.0, 1)), (u'Leatherheads (2008)', (3.0, 1))]

>>> e = d.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
>>> e.take(3)
[(u'AKA (2002)', (48.5, 14)), (u'Destination Tokyo (1943)', (158.5, 45)), (u'Stanley & Iris (1990)', (771.5, 249))]

>>> f = e.map(lambda x: (x[0], x[1][0] / x[1][1]))
[(u'Irma la Douce (1963)', 3.5860655737704916), (u'Monsieur Hire (1989)', 3.795774647887324), (u'Operation Homecoming: Writing the Wartime Experience (2007)', 3.625)]
```

### `flatMap`

- Compute the average rating per tag. _Hint:_ keep track of both the summed ratings per tag and the count per tag.  Use nested tuples like before.

```python
>>> tag_ratings = data.flatMap(lambda x: [(tag, (x[3], 1)) for tag in x[1]])
>>> tag_ratings.take(3)
[(u'Action', (3.5, 1)), (u'Adventure', (3.5, 1)), (u'Drama', (3.5, 1))]
>>> sums = tag_ratings.reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))
>>> avg_tag_rating = sums.map(lambda x: (x[0], x[1][0] / x[1][1]))
>>> avg_tag_rating.take(3)
[(u'Action', 3.4213307400955033), (u'Romance', 3.5537764415581821), (u'Mystery', 3.6776306613582186)]

# You might want to order the tags by avg rating, showing the top 10 categories
>>> avg_tag_rating.map(lambda x: x[::-1]).sortByKey(False).take(10)
[(4.0121511946014952, u'Film-Noir'), (3.7834593152512226, u'Documentary'), (3.7801731498090883, u'War'), (3.7645374449339206, u'IMAX'), (3.6776306613582186, u'Mystery'), (3.6732628208935227, u'Drama'), (3.6656546597629625, u'Crime'), (3.6428571428571428, u'(no genres listed)'), (3.5999880565273004, u'Animation'), (3.5624784381533501, u'Musical')]
```
