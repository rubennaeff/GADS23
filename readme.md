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

Please see [Cloning the repo](./01_intro_to_data_science/setup.md#cloning-the-repo) for how to download the latest course notes to your laptop.


## Resources

- [Calendar](./calendar.md)
- [Final Project](./final_project.md)
- [Guest speakers](./guest_speakers.md)
- [All datasets](./data/)
- [Further Reading](./further_reading.md) to continue your studies
- [Extraneous](./extraneous.md) to make your life more pleasant


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
  - Presentations Assignment #1
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
  - _[Guest Speaker](./guest_speakers.md): Amy Roberts, CEO & Founder of Healthy Bytes_
  - **[Assignment #2: Linear Regression](./08_regression_final/assignment_02_salary_prediction.ipynb) Salary Prediction**


**III. Supervised Learning: Classification**

- [09: LOGISTIC REGRESSION](./09_logistic_regression/)
  - [Slides](./09_logistic_regression/gads23_09_logistic_regression.pdf)
  - [Logistic Regression](./09_logistic_regression/logistic_regression.ipynb) Iris dataset, precision/recall, decision boundaries; exercises
  - [Insult Classification](./09_logistic_regression/insult_classification.ipynb) exercise
  - [Area Under the ROC Curve](./09_logistic_regression/roc_curve.ipynb) _optional_ deep dive
  - [Non-linear decision boundaries](./09_logistic_regression/non_linear_decision_boundaries.ipynb) _optional_

- [10: REVIEW](./10_review/)
  - [Slides](./10_review/gads23_10_exit_tickets_review.pdf) Exit tickets review
  - [Review Assignment #2](./08_regression_final/assignment_02_salary_prediction_solutions.ipynb) and [leaderboard](./08_regression_final/assignment_02_salary_prediction_submissions.ipynb)
  - [Final project announcement](./final_project.md) guidelines, deadlines, sample projects
  - _[Guest Speaker](./guest_speakers.md): Rohit Acharya, Chief Data Scientist at First Access_

- [11: STATISTICS & BAYES](./11_bayes/)
  - [Slides](./11_bayes/gads23_11_bayes.pdf)
  - [20 Newsgroups](./11_bayes/20_newsgroups.ipynb) `CountVectorizer`, `TfidfVectorizer`, `MultinomialNB` (demo)
  - [Naive Bayes implementation](./11_bayes/naive_bayes_exercise.py) exercise
  - [Statistics & Probability recap](./11_bayes/statistics_recap.ipynb) _optional_ basic recap
  - [Bayesian coin flips](./11_bayes/bayesian_coin_tosses.ipynb) _optional_ deep dive

- [12: ENSEMBLE LEARNING & RANDOM FORESTS](./12_random_forest/)
  - [Slides](./12_random_forest/gads23_12_random_forests.pdf)
  - [Random Forests in `sklearn`](./12_random_forest/random_forests_in_sklearn.ipynb) `DecisionTree`, `RandomForestClassifier`, `AdaBoostClassifier`, `GradientBoostingClassifier`
  - [Drawing trees in `sklearn`](./12_random_forest/drawing_trees_in_sklearn.ipynb) _optional_ `Graphviz`, `pydot`
  - [Plotting decision boundaries](./12_random_forest/plotting_decision_boundaries.ipynb) _optional_ `ExtraTreesClassifier`, `AdaBoost`
  - [Random Forests implementation](./12_random_forest/random_forest.py) with [notebook demonstration](./12_random_forest/random_forest_deep_dive.ipynb) _optional_ deep dive

- [13: SUPPORT VECTOR MACHINES](./13_svm/)
  - [Slides](./13_svm/gads23_13_svm.pdf)
  - [Recognizing hand-written digits](./13_svm/digit_recognition.ipynb) demo
  - [Plotting hyperplanes and support vectors](./13_svm/plotting_hyperplanes_and_support_vectors.ipynb) demo
  - [Plotting different SVM kernels](./13_svm/plotting_different_svm_kernels.ipynb) _optional_ demo of non-linear kernels
  - [Separating mushrooms](./13_svm/separating_mushrooms.ipynb) exercise
  - _[Guest Speaker](./guest_speakers.md): Sandy Griffith, Biostatistician and Technical Lead at Flatiron Health_
  - [Flask demonstration](./13_svm/flask/)

- [14: REVIEW & COMPETITION](./14_competition/)
  - [Slides](./14_competition/gads23_14_classification_review.pdf) Classification Review
  - [Comparison of all classifiers](./14_competition/classification_models.ipynb) exercise
  - _[Guest Speaker](./guest_speakers.md): Bob Filbin, Chief Data Scientist at Crisis Text Line_
  - **Assignment #3: Classification** [Kaggle competition](https://inclass.kaggle.com/c/gads23-stack-overflow), [data exploration](./14_competition/stack_overflow_exploration.ipynb) and [demo solution](./14_competition/kaggle_competition.py)


**IV. Unsupervised Learning**

- [15: CLUSTERING](./15_clustering/)
  - [Slides](./15_clustering/gads23_15_kmeans.pdf)
  - [Clustering irises](./15_clustering/clustering_irises.ipynb) `sklearn`, simple demo
  - [Clustering text](./15_clustering/clustering_text.ipynb) `sklearn`, 20-newsgroups
  - [Clustering tags in Stack Overflow](15_clustering/clustering_tags_on_stack_overflow.ipynb) Jaccard distance, exercise
  - KMeans implementation: [notebook](./15_clustering/kmeans_exercise.ipynb) and [code](./15_clustering/kmeans_exercise.py) exercise

- [16: DIMENSIONALITY REDUCTION](./16_dim_reduction/)
  - Presentations data explorations final project
  - [Slides](./16_dim_reduction/gads23_16_dim_reduction.pdf)
  - [PCA demo](./16_dim_reduction/pca_demo_math.ipynb) demo of the math
  - [SVD demo](./16_dim_reduction/svd_pca_math.ipynb) demo of the math
  - [Clustering House Legislatures](./16_dim_reduction/clustering_house_legislatures.ipynb) demo PCA, polarizing politics
  - [Facial Recognition](./16_dim_reduction/facial_recognition.ipynb) demo PCA, SVM and exercise
  - [Latent Semantic Analysis](16_dim_reduction/clustering_text.ipynb) demo SVD, text clustering

- [17/18: RECOMMENDATION SYSTEMS](./17_recommendations/)
  - [Slides](./17_recommendations/gads23_17_recommendations.pdf)
  - [Recommending Beers](./17_recommendations/recommending_beers.ipynb) demo of several recommendation methods
  - [Who To Follow](./17_recommendations/who_to_follow_exercise.ipynb) exercise item-based collaborative filtering
  - _[Guest Speaker](./guest_speakers.md): George Kailas, CEO at Instadat_
  - Extracurricular: [predicting student responses](./further_reading.md#predicting-student-reponses)


**V. Various**

- [19: GUEST LECTURE - HASHING, A/B TESTING, CONJUGATE PRIORS](./19_guest/)
  - [Guest Lecturer](./guest_speakers.md): Robert Doherty, Lead Data Science at Outbrain
  - [Streaming Data Algorithms](./19_guest/streaming.pdf): Part 1 slides
  - [Bayesian A/B Headline Testing](./19_guest/bayes_ab.pdf): Part 2 slides
  - [The Beta Distribution](./19_guest/Beta_Distribution.ipynb)
  - [Instant Headline Testing](./19_guest/Instant_Headline_Testing.ipynb)
  - [Amazon Resellers](./19_guest/LAB-The_Beta_Distribution_and_Amazon_Resellers.ipynb) LAB incl exercises

- [20: NEURAL NETWORKS](./20_neural_nets/)
  - [Slides](./20_neural_nets/gads23_20_neural_nets.pdf)
  - Videos: [Neurons and the brain](https://class.coursera.org/ml-005/lecture/44), [Digit recognition](https://class.coursera.org/ml-005/lecture/48) and [Autonomous driving](https://class.coursera.org/ml-005/lecture/57) by Andrew Ng
  - [Python implementation](./20_neural_nets/neural_network.py) and [demonstrating notebook](./20_neural_nets/nn_implementation.ipynb) _optional_ deep dive
  - [Restriced Boltzmann Machines](./20_neural_nets/boltzmann_feature_extraction.ipynb) _optional_ demo unsupervied neural nets in `sklearn`
  - Code Reviews work-in-progress

- [21: Amazon Web Services](./21_aws/)
  - [Slides](./21_aws/gads23_aws.pdf)
  - [Introduction to Amazon Web Services](./21_aws/readme.md)
  - [Setting Up AWS](./21_aws/aws.md)
  - [The Hadoop File System (HDFS)](./21_aws/hadoop.md)
  - [Spark](./21_aws/spark.md)

- [22: MAP-REDUCE](./22_mapreduce/)
  - [Slides](./22_mapreduce/gads23_22_mapreduce.pdf)
  - [Multiprocessing in Python](./22_mapreduce/multiprocessing_in_python.ipynb) local parallel computing
  - [mrjob](./22_mapreduce/mrjob/) _optional_ mapreduce framework in python
  - [Guest Speaker](./guest_speakers.md): Ethics by Monica Bulger, Researcher at Data & Society

- 23: FINAL PROJECT PRESENTATIONS

<!--
- EXTRA
  - Streaming, hashing, sketch, HLL, AB testing
  - FIELD TRIP
  - probably lots of material from previous classes
  - LDA
 -->
