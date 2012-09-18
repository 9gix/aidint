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
mkvirtualenv --no-site-packages aidint-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages aidint-env
cd aidint-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> aidint
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
python manage.py syncdb
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000
