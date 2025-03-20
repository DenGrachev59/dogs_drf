from django.urls import path
from rest_framework import routers

from dogs.views.dog import *
from dogs.views.breed import *
urlpatterns = [




]

router = routers.SimpleRouter()
router.register('breed', BreedViewSet)

urlpatterns += router.urls