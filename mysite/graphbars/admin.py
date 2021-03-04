from django.contrib import admin
from . models import Department, Student, Teacher, Project

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Project)
