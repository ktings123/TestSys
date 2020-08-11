from django.urls import path
from astershop.product.products import Addproduct, ProductView, EditProduct, DelProduct
from service.login import obtain_auth_token, Register,Logout

urlpatterns = [
    path(r'login', obtain_auth_token),
    path(r'logout', Logout.as_view()),
    path(r'register', Register.as_view()),
    path(r'Addprod', Addproduct.as_view()),
    path(r'product/<int:pk>', ProductView.as_view()),
    path(r'product', ProductView.as_view()),
    path(r'Editprod', EditProduct.as_view()),
    path(r'Delprod/<int:pk>', DelProduct.as_view()),

]
