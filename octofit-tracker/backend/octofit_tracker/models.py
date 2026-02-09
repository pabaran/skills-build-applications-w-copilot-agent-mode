from django.db import models


class Team(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=24, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, editable=False)
    user = models.CharField(max_length=24)
    activity_type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} on {self.date}"

class Workout(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, editable=False)
    user = models.CharField(max_length=24)
    score = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Rank {self.rank}"
