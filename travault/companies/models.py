from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    reference1 = models.CharField(max_length=255, blank=True)
    reference2 = models.CharField(max_length=255, blank=True)
    domain_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='owned_companies')
    industry = models.CharField(max_length=100)
    address = models.JSONField()
    description = models.TextField()
    linkedin_url = models.URLField(blank=True)
    type = models.CharField(max_length=50, choices=[
        ('PROSPECT', 'Prospect'),
        ('CLIENT', 'Client'),
        ('FORMER', 'Former Client'),
        ('SUPPLIER', 'Supplier'),
        ('OTHER', 'Other')
    ])
    ops_team = models.JSONField()
    client_type = models.CharField(max_length=50, choices=[
        ('TRAVEL', 'Travel'),
        ('EVENTS', 'Meetings and Events')
    ])
    account_status = models.CharField(max_length=50, choices=[
        ('LEAD', 'Lead'),
        ('NEW', 'New Client'),
        ('TRADING', 'Trading'),
        ('NOT_TRADING', 'No Longer Trading'),
        ('ON_HOLD', 'On Hold')
    ])
    payment_info = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
