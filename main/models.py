from django.db import models
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.email
