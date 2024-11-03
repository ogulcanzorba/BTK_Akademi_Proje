from django.http import HttpResponse
from django.template import loader
from .models import Lectures
from django.shortcuts import render, get_object_or_404
from .utils import generate_response


def home(request):
  lectures = Lectures.objects.all().values()
  template = loader.get_template('home_page.html')
  context = {
    'lectures': lectures,
  }
  return HttpResponse(template.render(context, request))


# def lecture_detail(request, lecture_name):
#     lectures = get_object_or_404(Lectures, slug=lecture_name)
#     template_name = f"{lectures.slug}.html"
#     return render(request, template_name, {'lectures': lectures})

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


# def chat_with_model(request):
#     user_input = request.GET.get("input", "")
#     response = ""
#
#     if user_input:
#         response = generate_response(user_input)
#
#     return render(request, "data-structures-and-algorithms.html", {"response": response, "user_input": user_input})

def chat_with_model(request, lecture_name):
    user_input = request.GET.get("input", "")
    response = ""

    if user_input:
        response = generate_response(user_input)

    lecture = get_object_or_404(Lectures, slug=lecture_name)
    template_name = f"{lecture.slug}.html"

    return render(request, template_name, {
        "response": response,
        "user_input": user_input,
        "lecture": lecture
    })