from django.core.urlresolvers import reverse
from django.contrib.auth.views import login
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from places.models import User

def custom_login(request):
    """ 
    If an already logged-in user visits the login page,
    redirect back to the front page. 
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index-page'))
    else:
        return login(request)

def check_username(request):
    """ 
    Used in the registration form (AJAX) to check for unavailable usernames.
    """
    if not request.POST:
        return HttpResponseForbidden()
    uname = request.POST.get('username', False)
    if User.objects.filter(username=uname):
        return HttpResponse('Username is not available.')
    else:	
        return HttpResponse('OK')
