# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)
# # /books GET
# # /books POST
# # /books/:id GET
# # /books/:id PUT
# # /books/:id DELETE

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
# Provide the 'basename' explicitly to avoid the 'QuerySet' object has no attribute 'model' error
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
