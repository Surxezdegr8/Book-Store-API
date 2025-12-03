from django.urls import path
from .api import *

urlpatterns = [
    path('create', create_user, name='create'),
    # path('login',login_user, name='login'),
    path('protected', protected_view, name='protected'),
]