from django.shortcuts import render
from MyApp.forms import StudentForm


def home(request):
  mimi = StudentForm
  return render(request, 'index.html', {'form': mimi})
