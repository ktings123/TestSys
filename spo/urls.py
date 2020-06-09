from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from spo.Project.apiDetail import ApiView, DetailApiView
from spo.Project.ProductList import AddProduct, ProductListView, EditProduct

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/$', ApiView.as_view()),
    url(r'api/(?P<pk>[0-9]+)', DetailApiView.as_view()),
    url(r'product', ProductListView.as_view()),
    url(r'Addprod', AddProduct.as_view()),
    url(r'Editprod/(?P<pk>\d+)/', EditProduct.as_view()),

    # url(r'user', views.index),
    # url(r'views1', views.in_a),
    # path('',views.index,name='index'),
    # path('',views.index2,name='index2'),
]
