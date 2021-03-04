from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name






