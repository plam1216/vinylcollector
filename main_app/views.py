from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .models import Vinyl, Buyer
from .forms import PurchaseForm

# Create your views here.
def home(request):
    # return HttpResponse('Home working')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyls_index(request):
    vinyls = Vinyl.objects.all()
    # render 'index.html' from folder 'vinyls'
    return render(request, 'vinyls/index.html', {'vinyls': vinyls})

def vinyls_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)

    has_not_purchased = Buyer.objects.exclude(id__in = vinyl.buyers.all().values_list('id'))

    purchase_form = PurchaseForm
    return render(request, 'vinyls/detail.html', {
        'vinyl': vinyl,
        'purchase_form': purchase_form,
        'buyers': has_not_purchased    
    })

def add_purchase(request, vinyl_id):
    # create ModelForm using 'request.POST'
    form = PurchaseForm(request.POST)
    # validate form
    if form.is_valid():
        # don't save to db until vinyl_id is assigned
        new_purchase = form.save(commit=False)
        new_purchase.vinyl_id = vinyl_id
        new_purchase.save()
    return redirect('detail', vinyl_id=vinyl_id)

def assoc_buyer(request, vinyl_id, buyer_id):
    Vinyl.objects.get(id=vinyl_id).buyers.add(buyer_id)
    return redirect('detail', vinyl_id=vinyl_id)

class VinylCreate(CreateView):
    model = Vinyl
    # include all fields from Vinyl in 'models.py'
    # fields = '__all__'
    fields = ['name', 'artist', 'genre', 'year']
    # success_url = '/vinyls/'

class VinylUpdate(UpdateView):
    model = Vinyl
    # only allow user to update certain fields of Vinyl
    fields = ['artist', 'genre', 'year']

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'

class BuyerCreate(CreateView):
    model=Buyer
    fields = ('name',)

class BuyerUpdate(UpdateView):
    model=Buyer
    fields=('name',)

class BuyerDelete(DeleteView):
    model=Buyer
    success_url = '/buyers/'

class BuyerDetail(DetailView):
    model = Buyer
    template_name = 'buyers/detail.html'

class BuyerList(ListView):
    model = Buyer
    template_name = 'buyers/index.html'