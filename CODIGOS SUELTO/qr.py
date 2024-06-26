import pyqrcode
from pyqrcode import QRCode

url = pyqrcode.create('http/localhost:3000')
url.svg('myweb.svg', scale=8)