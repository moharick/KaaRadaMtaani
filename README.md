# KaaRadaMtaani

[![BCH compliance](https://bettercodehub.com/edge/badge/moharick/KaaRadaMtaani?branch=master)](https://bettercodehub.com/)
## Description
This is a web application that allows a user to be in the loop about everything happening in their neighborhood.

## Author
### [Moharick](https://github.com/moharick)



## Screenshots
<img src="https://github.com/moharick/project-1/blob/master/mtaa.png" width="1000">
<img src="https://github.com/moharick/project-1/blob/master/mtaa2.png" width="1000">
<img src="https://github.com/moharick/project-1/blob/master/mtaa3.png" width="1000">

## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/moharick/KaaRadaMtaani.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd KaaRadaMtaani
```

##### 2. Create a virtual environment
 Install `Virtualenv`

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```gallery```
   ```prettier
   # create database gallery
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python manage.py makemigrations gallery
```


then run the command below;

 ```bash
 python manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    python3 manage.py runserver

### Running Tests
>To run tests;

    python manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
As a user I would like to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.


## Bugs
There are no known bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2019 Moharick

## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
> Send me an [email](moharick@gmail.com) to collaborate on the project.

