from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    def get(self, request):
        templateName = "doggy.html"

        return render(request, templateName)
