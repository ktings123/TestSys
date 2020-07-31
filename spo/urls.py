from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from spo.Project.apiDetail import *
from spo.Project.ProductList import *
from spo.test_api.tests import *

urlpatterns = [
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api', ApiView.as_view()),
    path(r'api/<int:pk>', DetailApiView.as_view()),
    path(r'Addapi', AddApi.as_view()),
    path(r'Editapi', EditApi.as_view()),
    path(r'Delapi', DelApi.as_view()),
    path(r'product', ProductListView.as_view()),
    path(r'product/<int:pk>', ProductListView.as_view()),
    path(r'Addpro', AddProduct.as_view()),
    path(r'Editpro/<int:pk>', EditProduct.as_view()),
    path(r'Delpro/<int:pk>', DelProduct.as_view()),
    path(r'test_api', Api_test_get.as_view()),
]
