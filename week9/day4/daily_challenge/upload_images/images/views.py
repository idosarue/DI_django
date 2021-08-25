from django.shortcuts import render
from django.views.generic import CreateView, ListView, FormView
from .forms import ImgForm, DateRangeForm
from .models import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class ImageListView(ListView):
    model = Image
    template_name = 'imgs/home.html'

class UploadImage(LoginRequiredMixin, CreateView):
    form_class = ImgForm
    template_name = 'imgs/add_img.html'
    success_url = reverse_lazy('home')

class SortImgView(FormView):
    form_class = DateRangeForm
    template_name = 'imgs/sort_imgs.html'

class SortedImgsList(ListView):
    template_name = 'imgs/sorted_imgs.html'

    def get_queryset(self): # new
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        images = Image.objects.filter(timestamp__range=[start_date, end_date])
        return images