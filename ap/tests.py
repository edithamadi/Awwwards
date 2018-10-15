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

    def test_save_method(self):
            """
            Function testing that profile is being saved
            """
            self.profile.save_profile()
            profiles = Profile.objects.all()
            self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        """
        Function testing that profile can be deleted
        """
        
        self.profile.save_profile()
        self.profile.delete_profile()

    def search_profile(self):
        """
        Function to test if one can search a profile
        """
        self.profile.search_profile()
        first_name= self.profile.search_profile(self.profile.user)
        profile = Profile.objects.get(user_id=self.profile.user)
        self.assertTrue(first_name, profile)

class ProjectsTestClass(TestCase):
    """
    Testing projects class and its functions
    """
    def setUp(self):

        self.user = User.objects.create(username='stella')
        #creating an new profile
        self.projects = Projects(landing_page_image='rock5.jpg', title='This is the title', description="this is the description",user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.projects, Projects))

    def test_save_method(self):
            """
            Function testing that projects is being saved
            """
            self.projects.save_projects()
            projects = Projects.objects.all()
            self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        """
        Function testing that projects can be deleted
        """
        
        self.projects.save_projects()
        self.projects.delete_projects()

    def search_projects(self):
            """
            Function to test if one can search a project
            """
            self.profile.search_projects()
            first_name= self.profile.search_projects(self.projects.user)
            projects = Projects.objects.get(user_id=self.projects.user)
            self.assertTrue(first_name, projects)


