# Set-up
## Superuser  
username: viswa-vinod
password: vinod-django

## pylint setup
.vscode/settings.json requires 
"python.pythonPath": "~/.pyenv/versions/3.7.2/bin/python3.7"

to be added so that pylint can use python3.7 to recognize django module. Very strange that adding the python added in the local virtualenv does not work. 

also, do
(https://stackoverflow.com/questions/45135263/class-has-no-objects-member)
pip install pylint-django

And add the following to .pylintrc in vscode
load-plugins=pylint-django

# manage.py commands
All manage.py commands must be run from the src folder

- python manage.py runserver  (used to run the server which renders the app)
- python manage.py createsuperuser ( usually run once to creae an admin user; must run when db gets deleted )
- python manage.py migrate (see below) 
- python manage.py startapp <appname>  (used to create product )
- python manage.py makemigrations (see below )
- python manage.py shell (to get the python shell that also allows all of django magic to run)

Always run the following commands when a change to a model.py is made

- python manage.py makemigrations
- python manage.py migrate

# Add/Edit objects to models:
This can be done using the admin app or by using the python shell.

from products.models import Product
Product.objects.create(title='bands', description='exercise bands for glutes and knees exercises', price=200, summary='got to learn how to use it')

# views
When you create view, 
 - define the view function, specifically the context (except for very basic case) and template
 - create the template, preferably within the app (django lingo for 'component')
 - register the template in the urls array (trydjango/urls.py)
