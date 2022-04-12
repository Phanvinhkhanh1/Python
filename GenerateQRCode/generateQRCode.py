import pyqrcode
from pyqrcode import QRCode

s = "https://github.com/Phanvinhkhanh1/Python"

url = pyqrcode.create(s)

url.svg("my_profile.svg",scale = 8)



