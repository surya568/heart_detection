from django.urls import path,include
from . import views
urlpatterns = [
    path('detect/',views.page2,name='detect'),
]
