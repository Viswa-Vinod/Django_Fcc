from django.urls import path
from products.views import (
    product_detail_view, 
    product_create_view, 
    product_delete_view, 
    product_list_view,
    product_update_view
)

app_name = "products" # namespacing used in models.py, the get_absolute_url function
urlpatterns = [
     # route names are used in get_absolute_url
    # using route names lets you change the actual route but still refer to the actual route string 
    # within this code-base with the name everywhere else
    path('', product_list_view, name="product-list"), 
    path('create/', product_create_view, name="product-create"),
    path('<int:id>/', product_detail_view, name="product-detail"), # route with url params
    path('<int:id>/update', product_update_view, name="product-update"),
    path('<int:id>/delete', product_delete_view, name="product-delete")
]
