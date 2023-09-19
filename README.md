# Challenge-Rating-Predictor

This program creates a Graphical User Interface (GUI) in Python that allows users to generate predicted challenge ratings for custom monsters in the roleplaying game Dungeons and Dragons based on the values entered for various attributes.
These attributes include speed, size, skills, hit points, senses, and armor class. In order to generate predicted challenge ratings as accurately as possible, 14 JSON files were parsed where
each of them contained data regarding monsters in the game. Only relevant data was extracted which included the name of the monsters and the attributes mentioned above.
This data was then used to train the machine learning model which used the random forest regression algorithm to predict the challenge rating for any custom monster.
