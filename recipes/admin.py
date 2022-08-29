from django.contrib import admin
from .models import Recipe
from .models import Measure
from .models import FoodItem
from .models import Ingredient

admin.site.register(Recipe)

admin.site.register(Measure)

admin.site.register(FoodItem)

admin.site.register(Ingredient)
