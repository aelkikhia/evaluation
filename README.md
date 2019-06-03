# evaluation
Sample code for evaluation

## Run locally

### Requirements
* commandline: Python 3.6 and pip
* Flask REST api: Flask, Flask-Cors, Flask-JWT, Flask-RESTful, Flask-SQLAlchemy
    
### Installation
Install the requirements: `pip install -r requirements/requirements.txt`
   
### Run scripts on commandline 
* Array Diff: `python bin/array-diff.py --current 1 3 5 6 8 9 --target 1 2 5 7 9`
* Social Network Analysis: `python bin/social-network-analysis.py -f <file>`
   
## Running in Docker as a flask endpoint
command line: `docker-compose build && docker-compose up` 