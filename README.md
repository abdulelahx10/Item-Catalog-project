# Udacity Item Catalog Project

a python3 using Flask that provides a list of items within a variety of categories as well as provide a user registration and authentication system.
You'll be able to view, create, edit and delete items(editing and deleteing requires you to be the creator of that item)
You'll also be able to export the data as a JSON

## Getting Started


### Prerequisites

[Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) are needed
The used [Vagrantfile](https://www.dropbox.com/s/w3gsd5ve3t6qzs1/Vagrantfile?dl=0) to create Vagrant

The python program require many library to run, like Flask, sqlalchemy...
to install write these commands in the terminal:

```
pip3 install flask
pip3 install sqlalchemy
pip3 install oauth2client
pip3 install httplib2
```


## Running the the application

cd to the folder of the application:

```
cd Path/to/folder
```

Before running the application you need to setup the database and fill it with some data.
To setup:

```
python3 database_setup.py
```
then fill the database:
```
python3 items_seeder.py
```

running the application:

```
python3 app.py
```
this will run the application on the localhost port 5000
<http://localhost:5000>

## Authors

* **Abdulelah Alshalhoub** - *Initial work* - [abdulelahx10](https://github.com/abdulelahx10)