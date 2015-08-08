# Course Project

The final project should represent significant original work applying data science techniques to an interesting problem. Final projects are **individual** attainments, but you should be talking frequently with your instructors and classmates about them.

You are responsible for creating a **project paper** and a **project presentation**. The paper should be written with a technical audience in mind, while the presentation should target a more general audience. Optionally, it would be exciting to actually implement a "live" system based on your work, and to the degree this is possible within the time frame of the course, it is certainly encouraged!


### Overview

Please complete the following steps:

- [Choose your topic](#choose-your-topic): a data related problem in a field you are interested in, or a Kaggle competition
- [Vet your ideas](#vet-your-ideas) with the instructional team - ASAP, ultimately **due Tue Aug 04** (lesson #12)
- [Submit an outline](#submit-an-outline) for review - **due Tue Aug 11** (lesson #14)
- [Initial data exploration](#initial-data-exploration) presentation - **on Tue Aug 18** (lesson #16)
- [Submit your work-in-progress](#submit-your-work-in-progress) - **due Tue Sept 1** (lesson #20)
- [Final presentation](#final-presentation), for a non-tech audience - **on Thu Sept 10** (lesson #23)
- [Submit your paper](#submit-your-paper) or annotated notebook (for tech audience) - **due Thu Sept 10** (lesson #23)

Please reach out to your instructional team if you think you won't make any of these deadlines.


### Choosing a topic

Address a data-related problem in your professional field or a field you're interested in. Pick a subject that you're passionate about. If you're strongly interested in the subject matter it'll be more fun for you and you'll produce a better project!

To stimulate your thinking, you can take a look at the following resources

1. [Selected projects](#selected-projects) listed below
1. GA's public [Gallery of projects](https://gallery.generalassemb.ly/DS)
1. Another [overview of past GADS projects](https://github.com/justmarkham/DAT-project-examples)
1. Our own [data folder](./data/) lists many public data sources
1. [Kaggle competitions](https://www.kaggle.com/competitions)

You are allowed to pick a Kaggle competition as your project. A good competition to begin with is [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/), which even provides a step-by-step guide to get you started. Each Kaggle competition has discussion forums, where you can discuss your thoughts with other participants. Since Titanic is explicitly a beginner's competition, your scores will be erased after a few months. So you are free to experiment and "fail fast".

Additionally (and optionally), you could spend some time outlining how your modeling could be applied in a live system. For example, you could think of a website that gives users personal recommendations of some kind, based on their public profile on Twitter. Please describe where the data would live, how the results would be represented, and how your end-users would access it. This extra mile is optional. If you are really ambitious, you can even go ahead and implement all of this.

It doesn't really matter what you choose as long as there is plenty of data, and you are genuinely interested in it.

### Vet your ideas

Don't keep your thoughts to yourself: please talk frequently with your instructors and classmates about them! Please check in as soon as possible with your instructors to see if your idea is achievable. Ideally, it is challenging yet small enough to do it well in a limited time span.


### Submit an outline

Please submit a consice plan of your project
- Main problem to solve
- Description of dataset, and you will you obtain it
- Hypothesis
- Statistical & Machine Learning methods you plan to use (and why)
- What business applications do you think your findings will have?

Please keep it concise. A paragraph with five sentences would suffice. It is understood that things might change during the course of your research.

### Initial data exploration

Just to make sure your dataset is viable and rich enough, we will start a round of preliminary presentations that cover just the data exploration. This step is exactly the same as the **[first assignment](./04_presenting/assignment_01.md)** you did earlier. Please submit your presentation and code before class.

You could use this presentation to gather ideas from your classmates as well. Often the data turn out even more interesting than you already thought!

You may keep it short: **2-5 minutes** is enough, but it's fine if you go a little longer. We'll spend probably plenty of time discussing it in the Q&A.


### Submit your work-in-progress

Submit a rough copy of your work so far, including code, narrative, and visualizations.  An annotated ipython notebook would suffice.  Briefly describe your successess and challenges, and explain next steps. Your peers and instructors will provide feedback.

We might set up some code reviews. Each students will review two submissions to provide feedback, tips and tricks. It's not only usefull to get suggestions from peers, but reviewing other people's code goes a long way as well.


### Final presentation

The final presentation is the center piece of the course, and will take place on the last day of class. give Aim for a **5-7 minute** talk that summarizes the results in an engaging way. The presentations should target a **non-technical audience** and serve the purpose of having students practice the highly sought after communication skills that data scientists need. You could think of students of GA's other courses as your audience. Focus on creating an engaging, clear, and informative presentation that tells the story of your project.

What to cover in presentation:
- Overview of problem and hypothesis
- Overview of your data
- Modeling techniques used and why (save the details for your paper)
- Conclusions
- Further research and/or business opportunities

|  Grading    |                                                                        |
|-------------|:-----------------------------------------------------------------------|
| Excellent   | Student's presentation is engaging, clear, and informative, describing the project, approach, and conclusions, and is suitable for a non-technical audience. |
| Good        | Student's presentation is as above but is either inadequately engaging, clear, or informative. |
| Fair        | Student's presentation fails on two out of three of engaging, clear, and informative. |
| Poor        | Student's presentation fails on all three or is off-topic with respect to his or her paper. |



### Submit your paper

Students are also required to submit a short paper or a well-annotated ipython notebook that describes the project’s technical details.  The paper should target a **technical audience** (e.g., your classmates and instructional team).

What to cover in paper:
- Description of problem and hypothesis
- Detailed description your data set
  - Description of your dataset and how it was obtained
  - Some basic statistics (# of rows, some aggregates)
  - What did you learn in the initial data exploration phase?
  - How did you decide what features to use in your analysis?
  - Description of any pre-processing steps you took
- Detailed description your models
  - Describe what kinds of statistical methods and machine learning algorithms you used
  - How did you validate your models?
  - What other models did you consider, and why didn't you proceed with those?
  - Some suggested keywords are regression, classification, recommendations, cross-validation, overfitting, etc.
- What business applications do your findings have? 
- _Optionally_, describe how your analyses would be implemented in a live system (e.g., a personal recommendation system or a tweetbot). Where would the data live, how would you represent your results, how would end-users access it? When would your model learn new parameters? Describe in detail the pipeline from data ingestion to end-user experience.

|  Grading    |                                                                        |
|-------------|:-----------------------------------------------------------------------|
| Excellent   | Student's paper demonstrates thorough understanding of statistical techniques, data management, and the application of these in programming, and is clearly communicated to a reasonably technical audience. |
| Good        | Student's paper demonstrates above knowledge, but lacks some necessary rigor, detail, and/or exploratory depth or is not well communicated. |
| Fair        | Student's paper demonstrates some learning of principles taught in class, but is clearly lacking in rigor and/or depth. |
| Poor        | Student's paper is incomplete or does not conclusively demonstrate understanding of statistics or programming. |



## Examples


### Selected projects

- [Predicting Kickstarter](https://github.com/justmarkham/DAT-project-examples/blob/master/pdf/kickstarter_presentation.pdf) Ruben's own final project
- [VoteLikeYouTweet](http://votelikeyoutweet.com/) Classifying tweets according to political engagement (by Ruben)
- [Haterz gon' hate](http://haternews.herokuapp.com/?network=twitter) Computing hater score of your tweets (or news groups or reddit posts) by Kevin McAlear


### Example milestones

#### Outline
* I'm planning to predict passenger survival on the Titanic.
* I chose this topic because I'm fascinated by the history of the Titanic.
* I feel everyone knows this competition, so I have become curious.
* I am an extremely ambitious person and would like to beat the leaderboard right away.
* At a first sight, the data looks very structured, and the problem is very straightforward, so I think this would be perfect for my first steps as a data scientist.
* Since I'm predicting a binary outcome, I plan to use a classification method such as logistic regression to make my predictions.

#### Data Exploration
* I have Kaggle's Titanic dataset with 10 passenger characteristics.
* The dataset has less than 900 rows, which I think is enough for some nice insights, but not too much to be overwhelming. I should be careful not to add too many features, though.
* I know that many of the fields have missing values, that some of the text fields are messy and will require cleaning, and that about 38% of the passengers in the training set survive.
* I've created visualizations and numeric summaries to explore how survivability differs by passenger characteristic, and it appears that gender and class have a large role in determining survivability.
* I think that the fare and ticket columns might be useful for predicting survival, but I still need to clean those columns.
* I analyzed the differences between the training and testing sets, and found that the average fare was slightly higher in the testing set.

#### Work-in-progress
* I estimated missing values for age using the titles provided in the Name column.
* I created features to represent "spouse on board" and "child on board" by further analyzing names.
* My logistic regression models never reached a satisfying accuracy, as they all stayed under 56%. My precision and recall were even lower than that, around 50% and 35%, respectively.
* Looking at these visualizations, I think my data cannot be separated by a straight line. So I am considering applying a second degree polynomial before applying a logistic regression, as we did in lesson #9 in the [Non-linear decision boundaries notebook](./09_logistic_regression/non_linear_decision_boundaries.ipynb).
* I tried Logistic Regression and Naive Bayes, but I still want to give Random Forest a shot. I see structure in the data, but it's not very linear, I think.

