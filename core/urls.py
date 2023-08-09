from django.urls import path
from . import views

urlpatterns = [

    path('', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/create', views.PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    path('\about', views.about, name='about'),
    
]