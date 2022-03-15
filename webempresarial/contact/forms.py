from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        
        #attrs es el atributo para ingresar clases de bootstrap o de css al formulario
        attrs = {'class':'form-control','placeholder':'Escribe tu mensaje'}
    ),min_length=3,max_length=100)
    email = forms.EmailField(label = 'Email', required=True, widget=forms.EmailInput(
        attrs = {'class':'form-control','placeholder':'Escribe tu mensaje'}
    ),min_length=3,max_length=100)
    content = forms.CharField(label = 'Contenido', required=True, widget=forms.Textarea(

        # el rows es para definir el tamanio del input en lineas, en este caso su tamanio es de 3 lineas
        attrs = {'class':'form-control','rows':3,'placeholder':'Escribe tu mensaje'}
    ),min_length=10,max_length=1000)