from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('acc_make/', views.acc_make, name='acc_make'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
