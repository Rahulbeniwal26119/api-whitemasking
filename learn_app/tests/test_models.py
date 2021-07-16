from learn_app.models import Dull
from mixer.backend.django import mixer 
import pytest 


@pytest.mark.django_db
class TestModels:

    def test_is_name_valid(self):
        # product = Dull.objects.create("Rahul Beniwal", "Hey Rahul Beniwal Here")
        product = mixer.blend("learn_app.Dull", name="Rahul Beniwal", description="Say Hello")
        assert product.is_name_valid == True

    def test_is_name_invalid(self):
        product = mixer.blend("learn_app.Dull", name="Rahu6l Beniwal", description="Say Hello")
        assert product.is_name_valid  == False