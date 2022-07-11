from django.shortcuts import render

from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        pass


class TestView(View):
    def get(self, request):
        return render(request, 'test.html')