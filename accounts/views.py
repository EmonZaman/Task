from django.contrib.auth import login
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from accounts.models import User


class LoginView(View):
    template_name = "accounts/form1.html"

    template_index = "accounts/form2.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(first_name, last_name, email, country, username, password)
        # u = User()
        # u.objects.get(username=username)
        # u.objects.get(email=email)
        # u.objects.get(password=password)
        u = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, country=country,
                                     username=username, password=password)
        u.set_password(password)
        u.save()
        login(request, u)
        return render(request, self.template_index)


class ShowView(TemplateView):
    template_name = 'accounts/form2.html'
