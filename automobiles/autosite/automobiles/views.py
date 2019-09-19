from django.shortcuts import render

from django.http import Http404

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import Car
from .models import Motorcycle
from .models import PersonOwnsCar
from .models import PersonOwnsMotorcycle
from .models import Person
from django.template import loader

from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.core.urlresolvers import reverse_lazy
 
# Create your views here.
from automobiles.models import Car
from automobiles.models import Motorcycle
from automobiles.models import PersonOwnsCar
from automobiles.models import PersonOwnsMotorcycle
from automobiles.models import Person

# view for the index page
class IndexView(generic.ListView):
    context_object_name = 'car_list'
     
    template_name = 'automobiles/index.html'

    def Index(request):
        car_list = Car.objects.all()
        return render(request, 'automobiles/index.html', locals())



    def get_queryset(self):
        return Car.objects.all()
       

# view for the car entry page
class CarEntry(CreateView):
    model = Car
    # the fields mentioned below become the entry rows in the generated form
    fields = ['car_id', 'year', 'make', 'model', 'price']
 
# view for the product update page
class CarUpdate(UpdateView):
    model = Car
    # the fields mentioned below become the entry rows in the update form
    fields = ['car_id', 'year', 'make', 'model', 'price']

# view for the index page
class IndexView2(generic.ListView):
    context_object_name = 'motorcycle_list'
    template_name = 'automobiles/index2.html'

    def Index2(request):
        motorcycle_list = Motorcycle.objects.all()
        return render(request, 'automobiles/index2.html', locals())

    def get_queryset(self):
        return Motorcycle.objects.all()

 
# view for the car entry page
class MotorcycleEntry(CreateView):
    model = Motorcycle
     #the fields mentioned below become the entry rows in the generated form
    fields = ['motorcycle_id', 'year', 'make', 'model', 'price']
 
# view for the product update page
class MotorcycleUpdate(UpdateView):
    model = Motorcycle
    # the fields mentioned below become the entry rows in the update form
    fields = ['motorcycle_id', 'year', 'make', 'model', 'price']



class IndexView3(generic.ListView):
    context_object_name = 'personownscar_list'
    template_name = 'automobiles/index3.html'

    def Index3(request):
        personownscar_list = PersonOwnsCar.objects.all()
        return render(request, 'automobiles/index3.html', locals())

    def get_queryset(self):
        return PersonOwnsCar.objects.all()

 
# view for the car entry page
class PersonOwnsCarEntry(CreateView):
    model = PersonOwnsCar
     #the fields mentioned below become the entry rows in the generated form
    fields = ['Quantity', 'Person', 'Car']
 
# view for the product update page
class PersonOwnsCarUpdate(UpdateView):
    model = PersonOwnsCar
 #   # the fields mentioned below become the entry rows in the update form
    fields = ['Quantity', 'Person', 'Car']



class IndexView4(generic.ListView):
    context_object_name = 'person_list'
    template_name = 'automobiles/index4.html'

    def Index4(request):
        person_list = Person.objects.all()
        return render(request, 'automobiles/index4.html', locals())

    def get_queryset(self):
        return Person.objects.all()

 
# view for the car entry page
class PersonEntry(CreateView):
    model = Person
   #  the fields mentioned below become the entry rows in the generated form
    fields = ['user_id', 'first_name', 'last_name', 'email']
 
 #view for the product update page
class PersonUpdate(UpdateView):
    model = Person
     #the fields mentioned below become the entry rows in the update form
    fields = ['user_id', 'first_name', 'last_name', 'email']

class IndexView5(generic.ListView):
    context_object_name = 'personownsmotorcycle_list'
    template_name = 'automobiles/index5.html'

    def Index5(request):
        personownsmotorcycle_list = PersonOwnsMotorcycle.objects.all()
        return render(request, 'automobiles/index5.html', locals())

    def get_queryset(self):
        return PersonOwnsMotorcycle.objects.all()

 
# view for the car entry page
class PersonOwnsMotorcycleEntry(CreateView):
    model = PersonOwnsMotorcycle
     #the fields mentioned below become the entry rows in the generated form
    fields = ['Quantity', 'Person', 'Motorcycle']
 
# view for the product update page
class PersonOwnsMotorcycleUpdate(UpdateView):
    model = PersonOwnsMotorcycle
 #   # the fields mentioned below become the entry rows in the update form
    fields = ['Quantity', 'Person', 'Motorcycle']





 

