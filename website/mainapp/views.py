from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.

class IndexView(TemplateView): 
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo': 'Somos WebConstructores, tú solución de desarrollo web'},)
    
class UsersView(TemplateView):
    template_name = 'users.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users, 'titulo' : 'Usuarios'})