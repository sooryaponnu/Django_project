# importing the render function from django.shortcuts
# the render function renders templates
from django.shortcuts import render

# this is the view that will render the index page
def homeView(request):
    return render(request, 'dictionary/index.html')

# this is the view that will render search page
def searchView(request):
    return render(request, 'dictionary/search.html')