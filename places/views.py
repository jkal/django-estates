from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))
