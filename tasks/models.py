from django.db import models

class Task(models.Model):
    TYPE_OF_STATUS = {
        "todo": "To Do",
        "working": "Working",
        "done": "Done"
    }
    DIFFICULTY = {
        "low": "Low",
        "medium": "Medium",
        "high": "High"
    }

    name = models.CharField(max_length=100, blank=True, default="Task")
    status = models.CharField(max_length=7, choices=TYPE_OF_STATUS, blank=True, default="todo")
    priority = models.CharField(max_length=6, choices=DIFFICULTY, blank=True, default="low")
    complexity = models.CharField(max_length=6, choices=DIFFICULTY, blank=True, default="low")
    summary = models.CharField(max_length=500, blank=True, default="")


    def ___str___(self):
        return self
    

