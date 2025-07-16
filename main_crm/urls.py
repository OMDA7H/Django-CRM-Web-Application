from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webapp.urls')),
]

handeler404 = 'webapp.views.custom_page_not_found'
