from django.urls import path
from .views import product_list, product_create, product_detail, product_update, product_delete, category_create, \
    category_list, category_detail, category_update, category_delete

urlpatterns = [
    path('', product_list),
    path('create/', product_create),
    path("<int:product_id>/", product_detail),
    path("update/<int:product_id>/", product_update),
    path("delete/<int:product_id>/", product_delete),
    path("category/", category_list),
    path("category/create/", category_create),
    path("category/<int:category_id>/", category_detail),
    path("category/update/<int:category_id>/", category_update),
    path("category/delete/<int:category_id>/", category_delete),
]