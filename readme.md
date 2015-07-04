# GA Data Science NYC #23

**Team**
- [Daniel Demoray](mailto:ddemoray@ga.co), producer
- [Ruben Naeff](mailto:rubennaeff@gmail.com), instructor
- [Antoine Grant](mailto:antoinejgrant@gmail.com), expert in residence
- [egroup](mailto:dat-nyc-23@ga-groups.com) & [Slack channel](https://ganyceveningcourses.slack.com/messages/data-science-23/), everyone

Please do not hesitate to contact any of us!

**Logisitics**
- June 25 - September 10, 2015
- Tuesdays and Thursdays 6.30-9.30
- GA West, 10 East 21st St, room 4A (4th floor)
- Office hours: TBD

**Please fill out an
[exit ticket](https://docs.google.com/forms/d/1-3HioTz5qPSaqvDvUw1xXSQjGsgD9OVMtVaVWhPjgcg/viewform)
after each class**


## Copying the course notes to your machine

To clone the repo, type
```sh
git clone http://github.com/ga-students/DAT-23-NYC
```

To update the repo, so you have the latest course notes on your computer
```sh
git pull
```

Note that the above statement can give an error if you had changed any of the files yourself.
Please **make a copy** of the files you edited (e..g, using `cp`) and then type the following commands.
If you did not copy your changes, they will be **overwritten** and your changes will be lost.

```sh
git reset --hard HEAD
git pull
```

## Syllabus (tentative)

|  # | Date       | Topic                                               |
|---:|:-----------|:----------------------------------------------------|
|    |            | **I. Data Exploration (Analytics)**                 |
|  1 | Thu Jun 25 | Introduction to data science, Unix                  |
|  2 | Tue Jun 30 | Databases, SQL, Python                              |
|  3 | Thu Jul 02 | Python, pandas                                      |
|  4 | Tue Jul 07 | Presenting, visualizations, web scraping, APIs      |
|    |            | _Assignment #1: Data exploration_                   |
|    |            | **II. Modeling and Predicting**                     |
|  6 | Thu Jul 09 | Intro to Machine Learning, kNN                      |
|  5 | Tue Jul 14 | Linear Algebra                                      |
|  7 | Thu Jul 16 | Linear Regression                                   |
|    |            | _Assignment #2: regression_                         |
|  8 | Tue Jul 21 | Logistic Regression and Regularization              |
|  9 | Thu Jul 23 | Bayesian Statistics and Naive Bayes                 |
| 10 | Tue Jul 28 | Decision Trees and Random Forests                   |
| 11 | Thu Jul 30 | Review: regression and classification (competition) |
|    |            | _Assignment #3: regression and classification_      |
|    |            | _Deadline project proposals_                        |
| 12 | Tue Aug 04 | Ensemble Learning                                   |
| 13 | Thu Aug 06 | K-Means Clustering                                  |
| 14 | Tue Aug 11 | PCA and Unsupervised Learning                       |
| 15 | Thu Aug 13 | Recommendation Systems                              |
|    |            | Presentations data explorations for projects        |
|    |            | **III. Various**                                    |
| 16 | Tue Aug 18 | Further Topics in Unsupervised Learning             |
| 17 | Thu Aug 20 | Scaling: Hadoop, Spark                              |
| 18 | Tue Aug 25 | _TBD: guest speakers, ethics, requests, etc._       |
| 19 | Thu Aug 27 | _TBD_                                               |
| 20 | Tue Sep 01 | _TBD_                                               |
| 21 | Thu Sep 03 | _TBD_                                               |
| 22 | Tue Sep 08 | _TBD_                                               |
| 23 | Thu Sep 10 | Final presentations                                 |

Additional topics may include hasing, Bloom filters, HyperLogLog, Item Response Theory, graph theory, A/B testing, ethics, etc. We'll invite guest speakers to come present in class. Let me know if there is a company you're particularly interested in.


## Resources

- [All datasets](./data)

**I. Data Exploration (Analytics)**

- [01: INTRODUCTION TO DATA SCIENCE](./1_intro_to_data_science)
  - [Slides](./1_intro_to_data_science/gads23_01_intro.pdf)
  - [Setting Up Your Environment](./1_intro_to_data_science/setup.md)
  - [Data Science at the Command Line](./1_intro_to_data_science/unix.md)

- [02: DATABASES, SQL, PYTHON](./2_sql_python)
  - [Slides](./2_sql_python/gads23_02_sql_python.pdf)
  - [SQL Exercises](./2_sql_python/databases.md)
  - [Python Exercises](./2_sql_python/intro_to_python.ipynb)
  - [Data Exploration in Python](./2_sql_python/data_exploration_in_python.ipynb)

- [03: PYTHON, PANDAS](./3_pandas)
  - [Slides](./3_pandas/gads23_03.pdf)
  - [Pandas Exercises](./3_pandas/intro_to_pandas.ipynb)

- [04: DATA EXPLORATION](./4_presenting)
  - How To Present Your Insights
  - [Visualizations](./4_presenting/visualizations.ipynb)
  - [Web scraping](./4_presenting/web_scraping.ipynb)
  - APIs
  - **[Assignment #1: Data exploration](./4_presenting/assignment_01.md)**

<!-- **II. Modeling and Predicting** -->
