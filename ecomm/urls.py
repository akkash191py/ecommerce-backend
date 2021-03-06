"""ecomm URL Configuration
"""

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/', include('products.urls')),
    path('api/', include('cart.urls')),
    path('api/accounts/', include('ecomm_auth.urls')),

]
