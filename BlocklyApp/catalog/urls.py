from django.urls import path
from .views import BlocklyApp

urlpatterns = [
    path('', BlocklyApp, name='blockly-index')
]