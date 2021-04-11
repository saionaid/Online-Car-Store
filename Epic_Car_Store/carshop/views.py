from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import RegisterForm, ContactForm, ProductForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Product, CarType
from django.views.generic import UpdateView, ListView, FormView, TemplateView, DetailView, DeleteView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin



def congrats(request, *args, **kwargs):
    return render(request, "Congrats.html", {})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['carshop.change_product']
    template_name = 'product_update.html'
    model = Product
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('cars')


class ProductListView(ListView):
    template_name = "product_list.html"
    queryset = Product.objects.all()

class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['carshop.add_product']
    form_class = ProductForm

    template_name = "product_create.html"
    queryset = Product.objects.all()
    success_url = 'cars'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CarDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['carshop.delete_product']
    template_name = 'product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('cars')



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

    cartypes = CarType.objects.all()
    context = {'cartypes': cartypes}

    return render(request, "cars.html", context)

def contact_form(request, *args, **kwargs):
    return render(request, "contact_form.html", {})

def free4(request, *args, **kwargs):
    return render(request, "free4.html", {})





class CarsListView(ListView):
    model = Product

    context_object_name = 'product'
    template_name = 'carslist.html'

    def get_queryset(self):

        queryset = Product.objects.filter()

        category = self.request.GET.get('category', None)

        if category is not None:
            queryset = queryset.filter(type__id=int(category))

        return queryset



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




