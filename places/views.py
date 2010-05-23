from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError

from places.models import Place, Category, User
from places.forms import PlaceForm

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request)

def check_username(request):
    """ 
    Checks if the POST-ed username is available. 
    Called from an AJAX request in the registration form.
    ? Move this to some utility file.
    """
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

    latest5 = Place.objects.filter(published=True).order_by('-pub_date')[:5]
    popular5 = Place.objects.filter(published=True).order_by('-hits')[:5]
    categories = Category.objects.all()

    cx = { 
        'latest_places' : latest5,
        'popular_places' : popular5,
        'categories' : categories,
    }

    return render_to_response('index.html', cx, context_instance=RequestContext(request))

def all_places(request):
    q = request.GET.get('q', '')
    all_places = get_list_or_404(Place, published=True)
    return render_to_response('places/all.html', {'places_list' : all_places, 'filter_on' : q}, context_instance=RequestContext(request))

@login_required
def fav_places(request):
    u = request.user
    return render_to_response('places/fav.html', {}, context_instance=RequestContext(request))

def view_place(request, place_id):
    """
    Find a place using its primary key and pass its information to the template.
    """

    my_place = get_object_or_404(Place, pk=place_id)
    return render_to_response('places/place.html', {'place' : my_place}, context_instance=RequestContext(request))

@login_required
def delete_place(request, place_id):
    my_place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        if request.user == my_place.submitter:
            my_place.delete()
            return render_to_response('places/delete_complete.html', {'place' : my_place}, context_instance=RequestContext(request))
        else:
            return HttpResponseForbidden()
    else:
        return render_to_response('places/delete.html', {'place' : my_place}, context_instance=RequestContext(request))

@login_required
def new_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            print 'valid form'
            new_place = form.save(commit=False)
            new_place.submitter = request.user
            new_place.latitude = 33.3333
            new_place.longitude = 33.3333
            new_place.save()
            return HttpResponseRedirect('/places/new/thanks/') 
        else:
            print 'invalid form'
            print form.errors
    else:
        form = PlaceForm()
    return render_to_response('places/new.html', { 'form' : form }, context_instance=RequestContext(request))
