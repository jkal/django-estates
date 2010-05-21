from django.http import HttpResponseRedirect

"""
A decorator that allows the programmer to restrict access 
to some views only to non logged-in users. For instance, 
if auser in logged in, it should be denied access to views 
like /accounts/register or /accounts/login.
"""
 
def anonymous_required(view_function, redirect_to=None):
    return AnonymousRequired(view_function, redirect_to)
 
class AnonymousRequired(object):
    def __init__(self, view_function, redirect_to):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = settings.LOGIN_REDIRECT_URL
        self.view_function = view_function
        self.redirect_to = redirect_to
 
    def __call__(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated():
            return HttpResponseRedirect(self.redirect_to) 
        return self.view_function(request, *args, **kwargs)
