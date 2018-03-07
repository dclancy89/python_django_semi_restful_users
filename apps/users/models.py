from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def validate_user(self, postData):
		errors = {}

		try:
			validate_email(postData['email'])
		except ValidationError:
			errors['email'] = "This is not a valid email."
		else:
			if User.objects.get(email=postData['email']):
				errors['email'] = "This user already exists."



		if len(postData['first_name']) < 2:
			errors['first_name'] = "First name must be greater than 2 characters."
		if len(postData['last_name']) < 2:
			errors['last_name'] = "Last name must be greater than 2 characters."

		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()