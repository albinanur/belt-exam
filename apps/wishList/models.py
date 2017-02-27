from __future__ import unicode_literals
from ..loginRegister.models import User
from django.db import models

class Item(models.Model):
	name = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Wishlist(models.Model):
	item = models.ForeignKey(Item)
	user = models.ForeignKey(User)
	added_by = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


