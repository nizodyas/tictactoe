from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Invitaion(models.Model):
    from_player = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="invitations_received",
                                verbose_name="User to invite",
                                help_text="please select a user you eant to play with",
                                on_delete=models.CASCADE
                                )
    message = models.CharField(max_length=300,
                               verbose_name="Optional Message",
                               help_text="It's always nice to add a friendly message"
                               )
    timestamp = models.DateTimeField(auto_now_add=True)

