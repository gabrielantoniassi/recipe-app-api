"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet) # Create endpoint for each method

app_name = 'recipe'

urlpatterns = [ # Select urls created by the router
    path('', include(router.urls)),
]
