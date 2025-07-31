from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BookViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("books", BookViewSet, basename="book")

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path("", include(router.urls))
]