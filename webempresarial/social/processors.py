from .models import Link

# esta funcion es para extender el contexto del diccionario social
# ctx siginifica context en abreviado
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx