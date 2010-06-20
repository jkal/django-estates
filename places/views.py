from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.core.files.base import ContentFile

from places.models import Place, Category, User, Favorite, Photo
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
    all_places = Place.objects.filter(published=True)
    return render_to_response('places/all.html', { 'places_list' : all_places, 'filter_on' : q }, context_instance=RequestContext(request))

@login_required
def fav_place(request, place_id):
    """ User makes a GET request to favorite a place. """ 
    if request.method == 'GET':
        u = request.user
        my_place = get_object_or_404(Place, pk=place_id)
        obj, created = Favorite.objects.get_or_create(user=u, place=my_place)
        if created:
            return HttpResponse('Your bookmarks have been updated.') 
        else:
            return HttpResponse('This is already on your bookmarks.') 
    else:
        return HttpResponse('What are you trying to do?')

def view_place(request, place_id):
    """
    Find a place using its primary key and pass its information to the template.
    """

    my_place = get_object_or_404(Place, pk=place_id)
    my_place.hits = my_place.hits + 1
    my_place.save()
    my_photos = list(Photo.objects.filter(place=my_place))
    return render_to_response('places/place.html', {'place' : my_place, 'photos' : my_photos}, context_instance=RequestContext(request))

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
            # print request.FILES
            new_place = form.save(commit=False)
            new_place.submitter = request.user
            new_place.save()
            
            # handle assets
            # for a in request.POST.getlist('asset'):
            #    pass
            
            # handle images
            for f in request.FILES.getlist('image'):
                new_photo = Photo(place=new_place)
                file_content = ContentFile(f.read())
                new_photo.pic.save(f.name, file_content)
                
            return HttpResponseRedirect(reverse('new-place-thanks')) 
        else:
            print form.errors
    else:
        form = PlaceForm()
    return render_to_response('places/new.html', { 'form' : form }, context_instance=RequestContext(request))
