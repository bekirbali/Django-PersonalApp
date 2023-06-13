from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=64)
    user_id=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Personnel(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True, blank=True)

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer Not to Say'),

    )

    gender = models.CharField(max_length=1, choices=GENDER, default='N')

    TITLE = (
        ('Jr', 'Junior'),
        ('Md', 'Mid Level'),
        ('Sr', 'Senior'),
        ('Ac', 'Associate'),
    )

    title = models.CharField(max_length=2, choices=TITLE, default='Jr')
    salary = models.IntegerField()
    started = models.DateField()
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} - {self.title}'