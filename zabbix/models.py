from django.db import models


class Machines(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'machines'
        app_label = 'general_controls'
