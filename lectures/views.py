from django.http import HttpResponse
from django.template import loader
from .models import Lectures

def home(request):
  lectures = Lectures.objects.all().values()
  template = loader.get_template('home_page.html')
  context = {
    'lectures': lectures,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  lectures = Lectures.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'lectures': lectures,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())