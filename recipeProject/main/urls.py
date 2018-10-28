from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipes_index),
    path('recipes', views.recipes_list),
    path('inventory', views.inventory),
    path('recipes/<int:id>', views.recipes_detail),
    path('recipes/recommendations', views.get_recipe_recommendations),
    path('inventory/add/<int:id>', views.add_to_inventory),
    path('inventory/delete/<int:id>', views.remove_from_inventory),

]
