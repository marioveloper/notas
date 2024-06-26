import uuid

def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")[:12]
    return code

def generate_rank(referrals):
    if referrals < 3:
        rank = 'Sin rango'
    elif referrals < 5:
        rank = 'Peon Blanco *'
    elif referrals < 10:
        rank = 'Peon Negro *'
    elif referrals < 15:
        rank = 'Peon Blanco **'
    elif referrals < 20:
        rank = 'Peon Negro **'
    elif referrals < 40:
        rank = 'Peon Blanco ***'
    elif referrals < 80:
        rank = 'Peon Negro ***'
    elif referrals < 120:
        rank = 'Torre Blanca'
    elif referrals < 160:
        rank = 'Torre Negra'
    elif referrals < 200:
        rank = 'Caballo Blanco'
    elif referrals < 240:
        rank = 'Caballo Negro'
    elif referrals < 500:
        rank = 'Alfil Blanco'
    elif referrals < 750:
        rank = 'Alfil Negro'
    elif referrals < 1000:
        rank = 'Reina Blanca'
    else:
        rank = 'Reina Negra'
    return rank
