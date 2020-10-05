from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.


class WordToPdf(View):

    def get(self, request):
        return render(request, "convert/word2pdf.html")

    def post(self, request):
        pass