from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
    
class CreateUsersView(TemplateView):
    template_name = 'createusers.html'

    def get(self, request, *args, **kwargs):
        formulario = UserCreationForm(request.POST)
        return render(request, self.template_name, {'formulario': formulario, 'titulo': 'Formulario de creación de usuarios',})

    def post(self, request, *args, **kwargs):
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensajes = {'enviado': True, 'resultado': 'El usuario se ha creado correctamente'}
        else:
            mensajes = {'enviado': False, 'resultado': formulario.errors}
        return render(request, self.template_name, {'formulario': formulario, 'mensajes': mensajes, 'titulo': 'Formulario de creación de usuarios',})
