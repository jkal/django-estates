from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError

from places.models import Place, User
from places.forms import PlaceForm

def check_username(request):
    if not request.POST:
        return HttpResponseForbidden()
    uname = request.POST.get('username', False)
    if User.objects.filter(username=uname):
        return HttpResponse('Username is not available.')
    else:
        return HttpResponse('OK')

def index(request):
    """
    Find the 5 latest and 5 most popular ads to display.
    """
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def all_places(request):
    all_places = get_list_or_404(Place, published=True)
    return render_to_response('places/all.html', {'places_list' : all_places}, context_instance=RequestContext(request))

@login_required
def fav_places(request):
    u = request.user
    return HttpResponse('Favorite ads for user %s' % u.username)

def view_place(request, place_id):
    """
    Find a place using its primary key and pass its information to the template.
    """

    my_place = get_object_or_404(Place, pk=place_id)
    return render_to_response('places/place.html', {'place' : my_place}, context_instance=RequestContext(request))

@login_required
def new_place(request):
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
    return render_to_response('places/new.html', { 'form': form })
