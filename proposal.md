Study Recommender Proposal
===========
*K. Lucia Zimmermann*

I. Objective
---------
In the past few years, online courses have exploded in popularity. While such courses contain all educational materials associated with the course, they are lacking a crucial element associated with the “brick and mortar” university experience: structured guidance. This project is an attempt to create a recommender system for online course students that determines the most effective study schedule based on collaborative filtering and individual user session history.

II. Existing Solutions
----------
Recommender systems are usually used in retail or media streaming contexts. To date there are no recommender systems in production specifically designed to recommend an online course student's next study material. Nonetheless, the wealth of existing recommendation solutions should be enough to create one from a mix-and-match approach.

Of particular interest to this project are those recommender systems used in online publications, which calculate the best article for users to read next. This has clear parallels with this project's objective, as in both cases the items are reading material and thus share certain characteristics such as absolute length, length in average reading time, and semantic properties. However, one key difference is that online publications suffer from a severe cold-start problem, while an online course will have a minimal cold-start problem. This is due to a difference in the items' "useful lifespan." Newspaper or magazine articles are created much more often and lose utility much faster than study materials for an online course. Thus, an online course will have a significant lack of user-interaction information only for the first run of the course.

As of this project's commencement, the most relevant existing example is the CHAMELEON, a recommender for publications that uses a hybrid approach, utilizing both item feature extraction and user session history (de Souza et al, 2018). User sessions are of special importance to the current project, as a student's current and past behavior is informative to the best study strategy.

III. Novel Approach
------------
Since this project's recommender system aims to solve a new problem, it will use a new strategy to do so. Both content-based and collaborative-filtering modules will be incorporated, as both intrinsic item features and aggregate user scores are crucial for determining course materials' difficulty and importance. Exactly how each component should be weighed will need to be determined in the course of data exploration. Preliminary assumptions include: each study material item is of different difficulty and different importance, each item's characteristics can only be divined through an interaction of feature extraction and aggregate user outcomes, and these interactions will vary between courses.

There has been one analysis done on this dataset along similar lines, building a composite "importance" score for these study materials for the purpose of a future recommender system, from the combination of current user behavior and given description of items (Huptych et al, 2017). This project will take a different approach, building an "importance" score that is primarily based on the collaborative filter (that is, past user outcomes), and incorporated with other scores more geared toward intrinsic item features but with a minimal emphasis on given item descriptions.

Theoretically, this recommender should be realizable through basic traditional approaches to content-based and collaborative-filtering modules, but if time permits, the complexity of factor interactions could mean that the model would benefit from incorporating a neural net *a la* CHAMELEON.

IV. Impact
------------
These online course offerings are a particularly effective manifestation of the Internet’s general ability to make education more accessible, with even ‘upper tier’ universities posting the entirety of their courses online for free and open to anyone. Such democratization of higher learning is surely a boon to society. However, the fact remains that the paid "brick and mortar" formal education experience comes with more personal attention and guidance on not just what to learn, but how to learn.

Research has shown that building "maps" of how to study a given corpus, whether by setting a schedule, ranking items' importance, etc, contributes majorly to effective learning. (Young 2019)

If an artifial intelligence solution met this demand, it would allow the continued mass-scale distribution of education through free online course offerings, and equalize opportunity further.

V. Presentation
-----------
These points can be summarized in a five-minute presentation. In addition, a simple web app will be constructed to demonstrate how this recommender would look and feel to a user. Such a skeleton app does not actually require the completed model to function, though that would be nice to have.

VI. Data Source
-----------
This model will be developed around and trained on the Open University Learning Analytics Dataset (OULAD). This dataset consists of seven tables representing all the user interactions and outcomes from seven online courses administered by Open University. User data is anonymized and includes demographics, registration, click events, interaction duration, and scores.

VII. Potential Problems
------------
This project's ambition may end up unrealized if there is less signal in the data than would appear, or if that signal cannot be divined in the timespan of the project. This is the most likely problem, considering the amount of possible features and cross-interactions between those features. There are two solutions to this problem: scaling down the minimal viable outcome to a process that would inform a future recommender (such as identifying solid, informative scores), or designing the model to be more of a "black box" solution, which would sacrifice interpretability for predictive power.

VIII. Next Steps
------------
The dataset needs extensive EDA, which will inform the first draft of possible feature extractions and collaborative filters. 


-------------
*Sources*

de Souza Pereira Moreira, Gabriel and Ferreira, Felipe and da Cunha, Adilson Marques (2018). News Session-Based Recommendations using Deep Neural Networks. In: Proceedings of the 3rd Workshop on Deep Learning for Recommender Systems - DLRS 2018, http://dx.doi.org/10.1145/3270323.3270328

Huptych, Michal; Bohuslavek, Michal; Hlosta, Martin and Zdrahal, Zdenek (2017). Measures for recommendations
based on past students’ activity. In: LAK ’17 Proceedings of the Seventh International Learning Analytics & Knowledge
Conference on - LAK ’17, pp. 404–408. http://dx.doi.org/doi:10.1145/3027385.3027426

Young, Scott (2019). Ultralearning. Chapter 5. Harper-Collins.

-------------
*Dataset*

Open University Learning Analytics Dataset (OULAD), download at: https://analyse.kmi.open.ac.uk/open_dataset