Provisioning a new site
=======================

## required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* SEE nginx.template.conf in this folder
* replace SITENAME with, e.g., superlists-staging.jacobson.tech

# Systemd Service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., superlists-staging.jacobson.tech

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        ├── virtualenv 

       