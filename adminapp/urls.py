from django.urls import path

from adminapp.views import admin_users, UserCreateView, UserUpdateView, UserDeleteView, IndexTemplateView, UserListView

app_name = 'adminapp'
urlpatterns = [
    path('',IndexTemplateView.as_view(), name = 'index'),
    path('users/',UserListView.as_view(),name='admin_users'),
    path('user-create/',UserCreateView.as_view(),name='admin_user_create'),
    path('user-update/<int:pk>/',UserUpdateView.as_view(),name='admin_user_update'),
    path('admin-delete/<int:pk>/',UserDeleteView.as_view(),name='admin_user_delete'),
]