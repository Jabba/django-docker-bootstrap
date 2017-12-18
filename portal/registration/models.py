from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email').__dict__['_unique'] = True
