from django.db import models
from sysadmin.models import Category

class User(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100, unique=True)
	passwd = models.CharField(max_length=100)
	team = models.CharField(max_length=100)
	tel = models.CharField(max_length=20)
	email = models.CharField(max_length=100)

	class Meta:
		db_table = u'jua_user'
	def __unicode__(self):
		return self.username

# Create your models here.
class Person(models.Model):
	id = models.AutoField(primary_key=True)
	team = models.CharField(max_length=100)
	family_name = models.CharField(max_length=255)
	given_name = models.CharField(max_length=255)
	simple_name = models.CharField(max_length=255)
	identity_num = models.CharField(max_length=255)
	gender = models.CharField(max_length=45)
	groupe = models.CharField(max_length=100)
	category = models.CharField(max_length=45)
	edit_time = models.DateField(auto_now=True)
	create_time = models.DateField(auto_now_add=True)
	seeding = models.IntegerField(default=0)
	category_id = models.IntegerField(default=0)
	failed = models.IntegerField(default=0)
	event_id = models.IntegerField(default=0)
	ranking = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	type = models.CharField(max_length=45)
	team_id = models.CharField(max_length=45)
	seed_rank = models.IntegerField(default=0)
	img_url = models.CharField(max_length=100)

	birth = models.DateField()
	best_result = models.CharField(max_length=100)
	number_of_officials = models.CharField(max_length=100)
	number_of_competitiors = models.CharField(max_length=100)
	federation = models.CharField(max_length=100)
	passport_no = models.CharField(max_length=100)
	tel = models.CharField(max_length=20)
	email = models.CharField(max_length=100)
	adress = models.CharField(max_length=255)

	class Meta:
		db_table = u'jua_person'
	def __unicode__(self):
		return 'Team: %s ; Name: %s .%s' % (self.team, self.family_name, self.given_name)

	# def save():

