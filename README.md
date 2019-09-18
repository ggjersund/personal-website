# Personal Website

[![Build Status](https://img.shields.io/travis/ggjersund/personal-website/master?style=flat-square)](https://travis-ci.org/ggjersund/personal-website)
[![Build Status](https://img.shields.io/coveralls/ggjersund/personal-website/master?style=flat-square&service=github)](https://travis-ci.org/ggjersund/personal-website)
[![GitHub issues](https://img.shields.io/github/issues/ggjersund/personal-website?style=flat-square)](https://github.com/ggjersund/personal-website/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/ggjersund/personal-website?style=flat-square)](https://github.com/ggjersund/personal-website/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ggjersund/personal-website?style=flat-square)](https://github.com/ggjersund/personal-website/network)

### Description
My personal developer website for displaying software I have created, make developer articles and whatever else I might find interesting.


### Development
To start the development environment you only need to have `docker` and `docker-compose` installed on your computer. Once these prerequisites are installed simply run `docker-compose up` (append `-d` for running in docker in the background). Wait for the environment to install dependencies and once it is finished you can start coding.


### Testing & Coverage
Tests are automatically run when pushing commits on any branch. `pytest` is used in combination with required Django plugins for running tests. Test coverage is run using `coverage`. To manually run, make sure you have activated the `pipenv` environment using `pipenv sync` followed by entering the shell using `pipenv shell`. Type `coverage run --source='.' -m pytest` from the repository root to run tests and check coverage. To check the coverage report simply type `coverage report -m`. A minimum requirement for code coverage is 80%. For checking code standards `pylint_runner` is used. All code must conform to PEP-8 and 10/10 is required to pass tests.


### Deployment
The master branch is continuously deployed. To get your changes onto the master branch you first have to perform a pull request on the development branch. You have to pass the tests, fulfill the minimum test coverage and pull request must be merged by an admin. Deployment is done in increments depending on the release of a new version and is done by a pull request from the deployment to the master branch. If you are manually deploying this project simply use `docker-machine` with the specified `docker-compose.prod.yml` file.
