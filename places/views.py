from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError

from places.models import Place
from places.forms import PlaceForm

def index(request):
    # Find the 5 newest and most popular ads.
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def details(request):
    return render_to_response('details.html', {}, context_instance=RequestContext(request))

def all_view(request):
    # all_places = Place.objects.all()
    #all_places = get_list_or_404(Place)
    all_places = get_list_or_404(Place, published=True)
    return render_to_response('all.html', {'places_list' : all_places}, context_instance=RequestContext(request))

def new_view(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            new_place = form.save()
            #new_place.save()
            return HttpResponseRedirect('/places/new/thanks/') 
        else:
            print 'invalid form'
    else:
        form = PlaceForm()
    return render_to_response('add.html', { 'form': form })
