import cv2, os
import numpy as np
import pytesseract as tsc


def sacar_texto(imagen):

    #cargar imagen y convertir a escala de grises
    ruta = 'C:\\Users\\Mario\\Desktop\\tarjeta_credito\\img\\'
    image = cv2.imread(ruta + imagen)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray', image)
    #cv2.waitKey(0)
    #thrashload para que el texto se vea blanco y el resto negro
    thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    texto = tsc.image_to_string(thresholded)

    return texto

#if __name__ == __main__():
#    print(sacar_texto(imagen))