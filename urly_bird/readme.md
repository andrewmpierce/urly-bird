URLy Bird

This is a Django app designed to be a clone of bit.ly. It is a URL shortener.
Users can input URL's to be shortened and users can look at their bookmarks as well
as see data on any individual bookmarks or the popularity of the bookmarks they have
created.

To Run:
You will need to install the requirements from the requirements.txt by running the
command "pip install -r 'requirements.txt'" from a machine with Python installed.
At this point you can load in fake data from fake-factory by running 'python
manage.py shell' then 'from urly.load_data import \*' and then 'get_data()'. This
will generate fake users and fake click activity. You can also access the site as it
is, but it will be a bit more lonely.

Finally you can run the the command 'python manage.py runserver' to see the site
hosted on a local server.
