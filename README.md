# e-Yantra Virtual Symposium Platform

## Pre-setup
Please look at some independent practice projects(related to threejs and not django) available in `harsh-dev` and `ngawang` branches to get some understanding of the threejs framework. Most of the projects are built(webpack build) from those branches and added to this project's static(javascript files) and templates(html files) folders.

Why we built project from practice branch and pasted them here?

We were not able to integerate django and webpack.

## Setup

> Use of Linux OS is recommended. However, it would work in any operating system.
- Setup a virtual environment
  ```
  python -m venv venv
  ```
- Install the required dependencies. Make sure to activate virtual environment before the below command.

  ```
  pip install -r requirements.txt
  ```

- Install `node` and `npm` from [official website](https://nodejs.org) or use [NVM](https://github.com/nvm-sh/nvm).

- Setup `NPM_BIN_PATH`(specific to your machine) in `settings.py` by copying the output of the command.

  ```
  which npm
  ```

  More instructions [here](https://django-tailwind.readthedocs.io/en/latest/installation.html#configuration-of-the-path-to-the-npm-executable)

- Install `taiwind` dependencies.

  ```
  python3 manage.py tailwind install
  ```

## Running the `django` server and `tailwind` cli

- To run the `django` server, run the command:

  ```
  python3 manage.py runserver
  ```

- To run the `tailwind` cli, run the command:

  ```
  python3 manage.py tailwind start
  ```

  Tailwind cli is needed only in development.

![logo-transparent](https://user-images.githubusercontent.com/56977388/180226746-a993ceb9-a886-4fc3-9b36-dbcb6cc93d41.png)


A social networking Django application (similar to Twitter) written in Python, HTML, CSS &amp; JavaScript.

#### Project Video: [Watch on Youtube](https://www.youtube.com/watch?v=d4_sidaZUZY)


<img width="954" alt="socialnetwork" src="https://user-images.githubusercontent.com/56977388/180219431-961e5777-28cf-470e-bd42-1c91fa176642.png">

## References

- https://docs.djangoproject.com/en/4.0/
- https://django-tailwind.readthedocs.io/en/latest/index.html