from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('promo_email', views.get_promo_email, name='promo_email'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/comment_new/<int:pk>', views.comment_new, name='comment_new'),

]
