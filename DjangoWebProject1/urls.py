"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('feedback/', views.feedback, name='feedback'),
    path('registration/', views. registration, name= 'registration'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
     path('videogames/', views.videogame_list, name='videogame_list'),
    
     path('add_to_cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
     path('checkout/', views.checkout, name='checkout'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
   path('checkout/', views.checkout, name='checkout'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('add_to_cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('videogames/', views.videogame_list, name='videogame_list'),
    path('videogames/<int:game_id>/add_comment/', views.add_comment, name='add_comment'),
     path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
      path('add_to_cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
      path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
     path('feedback-list/', views.feedback_list, name='feedback_list'),

   
    # Other URL patterns

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
