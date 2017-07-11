# flask-basic

A basic flask app.

## Setup

Clone the repository and change into its directory.

```
$ git clone git@github.com:natemeier/flask-basic.git
$ cd flask-basic
```

Create a virtual environment and activate it. This is where dependencies for the project will be installed.

```
$ virtualenv venv
$ source /venv/bin/activate
```

Note:  If the `virtualenv` command fails, you need to install it globally with pip.

```
$ pip install virtualenv
```

After activating the project virtual environment, install project dependencies.

```
$ pip install -r requirements.txt
```

Run the server, and visit the site at `127.0.0.1:5000`.

```
$ python run.py
```
