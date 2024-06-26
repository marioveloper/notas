def encender_vela(vela):
    if vela=='encendida':
        print('la vela esta '+ vela)
    elif vela == 'apagada':
        print('la vela esta '+ vela)
        print('encendiedo....')
        vela = 'encendida'
        print('la vela esta '+ vela)
    else:
        print('no comas mierda')
vela = 'apagada'
encender_vela(vela)
