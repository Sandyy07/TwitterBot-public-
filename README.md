# TwitterBot (public version)


Table of contents: 

Technologies
Python Libraries
Description


Technologies:
• Python • MongoDB • Heroku • Twitter API v2 • Git

Python Libraries:
• Tweepy • Multithreading • MongoDB Atlas API • PYgithub • requests • loadenv 

Description
A Python-based Twitter bot that uses the Twitter API endpoint to tweet a motivational quote every 2 hours while tracking a list of users to reply to their latest tweet with a random quote.
Technology: Python, MongoDB, Heroku, Git.

Detailed Description

$ The Twitter bot running on Heroku uses a 50 thousand tweets database hosted on MongoDB Atlas to post tweets every 2 hours.

$ The tweets are cleaned and formatted properly to show the author's name, tags, and other info while not exceeding the tweet character limit.

$ Simultaneously, it tracks the list of users from a MongoDB Atlas database where it also maintains the latest ID of the tweet of the specific user.

$ As soon as the user tweets, within 5 minutes, the bot replies to them with a new random quote. Then, it updates the ID of the tweet for future purposes.

$ All in all, On the first thread, the bot tweets a random quote on its profile every 2 hours and then sleeps.

$ Simultaneously, the second thread checks the tweet ID every 5 minutes and if a new tweet is found, replies to it.


$ Used a database of 50k quotes hosted on MongoDB, and fetched specific quotes from MongoDB Atlas web API using the python requests library.

$ Implemented tweet tracking by storing tweet IDs in MongoDB Database, bot updates the tweet ID every time a targeted user tweets, to which the bot replies.

$ Worked with the Tweepy library to GET and POST data via the Twitter V2 endpoint API.

$ Deployment on Heroku with worker dyno running all processes simultaneously using python multithreading, also developed a CI/CD pipeline using Heroku CLI.

$ I interacted with the API of Twitter to post and retrieve data, and MongoDB Atlas to save and update data.

$ Moreover, I created a lot of logical syntaxes to solve problems like getting a random quote from 50k quotes efficiently.

$ Tracking a list of users and only reply to un-replied/latest tweets modifying data into a human-readable tweet keeping the tokens and private files encrypted develop a CI/CD pipeline for the hassle-free deployment of production code along with maintaining failsafe git versions.
