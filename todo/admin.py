from django.contrib import admin
from .models import Todo
from django.contrib.auth.models import User

superuser = User.objects.create_superuser(
        username='luismi',
        email='luis.parent@unicaribe.edu.do',
        password='1234',
)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(Todo, TodoAdmin)

