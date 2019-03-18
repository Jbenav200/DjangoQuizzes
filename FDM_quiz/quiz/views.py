from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import AccessMixin


# GET -> asks for stuff
# POST -> sends you stuff
# PUT -> very specific stuff or if you are a webdev from the 1990s
# HEAD -> headers
class MainPage(AccessMixin, View):
    def get(self, request):
        return render(
            request, "main_page.html", {"name": "Euan"})
