from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('myapp.urls')),
    path('api', include('api.urls')),
    path('api/account', include('accounts.urls')),
    path('users/', include('users.urls'))

]
