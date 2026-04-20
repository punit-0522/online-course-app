from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("Course App Running")


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
]