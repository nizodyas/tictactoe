from django.forms import ModelForm

from player.models import Invitaion


class InvitaionForm(ModelForm):
    class Meta:
        model = Invitaion
        exclude = ('from_player', 'timestamp')