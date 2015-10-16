from faker import Faker
from urly_bird.models import Bird


class Generate_user_data():

    fake = Faker()

    Url_user.objects.all().delete()

    users = []

    for _ in range(100):
        new_user = user.id
        new_user.set_password('password')
        new_user.save()
        users.append(new_user)
