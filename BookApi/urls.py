from django.urls import path, include
from .api import *
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('list', bookListApi, name='list'),
#     path('create', bookCreateApi, name='create'),
#     path('view/<int:id>', bookDetailApi, name='view'),
#     path('update/<int:id>', bookUpdateApi, name='update'),
#     path('delete/<int:id>', bookDeleteApi, name='delete')
# ]

router = DefaultRouter()

router.register('router', BookViewSet, basename='router')

urlpatterns = [
    path('', include(router.urls)),
]