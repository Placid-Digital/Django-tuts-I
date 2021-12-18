from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    # path('', include('users.urls')),
    # path('', include('shadi.urls')),
    path('api/event/', include('api.urls')),
    # path('', include('users.urls')),
    path('admin/', admin.site.urls),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
