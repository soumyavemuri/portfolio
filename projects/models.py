from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    technologies = models.CharField(max_length=40, default='Technologies')
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=140)
    lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    content = models.CharField(max_length=400, default=lorem)
    dateofProject = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class Skill(models.Model):
    #title
    skill = models.CharField(max_length=20)
    # familiarity
    familiarity = models.IntegerField(verbose_name='familiarity with skill')

    def __str__(self):
        return self.skill