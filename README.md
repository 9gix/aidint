# Aidint Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --distribute aidint-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages aidint-env
cd aidint-env
source bin/activate
```

### Configure Environment ###
Because this project has no manage.py, you can either write the manage.py yourself or 
you can set the virtualenv postactivate to automate the configuration of your PYTHON_PATH and the DJANGO_SETTINGS_MODULE.
If not, you will have to EXPORT them everytime you start a new bash.

The PYTHON_PATH and DJANGO_SETTINGS_MODULE value is depends on your environment.


### Clone the code ###
Obtain the url to your git repository.

```bash
git clone https://github.com/yeo-eugene-oey/aidint
```

### Install requirements ###
```bash
cd aidint
pip install -r requirements.txt
```

### Configure project ###
```bash
cp aidint/__local_settings.py aidint/local_settings.py
vi aidint/local_settings.py
```

### Sync database ###
```bash
django-admin.py syncdb
django-admin.py migrate
```

## Running ##
```bash
django-admin.py runserver
```

Open browser to http://127.0.0.1:8000
