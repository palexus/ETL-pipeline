# Sentiment Analysis Docker Pipeline

Dockerized Pipeline of tweets using Twitter's API, MongoDB, PostgreSQL and Sentiment Analysis

## Project Description

In this project we created an ETL pipeline between two databases. First, we experimented with Twitter's API, where our text data (tweets) are being extracted from and stored directly in a NoSQL database (in our case MongoDB). The next step is a simple Extract-Transform-Load task (ETL job), whereby our data are being extracted from MongoDB, cleaned, transformed and analyzed based on positive or negative sentiment in order to be loaded into an SQL database (PostreSQL). In the last step, the most positive as well as the most negative score of each tweet (within a specific time interval) are being posted on the Slack-channel of our choice using a webhook-url from the built-in slackbot.

## How to Run

* Clone the whole repo locally on your machine
* Navigate from your (Bash) Terminal inside the project's main folder
* Locate and run the compose.yml-file with the following commands:
  + docker-compose build #Builds all containers
  + docker-compose up -d #Runs everything in the background
  + docker stop $(docker ps - aq) #Stops all containers
  + docker-compose down #Deletes all containers

## System Requirements

Be aware of the following system requirements before deploying the pipeline:

* latest version of Docker and Docker Compose
* all the packages and toolkits listed in requirements.txt
