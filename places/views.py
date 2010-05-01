from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError

from places.models import Place
from places.forms import PlaceForm

def index(request):
    # Find 5 newest and most popular ads.
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def details(request):
    return render_to_response('details.html', {}, context_instance=RequestContext(request))

def all_view(request):
    all_places = Place.objects.all()
    return render_to_response('all.html', {'places_list' : all_places}, context_instance=RequestContext(request))

def new_view(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/places/new/thanks/') 
    else:
        form = PlaceForm() # An unbound form
        return render_to_response('new.html', {'form': form})
