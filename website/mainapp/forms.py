from django import forms

class FormularioConsulta(forms.Form):
    nombre = forms.CharField          (label="Nombre", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar su nombre',
                                            'max_length':' El nombre de contacto no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    email = forms.EmailField            (label="Email", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email de contacto',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control',
                                            'type':'email'})
                                        )
    asunto = forms.CharField         (label="Asunto", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el asunto',
                                            'max_length' : 'La categoría no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )
    mensaje = forms.CharField         (label="Mensaje", required = True, max_length=1000,
                                        error_messages={
                                            'required': 'Indique el mensaje',
                                            'max_length': 'El campo puede tener hasta 1000 caracteres',
                                        },
                                        widget= forms.Textarea(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )