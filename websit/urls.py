from django.urls import path
from websit.views import *

urlpatterns = [
    path('',index_view),
    path('about',about_view),
    path('contact',contact_view)
]
