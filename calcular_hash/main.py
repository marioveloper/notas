import hashlib

def get_md5_file(archivo):
    """Get the MD5 hash of a file"""
    try:
        hash_md5 = hashlib.md5()
        with open(archivo, 'rb') as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hash_md5.update(bloque)
        return hash_md5.hexdigest()
    except Exception as e:
        print('Error: %s' % (e))
        return ""
    except:
        print('Error desconocido')

def get_sha256_file(archivo):
    """Get the SHA256 hash of a file"""
    try:
        hash_sha256 = hashlib.sha256()
        with open(archivo, 'rb') as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hash_sha256.update(bloque)
        return hash_sha256.hexdigest()
    except Exception as e:
        print('Error: %s' % (e))
        return ""
    except:
        print('Error desconocido')

print(get_sha256_file('url al video'))