from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from products.models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_create_view(request):
    
    # this is a raw html way of doing things and should be avoided
    
    # if request.method == "POST":
    #     new_title = request.POST.get('title')
    #     Product.objects.create(title=new_title)

    # this is a pure django way (using forms.Form) of rendering a form and saving data returned from the form
    # the benefit of this approach is that django builds validation automatically based on your form model.
    # where you use form.as_p in the html to render some form fields
    
    # my_form = RawProductForm() # the default for GET method when you want to render a form with empty fields
    # if request.method == "POST":        
    #     my_form = RawProductForm(request.POST) # putting the request.POST allows the capture of data from the form
    #     if my_form.is_valid():
    #         print(my_form.cleaned_data) # the data from form after validation
    #         Product.create(**my_form.cleaned_data) # save to DB
    #     else:
    #         print(my_form.errors)
    
    # product_context = {"form": my_form}
    
    # use this approach if your form is made from forms.ModelForm

    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductForm() # wipes out the form data after saving
        

        product_context = {"form": form} 

        # templates are created within the products app
        return render(request, "products/create.html", product_context)

    return render_initial_data(request) # for GET method


def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    
    if request.method == "POST":
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../")
    
    print("check for get ")
    if request.method == "GET":
        initial = { "title": obj.title, "description": obj.description, "price": obj.price }
        form = ProductForm(request.GET or None, initial=initial) 

    context = {"form": form}
    return render(request, "products/create.html", context)


# view based off product id
def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id) # this is the preferred way of getting an object which may not exist in the db
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    # print(obj)
    context = { "product": obj }
    return render(request, "products/details.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # if you want to delete it on a GET request you can simple do obj.delete()
    if request.method == "POST":
        # got a delete confirmation
        obj.delete()
        redirect("../")
    context = { "product": obj }

    return render(request, "products/delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()

    context = { "object_list": queryset }
    return render(request,"products/list.html", context )


def render_initial_data(request):
    initial_data = {
        "title": "smpl_title"
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    product_context = { "form": form }
    return render(request, "products/create.html", product_context)
