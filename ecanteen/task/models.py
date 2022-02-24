from django.db import models

# Create your models here.
class task(models.Model):
    task_name=models.CharField(max_length=100)
    task_description=models.TextField(max_length=100,null=True)

class Meta():
    db_table="task"
