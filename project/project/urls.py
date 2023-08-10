from django.contrib import admin
from django.urls import path, include
from project.views import Home

urlpatterns = [
    path("", Home.as_view(), name="App Name"),
    path("admin/", admin.site.urls),
    path("notes", include("demo.urls")),
]
