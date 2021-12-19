from django.urls import path

from app.register import views as register_views

urlpatterns = [
    path('', register_views.index, name='index')
]
