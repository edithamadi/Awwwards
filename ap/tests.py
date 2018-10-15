from django.test import TestCase
from .models import Profile, Projects
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    """
    Test profile class and its functions
    """
    def setUp(self):

        self.user = User.objects.create(username='stella')
        #creating an new profile
        self.profile = Profile(profile_photo='jakob.jpg', bio='This is my bio', user_contact_info="0724361712",user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

