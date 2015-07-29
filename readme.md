# GA Data Science NYC #23

**Team**
- [Daniel Demoray](mailto:ddemoray@ga.co), producer
- [Ruben Naeff](mailto:rubennaeff@gmail.com), instructor
- [Antoine Grant](mailto:antoinejgrant@gmail.com), expert in residence
- [egroup](mailto:dat-nyc-23@ga-groups.com) & [Slack channel](https://ganyceveningcourses.slack.com/messages/data-science-23/), [Google Drive folder](https://drive.google.com/drive/folders/0B4Z0Mpa9wB9rfm5PQWhXRUVZRnQzTFY5a1I0d0hsZnZ4MnkxVWV0Q1psbUdBX2RUMVBsZ3M), everyone

Please do not hesitate to contact any of us!

**Logisitics**
- June 25 - September 10, 2015
- Tuesdays and Thursdays 6.30-9.30
- GA West, 10 East 21st St, room 4A (4th floor)
- Office hours: TBD

**Please fill out an
[exit ticket](https://docs.google.com/forms/d/1-3HioTz5qPSaqvDvUw1xXSQjGsgD9OVMtVaVWhPjgcg/viewform)
after each class**


You can use `git` to painlessly copy and update the course notes to your machine. Please see the section [Cloning the repo](./01_intro_to_data_science/setup.md#cloning-the-repo).


## Syllabus (tentative)

|  # | Date       | Topic                                                                  |
|---:|:-----------|:-----------------------------------------------------------------------|
|    |            | **I. Data Exploration (Analytics)**                                    |
|  1 | Thu Jun 25 | Introduction to data science, Unix                                     |
|  2 | Tue Jun 30 | Databases, SQL, Python                                                 |
|  3 | Thu Jul 02 | Python, pandas                                                         |
|  4 | Tue Jul 07 | Presenting, visualizations, web scraping, APIs
_Assignment #1: Data exploration_ |
|    |            |
|    |            | **II. Supervised Learning: Regression**                                |
|  6 | Thu Jul 09 | Introduction to Machine Learning, kNN                                  |
|  5 | Tue Jul 14 | Presentations + Linear Regression                                      |
|  7 | Thu Jul 16 | Regression & Regularization, linear algebra, numpy _(AG OOO)_          |
|  8 | Tue Jul 21 | Regression & Text Processing                                           |
|    |            | _Assignment #2: regression_                                            |
|    |            | **III. Supervised Learning: Classification**                           |
|  9 | Thu Jul 23 | Logistic Regression _(AG OOO)_                                         |
| 10 | Tue Jul 28 | Review Assignment #2. _Guest Rohit Acharya, First Access_              |
| 11 | Thu Jul 30 | Bayesian Statistics & Naive Bayes.                                     |
|    |            | _Deadline project proposals_                                           |
| 12 | Tue Aug 04 | Decision Trees and Random Forests                                      |
| 13 | Thu Aug 06 | SVM / Ensemble Learning _Guest Sandy Griffith, Flatiron Health_   |
|    |            | _Assignment #3: classification_                                        |
|    |            | **IV. Unsupervised Learning**                                          |
| 14 | Tue Aug 11 | Review & competition. _Guest Bob Filbin, Crisis Text Line_  |
| 15 | Thu Aug 13 | K-Means Clustering.  |
|    |            | Presentations data explorations for projects                           |
| 16 | Tue Aug 18 | PCA and Unsupervised Learning  |
| 17 | Thu Aug 20 | Recommendation Systems & Further Topics in Unsupervised Learning |
|    |            | **V. Various**                                                         |
| 18 | Tue Aug 25 | Scaling                                                                |
| 19 | Thu Aug 27 | _TBD_ _(RN OOO)_                                                       |
| 20 | Tue Sep 01 | _TBD_                                                                  |
| 21 | Thu Sep 03 | _TBD_                                                                  |
| 22 | Tue Sep 08 | _TBD_                                                                  |
| 23 | Thu Sep 10 | Final presentations                                                    |
_OOO = Out of Office_

- Additional topics may include: neural nets, AWS, scaling, hadoop, spark, vowpal wabbit, hasing, Bloom filters, HyperLogLog, Item Response Theory, graph theory, A/B testing, ethics, etc.
- We'll invite guest speakers to come present in class. Let me know if there is a company you're particularly interested in.


## Resources

- [All datasets](./data/)
- [Extraneous](./extraneous.md) (all irrelevant things we discussed)


**I. Data Exploration (Analytics)**

- [01: INTRODUCTION TO DATA SCIENCE](./01_intro_to_data_science/)
  - [Slides](./01_intro_to_data_science/gads23_01_intro.pdf)
  - [Setting Up Your Environment](./01_intro_to_data_science/setup.md)
  - [Data Science at the Command Line](./01_intro_to_data_science/unix.md) including exercises

- [02: DATABASES, SQL, PYTHON](./02_sql_python/)
  - [Slides](./02_sql_python/gads23_02_sql_python.pdf)
  - [SQL Exercises](./02_sql_python/databases.md)
  - [Python Exercises](./02_sql_python/intro_to_python.ipynb)
  - [Data Exploration in Python](./02_sql_python/data_exploration_in_python.ipynb) including exercises

- [03: PYTHON, PANDAS](./03_pandas/)
  - [Slides](./03_pandas/gads23_03.pdf)
  - [Pandas Exercises](./03_pandas/intro_to_pandas.ipynb)

- [04: VISUALIZATIONS AND MORE DATA GATHERING](./04_presenting/)
  - [Slides](./04_presenting/gads23_04.pdf)
  - [Web scraping](./04_presenting/web_scraping.ipynb) _optional demo_
  - [Twitter API](./04_presenting/twitter_stream.py) _optional demo_
  - How To Present Your Insights
  - [Visualizations](./04_presenting/visualizations.ipynb) including exercises
  - [Anscombe's Quartet](./04_presenting/anscombe_quartet.ipynb) illustrating the need for visualizations
  - **[Assignment #1: Data Exploration](./04_presenting/assignment_01.md)**

**II. Supervised Learning**

- [05: INTRODUCTION TO MACHINE LEARNING](./05_intro_to_ml/)
  - [Slides](./05_intro_to_ml/gads23_05_intro_to_ml.pdf)
  - [kNN Classification](./05_intro_to_ml/k_nearest_neighbors.ipynb) Iris dataset
  - [kNN implementation](./05_intro_to_ml/knn.py) _optional_ exercise

_Regression models_

- [06: LINEAR REGRESSION](./06_linear_regression/)
  - [Slides](./06_linear_regression/gads23_06_linear_regression.pdf)
  - [Introduction to numpy](./06_linear_regression/intro_to_numpy.ipynb) _optional_
  - [Linear Algebra recap](./06_linear_regression/linear_algebra.ipynb) _optional_
  - [Linear Regression](./06_linear_regression/linear_regression.ipynb) `statsmodels`, `patsy`, `seaborn`; salaries, house prices
  - [3D plot in Python](./06_linear_regression/3d_plot.ipynb) _example as reference_

- [07: POLYNOMIAL REGRESSION & REGULARIZATION](./07_regularization/)
  - [Slides](./07_regularization/gads23_07.pdf)
  - [Regularization](./07_regularization/regularization.ipynb) polynomials, `makepipeline`, Ridge, Lasso

- [08: REGRESSION & TEXT PROCESSING](./08_regression_final/)
  - [One slide](./08_regression_final/gads23_08_regression_final.pdf)
  - [Text Processing](./08_regression_final/text_processing.ipynb) Amazon movie reviews, `CountVectorizer` (demo)
  - **[Assignment #2: Linear Regression](./08_regression_final/assignment_02_salary_prediction.ipynb) Salary Prediction**

_Classification models_

- [09: LOGISTIC REGRESSION](./09_logistic_regression/)
  - [Slides](./09_logistic_regression/gads23_09_logistic_regression.pdf)
  - [Logistic Regression](./09_logistic_regression/logistic_regression.ipynb) Iris dataset, precision/recall, decision boundaries; exercises
  - [Insult Classification](./09_logistic_regression/insult_classification.ipynb) exercise
  - [Area Under the ROC Curve](./09_logistic_regression/roc_curve.ipynb) _optional_ deep dive
  - [Non-linear decision boundaries](./09_logistic_regression/non_linear_decision_boundaries.ipynb) _optional_

- [10: REVIEW](./10_review/)
  - [Slides](./10_review/gads23_10_exit_tickets_review.pdf) Exit tickets review
  - [Review Assignment #2](./08_regression_final/assignment_02_salary_prediction_solutions.ipynb) and [Leaderboard](./08_regression_final/assignment_02_salary_prediction_submissions.ipynb)
  - [Rohit Acharya, Chief Data Scientist at First Access](./guest_speakers.md), guest speaker
  - [Final project announcement](./10_review/gads23_10_bayes.pdf) guidelines, deadlines, sample projects

- [11: STATISTICS & BAYES](./11_bayes/)
  - [Slides](./11_bayes/gads23_10_bayes.pdf)
  - [20 Newsgroups](./11_bayes/20_newsgroups.ipynb) `CountVectorizer`, `TfidfVectorizer`, `MultinomialNB` (demo)
  - [Naive Bayes implementation](./11_bayes/naive_bayes_exercise.py) exercise
  - [Statistics & Probability recap](./11_bayes/statistics_recap.ipynb) _optional_ basic recap
  - [Bayesian coin flips](./11_bayes/bayesian_coin_tosses.ipynb) deep dive _optional_


<!--   - [Slides](./10_statistics/gads23_08.pdf)
  - Statstictis & Probability
  - Bayes Theorem
  - Bayes and regression
  - Naive Bayes
 -->


<!-- - [11: DECISION TREES](./11_decision_trees/)
  - [Slides](./11_decision_trees/gads23_09.pdf)
 -->

<!-- - [13: COMPETITION](--some kaggle competition in class w/pizza and beer!--)
 -->

<!-- **III. Unsupervised Learning** -->

