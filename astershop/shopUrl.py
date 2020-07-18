from django.urls import path
from django.conf.urls import include
from astershop.product.products import Addproduct, ProductView, EditProduct, DelProduct
from astershop.service.login import CustomAuthToken, register

urlpatterns = [
    path(r'login', CustomAuthToken.as_view()),
    path(r'register', register.as_view()),
    path(r'Addprod', Addproduct.as_view()),
    path(r'product/<int:pk>', ProductView.as_view()),
    path(r'product', ProductView.as_view()),
    path(r'Editprod', EditProduct.as_view()),
    path(r'Delprod/<int:pk>', DelProduct.as_view()),
]
