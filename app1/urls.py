from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/', views.coin, name='coin'),
    path('get-coin/', views.get_all_coin, name='get-coin'),
    path('get-user-prod/<int:user_id>/<int:days>', views.get_user_products, name='getuserproducts'),
    path('addprod/', views.productaddform, name='productaddform'),
    path('addcli/', views.clientaddform, name='clientaddform'),
    path('addorder/', views.orderaddform, name='orderaddform'),
    path('get-client_orders/', views.client_orders_form, name='client_orders_form'),
    path('get-all-clients/', views.get_all_clients_in_db, name='get-all-client'),
    path('get-all-products/', views.get_all_products_in_db, name='get-all-products'),
]


