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
router.register('recipes', views.RecipeViewSet) # Create endpoint for each method of recipe app
router.register('tags', views.TagViewSet)       # Create endpoint for each method of tags app

app_name = 'recipe'

urlpatterns = [ # Select urls created by the router
    path('', include(router.urls)),
]
