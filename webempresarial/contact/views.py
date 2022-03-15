from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')

            # enviamos el correo y lo redireccionamos
            email = EmailMessage(
                #asunto,
                "La Caffettiera: Nuevo Mensaje de contacto"
                #cuerpo,
                'De {} <{}>\n\n{}'.format(name,email,content),
                #email_origen,
                'no-contestar@inbox.mailtrap.io',
                #email_destino,
                ['prueba123@hotmail.com'],
                #reply_to[email]
                reply_to=[email]

            )

            try:
                email.send()
                # en el caso de que haya salido todo bien, redireccionamos a OK
                return redirect(reverse('contact')+'?ok')
            except:
                # en el caso de que haya salido todo mal, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')


            

    return render(request, "contact/contact.html",{'form': contact_form})
