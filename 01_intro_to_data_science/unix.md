# Data Science on the Command Line

## Getting the 538 Data

We are going to take a look at election data from the 2012 election. This data is similar to that used by Nate Silver of 538 to predict the winner in the 2012 presidential election.  We will rely on previous election data from (2010 and 2008) to extract some insights that may be useful in this task.

The first datafile is [demographics data](../data/538/census_demographics.csv?dl=0). This file contains demographics information by state, including statistics on income, age and race. The file is comma-separated with a header line in the first line.

The second datafile is [polling data from 2012](../data/538/2012_poll_data_states.csv?dl=0). This file is tab-separated (even though the file says csv) and contains a collections of polls by state with a date and margin.

## Processing the data
First, if you haven't done so already, make sure you have [cloned the course](./setup.md#github) repo to your machine.

Now, we may want to get some general idea of what is in the datasets. Here we will use to two basic commands, `cd`, to change directory and `ls` to list the files. Note that in unix, your home directory can be abbreviated by a tilde (`~`).

```sh
cd ~/repo/DAT-23-NYC
ls
cd data/538
ls
```

The command `ls` only displays the names of the files in the current directory. You may want to use the options `-l` or `-lh` to obtain additional information, such as permissions, owners, filesize, timestamp of last modification.

- The `-l` flag displays a list in long format
- The `-lh` flag does the same, but rounds the filesize to kB, MB, GB, etc.


## Panicking and Getting help

You can always request help with the `man` command:

```sh
man cd
man ls
```

Whenever you feel your screen is getting cluttered, you can use the command `clear` to clear your screen. Also note that you can always view the current directory in Finder (Mac only) by typing `open .`.

If you found yourself stuck printing your seven terrabyte dataset onto your screen (which _will_ happen), just hit `^C` (control-C) to terminate the program.


### Previewing the data

Next we may want examine the data and perhaps how much data we have in the census file.  We use `cat` to print the whole file.

```sh
cat census_demographics.csv
```

Printing an entire file onto the screen may be counterproductive.  `head` and `tail` prints the top resp. bottom ten lines of a file.  You can use the flag `-3` to limit the output to three lines.  `-1` will only display the column header, for example.  You can use `wc` to get a word count of the file and `wc -l` to get a line count.  To save yourself typing, you can use the up and down arrows to navigate through past commands.

```sh
head census_demographics.csv
head -1 census_demographics.csv
tail census_demographics.csv
wc census_demographics.csv
wc -l census_demographics.csv
```

We'll use `less` to get a preview of the files.

```sh
less census_demographics.csv
```

When using `less`, the following commands might be useful
- Press `Enter` to display next line
- Press `Space` to display next screen
- Press `?` to search for a pattern (case sensitive)
- Press `q` to quit

You can use the pipe (`|`) to use the output of one program as the input of another program.

```sh
cat census_demographics.csv | head -2
cat census_demographics.csv | less
cat census_demographics.csv | wc
cat census_demographics.csv | wc -l
```

We see that the file `census_demographics.csv` is comma-separated, so we can use the `cut` command to view individual columns.

```sh
cat census_demographics.csv | cut -d',' -f1,3
```

- The `-d` flag to sort tells how to separate fields (columns)
- The `-f` flag tells us which fields to select


On a sidenote, unix has a feature called tab-completion. This enables us to refer to commands and files by typing just a first few characters and hitting `tab`. If there are multiple options, just hit `tab` twice.  A list with all suitable options appears.

```sh
cat cen\[tab\]
ca\[tab\]\[tab\]
```



### Organizing the data

Now, we can also get some basic information on the top educated states.  College-level education rate is the 6th column and `sort` lets us order the results.  We use `head` to only show the top 10.

```sh
cat census_demographics.csv  | cut -d',' -f1,6 | sort -t',' -k2 -nr
cat census_demographics.csv  | cut -d',' -f1,6 | sort -t',' -k2 -nr | head
```

- The `-t` flag to sort tells how to separate fields
- The `-k` flag tells us which field to sort on (the 2nd)
- The `-n` flag to sort gives us a numerical ordering
- The `-r` flag gives a reverse ordering


### Aggregating the data

Let's have a look at the poll data, which is in `2012_poll_data_states.csv`.  (Note that you can copy-paste all three lines at once into your terminal screen to execute them all in succession.)

```sh
clear
cat 2012_poll_data_states.csv | head -5
cat 2012_poll_data_states.csv | wc -l
```

Looking at the poll data, we may want to do some basic aggregation.  Let's find out what states had the most polls.  The 8th field has the state.  `uniq -c` gives us a count of each unique element.  Note, `sort` must always proceed `uniq` as it expects sorted input.  Duplicates that do not immediately succeed each other will be counted double.

```sh
cat 2012_poll_data_states.csv  | cut -f8 | sort | uniq -c | sort -nrk2
```

Our results look a bit funny: we've got "State" mixed in since it was a header column.  We can skip that row by using `tail -n` which gives the last `n` lines.  `tail +n` gives all tail starting at the `n`-th line.

```sh
cat 2012_poll_data_states.csv  | cut -f8 | tail +2 | sort | uniq -c | sort -nrk2
```

### Searching the data

We may want to look at just the September polls, since those were the latest polls in the files.  How many polls were in September?  We can filter using `grep`, a command that lets us search for a string in each line.

```sh
cat 2012_poll_data_states.csv | grep ^9 | wc -l
```

- The `^` character is a special character to search from the start of the line.
- Similarly, `$` means end of line.

How many polls were in the state of Michigan?

```sh
cat 2012_poll_data_states.csv | grep MI$ | wc -l
```

We can also use `grep` to find out how many polls had Obama leading and how many had Romney ahead.

```sh
cat 2012_poll_data_states.csv | grep ^9 | grep "Obama +" | wc -l
cat 2012_poll_data_states.csv | grep ^9 | grep "Romney +" | wc -l
```

Funny enough, this doesn't match the total number of polls in September.  Let's use `grep -v` which returns all lines that do **not** match the search string to see what the other rows are.

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

### Additional questions

Let's have a look at the movie reviews from Amazon, which can be found in `data/amazon/small-movies.txt`.

1. How many movie reviews are there?
1. What is the distribution of review scores? In other words, how many 1's, 2's, 3's, 4's and 5's?
1. How many unique users are there? (Remember uniq -c gives a count per user, uniq gives the same list without the count)

In practice, you'll have to deal with very large and ugly datasets. Let's look at NYC's 311 complaints in NYC in `data/311`.

1. How many columns does this file have? (Hint: use `grep -o`)
1. Use `tr` to count the number of columns. (Hint: use `tr ',' '\n'` to translate commas into newlines)
1. Are the two answers the same?
1. What are the top 5 complaint types?
1. How many days of complaints are registered?
1. How many complaints for each day do you see?


### Additional Resources
#### Unix Command Line
- [Video Tutorials for Command Line Basics](http://drupalize.me/series/command-line-basics-series)
- [Command Line Data Manipulation](http://planspace.org/2013/05/21/command-line-data-manipulation/)
- [Useful Unix Commands for Data Science](http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/)
