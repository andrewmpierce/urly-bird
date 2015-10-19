## URLy Bird
![URLy bird](https://usadultliteracy.files.wordpress.com/2013/05/earlybird1.jpg)

#### This is a Django app designed to be similar to bit.ly. It is a URL shortener.


Users can input URLs to be shortened and saved as bookmarks.  Users can look at their bookmarks as well as see data on any individual bookmarks or the popularity of the bookmarks they have created.

To Run:

* You will need to install some requirements from the requirements.txt file from a machine with Python installed. Do this by running the
command `pip install -r requirements.txt` from the command line. 
* Next, load in fake data from fake-factory by running `python manage.py shell`.
* Next, type `from urly.load_data import \*`. * Lastly, enter `get_data()`.

This will generate fake users and fake click activity. You can also access the site as it
is, but it will be a bit more lonely.

Finally, you can run the the command 'python manage.py runserver' to see the site
hosted on a local server.
