from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ])

    class Meta:
        db_table = 'ticket'

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'department'

class UserQuery(models.Model):
    user_id = models.IntegerField()
    query_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    response_text = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'user_query'