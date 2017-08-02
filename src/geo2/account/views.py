from django.shortcuts import render
from django.contrib.auth.views import LogoutView as DefaultLogoutView, LoginView as DefaultLoginView

from analytics.signals import user_logged_in
from .forms import LoginForm
# Create your views here.
class LoginView(DefaultLoginView): #FormView[Similar to it]
	authentication_form = LoginForm

	#Extends the formview
	#We want to send the signal to get the IP address
	def form_valid(self, form):
		done_ = super(LoginView, self).form_valid(form)
		if self.request.user.is_authenticated():
			user_logged_in.send(self.request.user, request=self.request)
		return done_

class LogoutView(DefaultLogoutView):
	pass