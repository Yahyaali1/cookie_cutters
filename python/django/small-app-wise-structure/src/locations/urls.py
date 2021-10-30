from django.urls import path, include

app_name = 'locations'
urlpatterns = [
    path('api/', include('src.locations.api.urls'))
]
