from django.db import models
from django import forms
# Create your models here.
def valid_name(value):
    if value[0].lower()=='f':
        raise forms.ValidationError('Name error at starting only')
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[valid_name])


def valid_url(value):
    if value[0].lower()=='com':
        raise forms.ValidationError('error at ending only')
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)    
    name=models.CharField(max_length=100)
    url=models.URLField()




def valid_author(value):
    if value[0].lower()=='g':
        raise forms.ValidationError('Name error at starting only')
class AccessRecords(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
