from django.urls import path
from myblog import views

urlpatterns = [
    path('',views.post_list, name = 'index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]