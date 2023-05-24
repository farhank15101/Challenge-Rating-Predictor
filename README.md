# Challenge-Rating-Predictor

This program creates a Graphical User Interface (GUI) in Python that allows users to generate predicted challenge ratings for custom monsters in the roleplaying game Dungeons and Dragons based on various attributes.
These attributes include speed, size, skills, hit points, senses, and armor class. In order to generate challenge ratings as accurately as possible, 14 json files were parsed where
each of them contained information regarding monsters in the game. Only relevant information was extracted which included the name of the monsters and the attributes mentioned above.
This information was then used to train the machine learning model which used the random forest regression algorithm to predict the challenge rating for a monster
