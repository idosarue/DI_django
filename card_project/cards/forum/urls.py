from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('all_threads/', views.threadListView.as_view(), name='all_threads'),
    path('threads/new/', views.CreateThreadView.as_view(), name='create_thread'),
    path('threades/<int:pk>', views.CreateCommentView.as_view(), name='create_comment'),
    path('thread/<int:pk>', views.ThreadDetailView.as_view(), name='thread_detail'),
    path('leaderboard/', views.leaderBoardView.as_view(), name='leader_board')
]
