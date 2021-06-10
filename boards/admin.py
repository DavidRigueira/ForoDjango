from django.contrib import admin

from .models import Board, Post, Topic, Category, Points

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(Points)
