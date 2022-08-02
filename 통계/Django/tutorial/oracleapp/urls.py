from django.urls import path

from . import views

app_name = "oracle"

urlpatterns = [
    path('test/', views.test),    
    path('member_list/', views.view_Member_List),   
    path('member/', views.view_Member), 
    path('cart_list/', views.view_Cart_List),
    path('cart/', views.view_Cart),    
    path('cart_insert_form/', views.view_Cart_Insert),
    path('cart_insert/', views.set_Cart_Insert),
    path('testdict/', views.testDict),
    path('cart_list_dict/', views.view_Cart_List_dict),
    path('lprod_list/', views.view_Lprod_List),
    path('lprod/', views.view_Lprod),
    path('cart_delete/', views.set_Cart_Delete),
    path('cart_update_form/', views.view_Cart_Update),
    path('cart_update/', views.set_Cart_Update),
    path('login_form/', views.login_form),
    path('login/', views.getLogin),
    path('logout/', views.set_Logout),
    path('cart_list_page/', views.view_Cart_List_Page, name="cart_list_page"),
]
