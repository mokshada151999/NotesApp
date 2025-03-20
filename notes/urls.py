from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Notes CRUD URLs
    path('notes/', views.note_list, name='note_list'),
    path('notes/create/', views.create_note, name='create_note'),
    path('notes/<int:note_id>/edit/', views.update_note, name='update_note'),
    path('notes/<int:note_id>/delete/', views.delete_note, name='delete_note'),
]
