from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.core.files.base import ContentFile
from places.models import Place, Category, User, Favorite, Photo
from places.forms import PlaceForm

def index(request):
    """ Find the 5 latest and 5 most popular places to display. """

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
    """ Create a list with all places and pass it to the template. """
    
    q = request.GET.get('q', '')
    all_places = Place.objects.filter(published=True)
    
    cx = { 
        'places_list' : all_places, 
        'filter_on' : q 
    }
    
    return render_to_response('places/all.html', cx, context_instance=RequestContext(request))

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
    my_photos = list(Photo.objects.filter(place=my_place))
    my_assets = my_place.assets.all()
    # increase views
    my_place.hits += 1
    my_place.save()
    
    cx = {
        'place' : my_place, 
        'photos' : my_photos,
        'assets' : my_assets,
    }
    
    return render_to_response('places/place.html', cx, context_instance=RequestContext(request))

@login_required
def delete_place(request, place_id):
    """ Delete place pointed by place_id. """
    
    my_place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        if request.user == my_place.submitter:
            my_place.delete()
            return render_to_response('places/delete_complete.html', { 'place' : my_place }, context_instance=RequestContext(request))
        else:
            return HttpResponseForbidden()
    else:
        return render_to_response('places/delete.html', { 'place' : my_place }, context_instance=RequestContext(request))

@login_required
def new_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            new_place = form.save(commit=False)
            new_place.submitter = request.user
            new_place.save()
            
            # required because of commit=False above
            # see: http://docs.djangoproject.com/en/dev/topics/forms/modelforms/#the-save-method
            form.save_m2m() 

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
