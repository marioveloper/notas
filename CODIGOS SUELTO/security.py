'''
    estas a cargo de la seguridad de un casino
    hay un ladron tratando de robarse el dinero
    mira a traves de los diagramas de seguridad para estar seguro
    que siempre tienes bajo custodia el dinero

    pregunta:  evalua una puerta dada del casino para determinar
    si hay alguien q posee dinero guardad y el ladron

    entrada: un string q incluye
    $(dinero)
    T(ladron)
    G(guardia)
    espacio en la puerta del casino q no esta ocupado el dinero,
    ladron o guardia se representa con x

    'ALARM' si el dinero esta en peligro
    'quiet' si el deniero esta a salvo

    ej: xxxxxGxx$xxxT
    ej: ALARM

    suena la alarma xq no hay guardia entre el ladron y el din
'''
import re
text = 'xxxxxGxx$xxxTxxxx$'
text = text.replace('$', 'D')
patron1 = r'(.)*D(x)*T'
patron2 = r'(.)*T(x)*D'
print(re.match(patron2, text))