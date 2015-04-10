from django.db import models

# # Create your models here.
class Event(models.Model):
	id = models.AutoField(primary_key=True,)
	type = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	short_name = models.CharField(max_length=45)
	country = models.CharField(max_length=45)
	city = models.CharField(max_length=45)
	date_from = models.DateField()
	date_to = models.DateField()
	par_type = models.CharField(max_length=45)
	age_group = models.CharField(max_length=45)
	gender = models.CharField(max_length=45)
	mcate = models.CharField(max_length=100)
	fcate = models.CharField(max_length=100)
	system = models.CharField(max_length=45)
	mat_no = models.IntegerField(max_length=11)
	time = models.IntegerField(max_length=11)
	ref_no = models.IntegerField(max_length=11)
	activated = models.IntegerField(max_length=4)
	small_str = models.CharField(max_length=45)
	seed_no = models.IntegerField(max_length=4)

	class Meta:
		db_table = u'jua_event'

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	weight = models.CharField(max_length=45)
	gender = models.CharField(max_length=10)
	drawn = models.IntegerField(max_length=4)
	event_id = models.IntegerField(max_length=11)
	date = models.DateField()

	class Meta:
		db_table = u'jua_category'


class AdminUser(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=20)
	passwd = models.CharField(max_length=20)
	
	class Meta:
		db_table = u'admin_user'


