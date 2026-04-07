from django.db import models

class DataJob(models.Model):
    SOURCE_CHOICES = [
        ('bigquery', 'BigQuery'),
        ('graphql', 'GraphQL'),
        ('postgres', 'PostgreSQL'),
    ]

    source = models.CharField(max_length=50, choices=SOURCE_CHOICES)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.source} - {self.status}"