from django.http import HttpResponse
from django.template import loader
from .models import Lectures
from django.shortcuts import render, get_object_or_404

def home(request):
  lectures = Lectures.objects.all().values()
  template = loader.get_template('home_page.html')
  context = {
    'lectures': lectures,
  }
  return HttpResponse(template.render(context, request))


def lecture_detail(request, lecture_name):
    lectures = get_object_or_404(Lectures, slug=lecture_name)
    template_name = f"{lectures.slug}.html"  # Add folder name if necessary
    return render(request, template_name, {'lectures': lectures})

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())