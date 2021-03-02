from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class LoggedInOnlyView(UserPassesTestMixin):
    permission_denied_message = 'Page not Found'
    
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('core:home')