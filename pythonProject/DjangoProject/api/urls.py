from django.urls import include, path
from rest_framework import routers
from api.views import PersonViewSet, SpeciesViewSet
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

router = routers.DefaultRouter()
router.register('people', PersonViewSet)
router.register('species', SpeciesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('^connection/',TemplateView.as_view(template_name = 'login.html')),
    path('acc_formdata/',views.LoginForm, name ='login'),
    path('Loginform/',views.LoginForm, name ='login')
]
