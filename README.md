# Properties or whatever

This is a small django project, including some test data, just for fun.

# Notes

Django version: 2.2
virtual environment not required, but highly encouraged. Instructions are below.
Use pycharm. The django support isn't built into the free edition, but it's better than notepad.

# Setup steps for windows

- install git bash for windows
- install python (or confirm it's installed)
- create virtual environment (optional)
- install dependencies
- set the settings environment variable
- create the database
- load the test data
- run the server
- go to the url to confirm it's working
- mess around


#### Install git bash for windows
- Install the git bash tools for windows, which will give you access to git commands in the windows command line. Follow the instructions on the website, located here: https://gitforwindows.org/

#### Install python
- Open up a windows terminal by going to the search bar and typing in `cmd`. Type `python --version`. If it prints version 3.something, you're good. If not, install one of the version 3 releases from this site: https://www.python.org/downloads/windows/.
- Try running `python --version` again. If it works, great. If not, you may need to add the python executable to your path.
- Type `path` into your windows search bar and open "Edit the System Evironment Variables"
- In the "Advanced" tab, click "Environment Variables", then click on the entry for "Path", "Edit", "New" and type in the path to your python executable.

#### Create a virtual environment
- Open a windows terminal, and install virtualenvwrapper with `pip install virtualenvwrapper`
- Use `mkvirtualenv <name you want>` to create a new virtual environment. You should see a `(name you want)` indicating you're in that virtual environment once it's done
- In general, use `workon <name>` to get into it and `deactivate` to exit.
- Any python packages installed here are only accessible in the virtual environment

#### Install dependencies
- Once you've cloned the repo, go to the base of the repo, where the .gitignore, README.md, and manage.py files are
- Ensure you're in your virtual environment
- `pip install -r web_service\requirements\base.txt` to install all dependencies (just django 2.2 right now)

#### Set the settings environment variable
- `set DJANGO_SETTINGS_MODULE=web_service.settings.local`

#### Create the database
- In the folder with manage.py:
- `python manage.py makemigrations`
- `python manage.py migrate`

#### Load the test data
- In the folder with manage.py:
- `python manage.py loaddata properties.json`
- There are now a bunch of addresses to play around with in your local database

#### Run the server
- `python manage.py runserver`

#### Go to the url
- Open up a browser
- go to `localhost:8000/properties/`
- You should get a page that lists the first 100 of the addresses in a barebones table.

#### Mess around
- Make all the changes you want. You have a skeleton project and some test data.
- If you change the models.py, run `python manage.py makemigrations` and `python manage.py migrate` to have your changes reflected in the database
- You can reload the data at any time. Reloading the data makes all data match what was there after the first `loaddata`, so any changes you made to the database will be overwritten.
