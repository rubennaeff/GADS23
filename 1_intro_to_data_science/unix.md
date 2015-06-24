# Data Science on the Command Line

## Getting the 538 Data

We are going to take a look at election data from the 2012 election. This data is similar to that used by Nate Silver of 538 to predict the winner in the 2012 presidential election.  We will rely on previous election data from (2010 and 2008) to extract some insights that may be useful in this task.

The first datafile is [demographics data](../data/538/census_demographics.csv?dl=0). This file contains demographics information by state, including statistics on income, age and race. The file is comma-separated with a header line in the first line.

The second datafile is [polling data from 2012](../data/538/2012_poll_data_states.csv?dl=0). This file is tab-separated (even though the file says csv) and contains a collections of polls by state with a date and margin.

## Processing the data
First, we may want to get some general idea of what is in the datasets. Here we will use to two basic commands, `cd`, to change directory and `ls` to list the files.

```sh
cd data/538
ls
```

### Previewing the data

Next we may want examine the data and perhaps how much data we have in the census file.  We'll use `less` to get a preview of the files or `cat` to print the whole file. `wc` gets a word count of the file and `wc -l` gets a line count.

```sh
less census_demographics.csv
cat census_demographics.csv
wc census_demographics.csv
wc -l census_demographics.csv
```

This file is comma-separated, so we can use the `cut` command to view individual columns.
```sh
cat census_demographics.csv | cut -d',' -f1,3
```

- The `-d` flag to sort tells how to separate fields
- The `-f` flag tells us which fields to select


### Organizing the data

Now, we can also get some basic information on the top educated states.  College-level education rate is the 6th column and `sort` let's us order the results.

```sh
cat census_demographics.csv  | cut -d',' -f1,6 | sort -t',' -nr -k2
```

- The `-t` flag to sort tells how to separate fields
- The `-k` flag tells us which field to sort on (the 2nd)
- The `-n` flag to sort gives us a numerical ordering
- The `-r` flag gives a reverse ordering


### Aggregating the data

Looking at the poll data, we may want to do some basic aggregation.  Let's find out what states had the most polls.  The 8th field has the state.  `uniq -c` gives us a count of each unique element.  Note, `sort` must always proceed `uniq` as it expects sorted input.

```sh
cat 2012_poll_data_states.csv  | cut -f8 | sort | uniq -c | sort -nrk2
```

Our results look a bit funny - we've got "State" mixed in since it was a header column.  We can skip that row by using `tail` which gives the last n lines.  `tail +n` gives all but first n lines.

```sh
cat 2012_poll_data_states.csv  | cut -f8 | tail +n2 | sort | uniq -c | sort -nrk2
```

### Searching the data

We may want to look at just the September polls, since those were the latest polls in the files.  How many polls were in September.  We can filter using `grep`, a command that let's us search for a string in each line.

```sh
cat 2012_poll_data_states.csv | grep ^9 | wc -l

```

- The `^` character is a special character to search from the start of the line.  Similarly `$` means end of line.


We can also use `grep` to find out how many polls had Obama leading and how many had Romney ahead.

```sh
cat 2012_poll_data_states.csv | grep ^9 | grep "Obama +" | wc -l
cat 2012_poll_data_states.csv | grep ^9 | grep "Romney +" | wc -l
```

Funny enough, this doesn't match the total number of polls in September.  Let's use `grep -v` which returns all lines without the search string to see what the other rows are.

```sh
cat 2012_poll_data_states.csv | grep ^9 | grep -v "Obama +" | grep -v "Romney +"
```

These polls returned are all ties with neither candidate ahead.

### In Class Examples

- How can we extract all polls that were in Ohio?

```sh
# Use grep to search for the OH pattern for Ohio at the end of the line - indicated by '$'
cat 2012_poll_data_states.csv | grep "OH$"
```

- How can we find out which polling company polled most often?

```sh
# Use sort | uniq -c to count up the polls, the sort is necessary as input to uniq
cat 2012_poll_data_states.csv | cut -f4 | sort | uniq -c | sort -n
```

- (**) How many polls were conducted in each month

```sh
# Use tail -n+2 to start from the second line
# Use cut to extract the month - the first thing before  a slash
# Use sort | uniq -c to count up the polls, the sort is necessary as input to uniq
cat 2012_poll_data_states.csv | tail -n+2 | cut -d'/' -f1 | sort | uniq -c | sort -n
```

- (**) In how many polls does Obama have a double digit lead

```sh
# Use cut to filter to the 'Spread' field
# Use grep to find the polls where Obama leads
# Use grep to filter to polls that are +<any digit 1-9><any digit 0-9>
cat 2012_poll_data_states.csv | cut -f7| grep "Obama +" | grep "+[1-9][0-9]"
```

### Additional review question
1. How many reviews are there?
1. What is the distribution of review scores? In other words, how many 1's, 2's, 3's, 4's, 5's
1. How many unique users are there? (Remember uniq -c gives a count per user, uniq gives the same list without the count)

### Additional Resources
#### Unix Command Line
- [Video Tutorials for Command Line Basics](http://drupalize.me/series/command-line-basics-series)
- [Command Line Data Manipulation](http://planspace.org/2013/05/21/command-line-data-manipulation/)
- [Useful Unix Commands for Data Science](http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/)
