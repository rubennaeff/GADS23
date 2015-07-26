# Course Project

### Overview

The final project should represent significant original work applying data science techniques to an interesting problem. Final projects are individual attainments, but you should be talking frequently with your instructors and classmates about them.


Please complete the following steps individually:

- Address a data related problem in a field you are interested in, or choose a Kaggle competition
- Vet your idea with the instructional team - ASAP, ultimately due
- Submit an outline for review - due
- Initial data exploration presentation - due
- Final data science presentation, for a non-tech audience - due
- Submit a paper or annotated notebook (for tech audience) - due


### Choosing a topic

Address a data-related problem in your professional field or a field you're interested in. Pick a subject that you're passionate about. If you're strongly interested in the subject matter it'll be more fun for you and you'll produce a better project!

To stimulate your thinking, you can take a look at the following resources
1. [Gallery of past GADS projects](https://gallery.generalassemb.ly/DS)
1. [Another overview of past GADS projects](https://github.com/justmarkham/DAT-project-examples)
1. Our own [data folder](./data/) lists many public data sources
1. [Kaggle competitions](https://www.kaggle.com/competitions)

You are allowed to pick a Kaggle competition as your project. A good competition to begin with is [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/), which even provides a step-by-step guide to get you started. Each Kaggle competition has discussion forums, where you can discuss your thoughts with other participants. Since Titanic is explicitly a beginner's competition, your scores will be erased after a few months. So you are free to experiment and "fail fast".

Additionally (and optionally), you could spend some time outlining how your modeling could be applied in a live system. For example, you could think of a website that gives users personal recommendations of some kind, based on their public profile on Twitter. Please describe where the data would live, how the results would be represented, and how your end-users would access it. This extra mile is optional. If you are really ambitious, you can even go ahead and implement all of this.

It doesn't really matter what you choose as long as there is plenty of data, and you are genuinely interested in it.

### Vetting your idea

Don't keep your thoughts to yourself: please talk frequently with your instructors and classmates about them!

Please check in as soon as possible with your instructors to see if your idea is achievable. Ideally, it is challenging yet small enough to do it well in a limited time span.


### Writing your outline

Please submit a consice plan of your project
- Main problem to solve
- Description of dataset, and you will you obtain it
- Hypothesis
- Statistical & Machine Learning methods you plan to use (and why)
- What business applications do you think your findings will have?


### Initial data exploration

Just to make sure your dataset is viable and rich enough, we will start a round of preliminary presentations that cover just the data exploration. This step is exactly the same as the **[first assignment](./04_presenting/assignment_01.md)** you did earlier. Please submit your presentation and code before class.

You could use this presentation to gather ideas from your classmates as well. Often the data turn out even more interesting than you already thought!

Keep it short, though: 2-5 minutes is enough. We'll spend probably plenty of time discussing it in the Q&A.


### Final presentation

The final presentation is the center piece of the course, and will take place on the last day of class. give Aim for a **5-7 minute** talk that summarizes the results in an engaging way. The presentations should target a **non-technical audience** and serve the purpose of having students practice the highly sought after communication skills that data scientists need. You could think of students of GA's other courses as your audience.

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
| Fair        | Student's presentation fails on two out of three of engaging, clear, and informative. 
| Poor        | Student's presentation fails on all three or is off-topic with respect to his or her paper. 



### Submit your paper

Students are also required to submit a short paper or a well-annotated ipython notebook that describes the project’s technical details.  The paper should target a **technical audience** (e.g., your classmates and instructional team).

What to cover in paper:
- Description of problem and hypothesis
- Detailed description your data set
  - Some basic statistics (# of rows, some aggregates)
  - How did you decide what features to use in your analysis?
  - What challenges did you face in terms of obtaining and organizing the data? 
  - What did you learn in the initial data exploration phase?
- Describe what kinds of statistical methods you used, and perhaps others you considered but did not use, and how you decided what to use. Think of regression, classification, recommendations, cross-validation, overfitting, etc.
- What business applications do your findings have? 
- _Optionally_, describe how your analyses would be implemented in a live system (e.g., a personal recommendation system or a tweetbot). Where would the data live, how would you represent your results, how would end-users access it? When would your model learn new parameters? Describe in detail the pipeline from data ingestion to end-user experience.

|  Grading    |                                                                        |
|-------------|:-----------------------------------------------------------------------|
| Excellent   | Student's paper demonstrates thorough understanding of statistical techniques, data management, and the application of these in programming, and is clearly communicated to a reasonably technical audience. |
| Good        | Student's paper demonstrates above knowledge, but lacks some necessary rigor, detail, and/or exploratory depth or is not well communicated. |
| Fair        | Student's paper demonstrates some learning of principles taught in class, but is clearly lacking in rigor and/or depth. |
| Poor        | Student's paper is incomplete or does not conclusively demonstrate understanding of statistics or programming. |













































## Project Deliverables

You are responsible for creating a **project paper** and a **project presentation**. The paper should be written with a technical audience in mind, while the presentation should target a more general audience. You will deliver your presentation (including slides) during the final week of class, though you are also encouraged to present it to other audiences.

Here are the components you should aim to cover in your paper:

* Problem statement and hypothesis
* Description of your data set and how it was obtained
* Description of any pre-processing steps you took
* What you learned from exploring the data, including visualizations
* How you chose which features to use in your analysis
* Details of your modeling process, including how you selected your models and validated them
* Your challenges and successes
* Possible extensions or business applications of your project
* Conclusions and key learnings

Your presentation should cover these components with less breadth and depth. Focus on creating an engaging, clear, and informative presentation that tells the story of your project.

Your project paper, presentation slides, and code should be included a **GitHub repository**, along with all of your data and a data dictionary. If it's not possible or practical to include your data, you should link to your data source and provide a sample of the data (anonymized if necessary).

Optionally, it would be exciting to actually implement a "live" system based on your work, and to the degree this is possible within the time frame of the course, it is certainly encouraged!


## Milestones

### Week 3 (10/21): Question and Data Set(s)

What is the question you hope to answer? What data are you planning to use to answer that question? What do you know about the data so far? Why did you choose this topic?

Example:
* I'm planning to predict passenger survival on the Titanic.
* I have Kaggle's Titanic dataset with 10 passenger characteristics.
* I know that many of the fields have missing values, that some of the text fields are messy and will require cleaning, and that about 38% of the passengers in the training set survive.
* I chose this topic because I'm fascinated by the history of the Titanic.

### Week 5 (11/4): Data Exploration and Analysis Plan

What data have you gathered, and how did you gather it? What steps have you taken to explore the data? Which areas of the data have you cleaned, and which areas still need cleaning? What insights have you gained from your exploration? Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)? How might you use modeling to answer your question?

Example:
* I've created visualizations and numeric summaries to explore how survivability differs by passenger characteristic, and it appears that gender and class have a large role in determining survivability.
* I estimated missing values for age using the titles provided in the Name column.
* I created features to represent "spouse on board" and "child on board" by further analyzing names.
* I think that the fare and ticket columns might be useful for predicting survival, but I still need to clean those columns.
* I analyzed the differences between the training and testing sets, and found that the average fare was slightly higher in the testing set.
* Since I'm predicting a binary outcome, I plan to use a classification method such as logistic regression to make my predictions.

### Week 8 (11/25): First Draft Due

Submit a rough copy of your work so far, including code, narrative, and visualizations. Describe your successess and challenges, and provide a detailed plan going forwards. Your peers and instructors will provide feedback.

### Week 10 (12/9): Second Draft Due

Submit a more polished version of your work, including drafts of your paper and your presentation. Your instructors will provide feedback.

### Week 11 (12/16): Presentation

Deliver your project presentation and submit all required deliverables (paper, slides, code, data, and data dictionary).