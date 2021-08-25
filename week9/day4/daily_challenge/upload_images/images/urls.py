from django.urls import path
from . import views


urlpatterns = [
    path('home', views.ImageListView.as_view(), name='home'),
    path('add_image', views.UploadImage.as_view(), name='add_image'),
    path('sort_imgs', views.SortImgView.as_view(), name='sort_img'),
    path('sorted_imgs', views.SortedImgsList.as_view(), name='sorted_imgs'),
]
