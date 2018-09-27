from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from player.views import home, new_invitations, accept_invitations, SignUpView

urlpatterns = [
    url('home', home, name='player_home'),
    url('login', LoginView.as_view(template_name="player/login_form.html"), name='player_login'),
    url('logout', LogoutView.as_view(), name='player_logout'),
    url('new_invitations', new_invitations, name='player_new_invitations'),
    url(r'^accept_invitations/(?P<id>\d+)/$', accept_invitations, name='player_accept_invitation'),
    url('signup', SignUpView.as_view(), name='player_signup')

]