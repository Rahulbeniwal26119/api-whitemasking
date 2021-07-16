from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from learn_app.views import DullView


class TestView:

    def test_product_detail_authentication(self):
        path = reverse("dull")
        request = RequestFactory().get(path)
        