from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=40,
        help_text='enter your name.', null=True)
    email_id = models.EmailField(max_length=254, null=True)
    notification_time = models.TimeField(
        help_text='Enter the time you would like to recieve notfication.')
    streak = models.IntegerField(blank=True, null=True,
        default='0',
        help_text='The number of days of continuous awesome productivity!')
    coins = models.IntegerField(blank=True, null=True)
    intrests = models.ManyToManyField('Intrest',
        help_text='Select all your preferred choices!')
    key = models.ManyToManyField('Keywords')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']


class Intrest(models.Model):
    topic = models.CharField(max_length=20)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('intrest-detail', args=[str(self.id)])

    class Meta:
        ordering = ['topic']

class Keywords(models.Model):
    kw = models.CharField(max_length=20)
    link = models.ManyToManyField('Link')

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['kw']

class Link(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['url']
