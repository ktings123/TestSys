from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from spo.Project.apiDetail import *
from spo.Project.ProductList import *

urlpatterns = [
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api', ApiView.as_view()),
    path(r'api/<int:pk>', DetailApiView.as_view()),
    path(r'Addapi', AddApi.as_view()),
    path(r'Editpai', EditApi.as_view()),
    path(r'Delapi', DelApi.as_view()),
    path(r'product', ProductListView.as_view()),
    path(r'product/<int:pk>', ProductListView.as_view()),
    path(r'Addprod', AddProduct.as_view()),
    path(r'Editprod/<int:pk>', EditProduct.as_view()),
    path(r'Delprod/<int:pk>', DelProduct.as_view())
]
