from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.core.files.base import ContentFile
from django.utils.translation import ugettext_lazy as _
from places.models import Place, Category, User, Favorite, Photo
from places.forms import PlaceForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
    latest5 = Place.objects.filter(published=True).order_by('-pub_date')[:5]
    popular5 = Place.objects.filter(published=True).order_by('-hits')[:5]
    categories = Category.objects.all()

    cx = { 
        'latest_places' : latest5,
        'popular_places' : popular5,
        'categories' : categories,
    }

    return render_to_response('index.html', cx, context_instance=RequestContext(request))
    
def search_places_count(request):
    if request.method != 'POST':
        return HttpResponse(status=405) # Method Not Allowed, GET is not allowed.
    query = request.POST.get('q', False)
    
    if query:
        # count()'s supposed to be faster than len()
        results = Place.objects.search(query).filter(published=True).count()
    else:
        results = Place.objects.all().count()
    
    return HttpResponse(results)

def search_places(request):
    query = request.GET.get('q', False)
    if query:
        # See PlaceManager in models.py.
        results = Place.objects.search(query).filter(published=True)
    else:
        # Return all places.
        results = Place.objects.filter(published=True)
    
    # Pagination takes place in the template.
    return render_to_response('places/all.html', { 'place_list' : results }, context_instance=RequestContext(request))

@login_required
def fav_place(request, place_id):
    """ User makes a POST request to favorite a place. """ 
    
    if request.method == 'POST':
        u = request.user
        my_place = get_object_or_404(Place, pk=place_id)
        obj, created = Favorite.objects.get_or_create(user=u, place=my_place)
        if created:
            return HttpResponse(status=200) # OK, bookmarks updated.
        else:
            return HttpResponse(status=304) # Not Modified, already bookmarked.
    else:
        return HttpResponse(status=405) # Method Not Allowed, GET is not allowed.

def view_place(request, place_id):
    """ Find a place based on PK and pass its information to the template. """

    my_place = get_object_or_404(Place, pk=place_id)
    my_photos = list(Photo.objects.filter(place=my_place))
    my_assets = my_place.assets.all()
    
    # Determine if the object is faved so that we can mark it.
    is_faved = False
    if request.user.is_authenticated(): 
        try:
            is_faved = Favorite.objects.get(user=request.user, place=my_place)
        except ObjectDoesNotExist:
            pass

    # Increase views.
    my_place.hits += 1
    my_place.save()
    
    cx = {
        'place' : my_place, 
        'photos' : my_photos,
        'assets' : my_assets,
        'is_faved' : is_faved,
    }
    
    return render_to_response('places/place.html', cx, context_instance=RequestContext(request))

@login_required
def delete_place(request, place_id):
    """ Delete place pointed by place_id. """
    
    my_place = get_object_or_404(Place, pk=place_id)
    if request.method == 'POST':
        # Necessary checks. Admins can delete places from the frontend.
        if request.user == my_place.submitter or request.user.is_staff:
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
