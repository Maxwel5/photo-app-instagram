from django.test import TestCase
from .models import Profile,Image,Instagram

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.hos=Profile(photo = 'hos.jpeg', bio = 'A famous animal used for racing sports')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hos,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.hos.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
