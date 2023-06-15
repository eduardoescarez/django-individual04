from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import FormularioConsulta
from mainapp.models import FormularioContactoDB

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
        return render(request, self.template_name, {'formulario': formulario, 'titulo': 'Crear cuenta de usuario',})

    def post(self, request, *args, **kwargs):
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensajes = {'enviado': True, 'resultado': 'El usuario se ha creado correctamente'}
        else:
            mensajes = {'enviado': False, 'resultado': formulario.errors}
        return render(request, self.template_name, {'formulario': formulario, 'mensajes': mensajes, 'titulo': 'Crear cuenta de usuario',})

class ContactView(TemplateView):
    template_name = 'contactform.html'

    def get(self, request, *args, **kwargs):
        formulario = FormularioConsulta()
        return render(request, self.template_name, {'formulario': formulario, 'titulo': 'Formulario de contacto',})
    
    def post(self, request, *args, **kwargs):
        form = FormularioConsulta(request.POST)
        mensajes = {
            'enviado' : True,
            'resultado': None
        }
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            registro = FormularioContactoDB(
                nombre = nombre,
                email = email,
                asunto = asunto,
                mensaje = mensaje,
            )
            registro.save()
            mensajes = {'enviado': True, 'resultado': 'Hemos recibido el formulario correctamente, y pronto nos pondremos en contacto.', 'titulo': 'Formulario de contacto',}
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        return render(request, self.template_name, {'formulario': form, 'mensajes': mensajes, 'titulo': 'Formulario de contacto',})
