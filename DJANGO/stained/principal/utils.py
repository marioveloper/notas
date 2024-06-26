import uuid

def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")[:12]
    return code

def generate_rank(referrals):
    if referrals < 20:
        rank = 'Sin rango'
    elif referrals < 40:
        rank = 'perla'
    elif referrals < 80:
        rank = 'perlaII'
    elif referrals < 120:
        rank = 'Zafiro'
    elif referrals < 160:
        rank = 'ZafiroII'
    elif referrals < 200:
        rank = 'Rubi'
    elif referrals < 240:
        rank = 'RubiII'
    elif referrals < 500:
        rank = 'Esmeralda'
    elif referrals < 750:
        rank = 'EsmeraldaII'
    elif referrals < 1000:
        rank = 'Diamante'
    else:
        rank = 'DiamanteII'
    return rank

def calculate_points(referrals):
    puntos = referrals*3
    return puntos

def fecha_final(f_inicio):
    fin = datetime.timedelta(days = 30)
    return f_inicio + fin