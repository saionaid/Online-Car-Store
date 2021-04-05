from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from .forms import RegisterForm, ContactForm, ProductForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Product, CarType
from django.views.generic import ListView, FormView, TemplateView, DetailView, DeleteView, CreateView








class ProductListView(ListView):
    template_name = "product_list.html"
    queryset = Product.objects.all()

class ProductCreateView(CreateView):

    form_class = ProductForm

    template_name = "product_create.html"
    queryset = Product.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)




def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})


def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def cars(request,*args,**kwargs):
    return render(request, "cars.html", {})

def contact_form(request, *args, **kwargs):
    return render(request, "contact_form.html", {})

def free4(request, *args, **kwargs):
    return render(request, "free4.html", {})


class HydrogenView(ListView):
    model = Product
    queryset = Product.objects.filter(type__name='Hydrogen')
    context_object_name = 'product'
    template_name = 'Hydrogen.html'



class DieselView(ListView):
    model = Product
    queryset = Product.objects.filter(type__name='Diesel')
    context_object_name = 'product'
    template_name = 'Hydrogen.html'

class PetrolView(ListView):
    model = Product
    queryset = Product.objects.filter(type__name='Petrol')
    context_object_name = 'product'
    template_name = 'Petrol.html'


class ElectricView(ListView):
    model = Product
    queryset = Product.objects.filter(type__name='Electric')
    context_object_name = 'product'
    template_name = 'Electric.html'


class GasView(ListView):
    model = Product
    queryset = Product.objects.filter(type__name='Gas')
    context_object_name = 'product'
    template_name = 'Gas.html'

class HybridView(ListView):
    model = Product
    queryset = Product.objects.filter(type__name='Hybrid')
    context_object_name = 'product'
    template_name = 'Hybrid.html'

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("http://127.0.0.1:8000/home")

    form = ContactForm()
    return render(request, "contact_form.html", {'form': form})




