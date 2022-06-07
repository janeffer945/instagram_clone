from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('',views.home, name = 'home'),
  path('upload/image', views.upload_image, name = "upload_image"),
  path('create_profile/',views.create_profile,name = 'create_profile'),
  re_path('profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
  path('like/(?P<image_id>\d+)', views.like_image, name = 'like_image'),
  path('comment/(?P<image_id>\d+)', views.comment,name = "comment"),
  path('profile/edit', views.profile_edit,name = 'profile_edit'),
  re_path('search/', views.search, name='search'),
  path('email/', views.email, name='email'),
  re_path('image/(?P<image_id>\d+)',views.one_image,name = 'single_image')
]