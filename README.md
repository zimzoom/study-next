# Study-Next

These notebooks detail the building of a time series classifier that predicts which students in an online course will fail or drop out, after just a few weeks in to the course. Logistic regression, random forests, and LSTM neural networks are explored.

Data
---
Download data here: https://analyse.kmi.open.ac.uk/#open-dataset

In order to run the notebooks as they are, save the data in a directory named `data`

Key jupyter notebooks
---

`0_example_recommender`: building of a basic recommender for study materials that utilizes user similarity weighted by course success.

`0_timelines`: graphs showing student click behavior for all courses (one graph per course). Here we can see a definite pattern emerge: that **the click behavior of students who ultimately fail is more volatile than that of students who ultimately pass.**

`1_student_logreg`: logistic regression classifying students as succeed/fail based on student demographic information

`2_lstm_rf_diffs`: long short term memory neural network classifying students as succeed/fail based on student click behavior from the first quarter of course timelines (in order to simulate real-world prediction circumstances)

`3_timeseries_features_model`: **the most successful model in this project.** Here, a random forest classifier achieves 79% accuracy (and importantly, 87% precision on failing students) when given only the best, most useful features as identified by the tsfresh package, which is designed specifically for time series feature extraction.

Additional explanatory materials
---
`proposal.md` is the initial proposal for this project, which was originally focused on building a novel study material recommender

`presentation.pdf` contains the slides used in a presentation on this classification project. Not too informative without the accompanying speech, but good for getting a nutshell overview in 60 seconds.
