# Devops Candidate Take-Home Assessment

## Purpose

The purpose of this assessment is to validate that the candidate can:

* package and ship a web application
* use docker
* understand python dependency management
* understand Python/Django basics
* understand networking basics
* understand Unix/Linux basics
* explain their design/architecture decisions

## Project Prompt

As a way to determine your ability to produce quality work autonomously and
demonstrate a few skills, we would like you to containerize a small web
application for us. The web app is a tiny Django app with one model and one
view. All it does is count page views. Imagine a junior developer has just
built this and wants to deploy it. They have, so far, only used the default
sqlite development database and directly installed things with pip. Your job
is to create a Dockerfile for the web application and it’s dependencies and a
Docker Compose file describing a database and a webserver as well as the web
application itself. The web app should talk to a standalone database,
preferably Mysql or Postgres, as opposed to the default sqlite local
file-based database. The application itself should talk to the standalone
database and sit behind a web server. This will require changing the Django
settings file so the database can be configured to talk to the standalone
database. You will also need to link all of the containers up in the
docker-compose.yml file. We would prefer you use Nginx for the web server,
but if you know another technology that would fit better, feel free to use
it. You may use community docker images for the web server and database
server, but we would like you to write the Dockerfile for the web
application.

## Project Deliverables

Please send us back the project repository with the following:

* Changes to the settings file
* Any files required for building or dependency management
* A Dockerfile for building the web application docker image
* A docker-compose.yml file that can be used to spin up the app/web server/database as a cluster. We should be able to build the cluster by just issuing `docker-compose up`.
* A file explaining any decisions you had to make or challenges you overcame.

## Bonus Points

We would love to see:

* Project history (We sent you a git repository, so you can commit your work as you see fit)
* Some way to repeatedly test that your cluster is communicating correctly.
