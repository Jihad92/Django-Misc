from django.contrib import admin

from .models import Movie, SearchTerm, Genre
# Register your models here.


admin.site.register([
    Movie, SearchTerm, Genre
])