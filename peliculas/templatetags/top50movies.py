from django import template

register = template.Library()

@register.filter(name='getValoracion')
def getValoracionFromDict(valoracionesDict, idMovie):
    for i in valoracionesDict:
        if i['idMovie'] == idMovie:
            return i['valoraciones']
    return 0