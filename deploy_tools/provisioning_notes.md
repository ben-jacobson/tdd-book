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

       
## Using Fabric
* A fabfile.py has been provided to automate as much of the deployment as possible
* however since fabfile uses the SSH-Agent and expects credentials, we are going to get stuck if we want to use AWS EC2 instances (In this case we are)

# simply add your PEM file to the SSH Agent
$ ssh-add MY_PEM_FILE.pem

# Then run the Fabric deployment script
$ cd deploy_tools
$ fab deploy:host=USER@MY_EC2_INSTANCE_DOMAIN
