
## treasureGram

The project will assegurate the explorers storing and allow manipulations in their treasures, as well as identifier explorer, images of treasures and one button to give how many likes you want.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. 

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.x +
PIP (Python Package Index)
Git
```

### Installing

A step by step series of examples that tell you have to get a development env running

The necessary steps will be

```
cd /path/to/your/projects
```

Cloning the repository

```
git clone https://github.com/rafaelribeiroo/treasureGram.git
```

Creating the isolated environment (Dismiss virtualEnv)

```
$ cd treasureGram && python -m venv .venv
```

Installing the prerequisites

```
$ source .venv/bin/activate && pip install -r requirements.txt
``` 

Gerenerate a random SECRETKEY

```
#Make sure that you in /path/to/the/project/treasureGram
$ python generateSecretKey.py
``` 
Doing this, copy the result and go to the next topic

Creating a .env file and attributing the values

```
$ sudo vim .env
SECRET_KEY=copy_here_your_secretkey_without_whitespace_after_before
DEBUG=TRUE
```

Running the project

```
$ make run
#If the port is already in use, try runserver 0.0.0.0:10201 instead
``` 

## Built With

* [Python](https://www.python.org/) - Programming language, used too to generate a random secretKey
* [Django](https://www.djangoproject.com/) - The web framework used

## Screenshots

* [Screen 1: Homepage](https://imgur.com/GwbNxJd)
* [Screen 2: Page Login](https://imgur.com/hVw5VOw)
* [Screen 3: Treasure Details](https://imgur.com/HO73kr1)

## Authors

* **Rafael Ribeiro** - *Maintaining* - [rafaelribeiroo](https://github.com/rafaelribeiroo)

## License

Course from [CodeSchool](https://www.codeschool.com/courses/digging-into-django)

## Acknowledgments

* Inspiration
