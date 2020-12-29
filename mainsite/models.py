from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class AccessInfo(models.Model):
    access_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-access_time',)

    def __str__(self):
        return self.access_time

class Branch(models.Model):
    shop_name = models.CharField(max_length=200)
    boss_name = models.CharField(max_length=200)

    def __str__(self):
        return self.shop_name

class StoreIncome(models.Model):
    income_year = models.CharField(max_length=4)
    income_month = models.CharField(max_length=2)
    income = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.income)

class Kindergarten(models.Model):
    president = models.CharField(max_length=100)
    branch_school = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_school

class SchoolStu(models.Model):
    recruit_year = models.CharField(max_length=4)
    recruit_num = models.PositiveIntegerField()
    kindergarten = models.ForeignKey(Kindergarten, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.recruit_num)

class Photo(models.Model):
    image = models.ImageField(upload_to='image/',blank=False, null=False)
    upload_date = models.DateField(default=timezone.now)

class Visitor(models.Model):
    states = models.CharField(max_length=6)
    country = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    visitor_num = models.PositiveIntegerField()

    def __str__(self):
        return str(self.visitor_num)
class Asiacountry(models.Model):
    asia_country = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    
    def __str__(self):
        return (self.asia_country)

class Visitors(models.Model):
    states = models.CharField(max_length=6)
    country = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    visitors_num = models.PositiveIntegerField()

    def __str__(self):
        return str(self.visitors_num)

class HelloVisit(models.Model):
    states = models.CharField(max_length=6)
    country = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    visitors_num = models.PositiveIntegerField()

    def __str__(self):
        return str(self.visitors_num)