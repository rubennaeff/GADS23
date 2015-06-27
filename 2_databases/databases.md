# Databases

## SQL Operators

### SELECT 

Every query should start with `SELECT`.  `SELECT` is followed by the names of the columns in the ouput.

`SELECT` is always paired with `FROM`, and `FROM` identifies the table to retrieve data from.

```sql
SELECT
<columns>
FROM
<table>
```

`SELECT *` denotes returns *all* of the columns.

### WHERE 
`WHERE` is used to filter table to a specific criteria and follows the `FROM` clause.

```sql
SELECT
<columns>
FROM
<table>
WHERE
<condition>
```

The condition is some filter applied to the rows, where rows that match the condition will be in the output

From the UNIX examples:

- What polls were taken in Ohio?

```sql
SELECT
*
FROM
polls_table
WHERE
State == 'OH'

```

### GROUP BY

`GROUP BY` allows us to aggregate over any field in the table. We identify some key with which want to segment the rows. Then, we roll-up or compute some statistic over all of the rows that match that key.

`GROUP BY` *must be* paired with an aggregate function - the statistic we want to compute in the rows - in the `SELECT` statement.

- How many polls where taken in each state?
```sql
SELECT
State, COUNT(*)
FROM
polls_table
GROUP BY
State;
```

`COUNT(*)` denotes counting up all of the rows.  Other aggregate functions commonly available are `AVG` - average, `MAX`, `MIN`, and `SUM`.

If we want an aggregate over the entire table - without results specific to any key, we can use an aggregate function in the `SELECT` statement and ignore the `GROUP BY` clause.

- In how many polls does Obama have a double digit lead?

```sql
SELECT
COUNT(*)
FROM
polls_table
WHERE Winner = 'Obama' and Spread >= 10;
```

### ORDER BY
Results of a query can be sorted by `ORDER BY`.

If we want to order the states by the number of polls, we would add an `ORDER BY` clause at the end. 

- In how many polls did Obama have a double digit lead
```
```sql
SELECT
State, COUNT(*) as cnt
FROM
polls_table
GROUP BY State
ORDER BY cnt
```

`COUNT(*) as cnt` renames the `COUNT(*)` value as `cnt` so we can refer to it later in the `ORDER BY` clause.


### JOIN
`JOIN` allows us to access data across many tables. We will need to specify how a row in one table links to a row in another.  For example, to `JOIN` the polling data with the demographic data from the the 538model - we will need to specify how a row in the polling table should match a row in the demographic data. The most sensible choice is by state - we want to link each poll to the demographics of the state.

```sql
SELECT polls_table.Date, polls_table.Spread, polls_table.State, demographics.*
FROM polls_table
JOIN demographics
ON (polls_table.State = demographics.State)
```

Here `ON` denotes

#### Inner Join
By default, most joins are an *Inner Join*, which means only when there is a match in both tables, does a row appear in the result. For example above, that means there is only an ouput row *if*
- There was a poll in the state
- *AND* we have the demographic data from that state.

If there is no a demographic data for a state, the poll be dropped, and similarly if there is no poll in that state the demographic data will be dropped.

#### Outer Join
If we want to keep the rows of one table *even if there is no matching counterpart* we can perform an *Outer Join*. Outer joins can be `LEFT`, `RIGHT`, or `FULL` meaning keep all the left rows, all the right rows or *all* the rows, respectively.

The following query will keep all of the rows even if there no demographic data exists.

```sql
SELECT polls_table.Date, polls_table.Spread, polls_table.State, demographics.*
FROM polls_table
LEFT JOIN demographics
ON (polls_table.State = demographics.State)
```

## Exercises

To get some practice with SQL, we'll use the some of the sample exercises available at [http://pgexercises.com](http://pgexercises.com) and [W3 School](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all).

### W3 School

Additional exercises are available through another online portal, the [W3 School](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

Below are some sample questions with solutions as well as some additional practice problems.

#### Sample Questions

Let's walk through a few examples:

1) Retrieve all Customers from Madrid

```sql
SELECT * FROM Customers WHERE City='Madrid'
```

2) What is the most common city for customers?

```sql
SELECT City, COUNT(*) as cnt FROM Customers GROUP BY City ORDER BY cnt desc;
```

3) What category has the most products?

```sql
SELECT CategoryName, COUNT(*) FROM Categories JOIN Products on (Categories.CategoryID = Products.CategoryID) GROUP BY CategoryName;
```

#### Exercises:

1. What customers are from the UK
2. What is the name of the customer who has the most orders?
3. What supplier has the highest average product price?
4. What category has the most orders?

5. (*) What employee made the most sales (by number of sales)?

6. (**) What employee made the most sales (by value of sales)?

7. (**) What Employees have BS degrees? (Hint: Look at LIKE operator)

8. (**) What supplier has the highest average product price *assuming they have at least 2 products* (Hint: Look at the HAVING operator)

### PGExercises

For more practice there are sample exercises available at [http://pgexercises.com](http://pgexercises.com)

Here we'll examine the toy dataset created for a country club and it's operations. As the Getting Started page states:

"The dataset for these exercises is for a newly created country club, with a set of members, facilities such as tennis courts, and booking history for those facilities. Amongst other things, the club wants to understand how they can use their information to analyse facility usage/demand."

