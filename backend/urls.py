from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from todo import views                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo')     # add this

urlpatterns = [
    path('', admin.site.urls),         path('', include(router.urls))                # add this
]

admin.site.site_header = "To-Do API"
admin.site.site_title = "Devfire Labs API portal"