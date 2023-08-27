from django.db import models


class Alert(models.Model):
    user_id = models.BigIntegerField(null=False, blank=False)
    sats_level = models.IntegerField(null=False, blank=False)  # Sats/vB
    alert_counter = models.IntegerField(null=False, blank=False, default=0)


class LastAlert(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user_id = models.BigIntegerField(null=False, blank=False)
    last_alert = models.DateTimeField(null=False, blank=False, auto_now=True)
