from faker import Faker
from .models import Click
from django.contrib.auth.models import User

import random
from hashids import Hashids


hashids = Hashids()
fake = Faker()

def get_data():
    users = []
    clicks = []
    accessed = []


    User.objects.all().delete()
    Click.objects.all().delete()

    for x in range(100):
        new_user = User.objects.create_user(username=fake.user_name(),
                    password='password',
                    email = fake.email())

        new_user.save()
        users.append(new_user)
        print(new_user)

    hashids = Hashids(min_length=6, salt="thisissalt")
    for x in range(500):
        new_click = Click(author=random.choice(users),
                     title=fake.text(max_nb_chars=15),
                     timestamp= fake.date_time_this_year(),
                     orig = fake.url(),
                     short = hashids.encode(x))

        new_click.save()
        clicks.append(new_click)
        print(new_click)
