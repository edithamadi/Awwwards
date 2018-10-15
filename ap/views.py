from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
     return render(request, 'welcome.html')

def search_results(request):

  if 'username' in request.GET and request.GET["projects"]:
      category = request.GET.get("projects")
      searched_categories = Projects.search_image(category)
      message = f"{category}"

      return render(request, 'all-ap/search.html',{"message":message,"projects": searched_categories})

  else:
      message = " Found 0 images for the search term"
      return render(request, 'all-ap/search.html',{"message":message})