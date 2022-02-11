
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # these two url order matters
    path('accounts/',include('accounts.urls')),
    path('', include('blog.urls')),
]
