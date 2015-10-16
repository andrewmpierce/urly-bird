from faker import Faker
from url.models import Url_User, Click, Accessed
from django.contrib.auth.models import User

import random
import hashids



fake = Faker()
def make_user():
    for x in range(100):
        new_user = User(username=fake.user_name(),
                    password='password',
                    email = fake.email(),
                    fav_color = 'blue')
        new_user.save()
        print(new_user)


def make_clicks():
    hashids = Hashids(salt="thisissalt")
    for x in range(500):
        new_click = Click(user=random.choice(User.objects.all(),
                     title=fake.text(max_nb_chars=15),
                     timestamp= fake.date_time_this_year(),
                     url = fake.url(),
                     short = hashids.encode(1, x)))
        new_click.save()
        print(new_click)


def make_accessed():
    for x in range(1000):
        new_accessed = Accessed(click = random.choice(Click.objects.all(),
                                url_user= click.user,
                                new_timstamp= fake.date_time_this_year()))
        new_accessed.save()
        print(new_accessed)
