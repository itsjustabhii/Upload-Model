# Upload-Model
Application built using Python-Django framework

## Backend

### Setting up of environment

Setting up of virtual environment
Use anaconda's `conda` environments or `virtualenv`

#### Creation of virtualenv with python

`virtualenv venv`

#### Activation of virtualenv

`source venv/bin/activate`

Once the virtualenv is activated, go ahead with the installation of the libraries

Use the requirements.txt to install the pre-requisites mentioned for the project
`pip install -r requirements.txt`

Use the following command to start the backend Django server
`python manage.py runserver`

Once started the project runs on a standard Django `port 8000` Keep the project running and move to frontend folder in the command line with `cd frontend`

Process:

1. Upload the files from file upload control to server from the GUI

2. The files are uploaded into the server's backend folder i.e. media folder and served as `static` files from the backend.
   The url the backend uses to serve the files is: ``http://localhost:8000
