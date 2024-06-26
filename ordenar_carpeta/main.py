import os, shutil


tipos = ['audios','documentos','fotos','videos','zips']
formatos = {
    'audios': ['mp3','mp2','opus'],
    'documentos': ['docx','xlsx','xls','pdf','vbs'],
    'fotos': ['jpg','png','gif', 'ico'],
    'videos': ['avi','mp4','mpg','mkv'],
    'zips': ['rar','zip']
}

"""crear carpetas"""
def crear_carpetas(tipos):
    for tipo in tipos:
        try:
            os.mkdir(os.getcwd()+'/'+tipo)
        except OSError as e:
            print(e)


""""mover los ficheros"""
def mover_ficheros(formatos):
    for fichero in os.listdir(os.getcwd()):
        if formatos['audios'].__contains__(fichero.split('.')[-1].lower()):
            shutil.move(os.getcwd()+'/'+fichero, os.getcwd()+'/audios')
            print(fichero)
        elif formatos['documentos'].__contains__(fichero.split('.')[-1].lower()):
            shutil.move(os.getcwd()+'/'+fichero, os.getcwd()+'/documentos')
            print(fichero)
        elif formatos['fotos'].__contains__(fichero.split('.')[-1].lower()):
            shutil.move(os.getcwd()+'/'+fichero, os.getcwd()+'/fotos')
            print(fichero)
        elif formatos['videos'].__contains__(fichero.split('.')[-1].lower()):
            shutil.move(os.getcwd()+'/'+fichero, os.getcwd()+'/videos')
            print(fichero)
        elif formatos['zips'].__contains__(fichero.split('.')[-1].lower()):
            shutil.move(os.getcwd()+'/'+fichero, os.getcwd()+'/zips')
            print(fichero)

if __name__ == '__main__':
    crear_carpetas(tipos)
    mover_ficheros(formatos)