from django.test import TestCase
from .views import test_base

urlpatterns += [
    path('test/', test_base, name='test-base'),
]
