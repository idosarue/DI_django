from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import ThreadForm, CommentForm
from django.views.generic import CreateView, DetailView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Thread
# Create your views here.
class threadListView(ListView):
    model = Thread
    template_name = 'forum/all_threads.html'


class CreateThreadView(CreateView):
    form_class = ThreadForm
    template_name = 'forum/create_post.html'
    
    def form_valid(self, form):
        self.thread = form.save(commit=False)
        self.thread.creator = self.request.user
        self.thread.save()
        return super().form_valid(form)

        
    def get_success_url(self):
        return reverse_lazy('thread_detail', kwargs={'pk':self.thread.id})

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_details.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('create_comment', kwargs['pk'])
        return super().get(request, *args, **kwargs)


class CreateCommentView(CreateView):
    form_class = CommentForm
    template_name = 'forum/thread_details.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('thread_detail', kwargs['pk'])
        return super().get(request, *args, **kwargs)

    def get_post(self):
        thread_id = self.kwargs['pk']
        return get_object_or_404(Thread, id=thread_id)


    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.creator = self.request.user
        comment.thread = self.get_post()
        comment.save()
        return redirect('thread_detail', comment.thread.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = self.get_post()
        return context
    