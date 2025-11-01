from pyzbar.pyzbar import decode
from PIL import Image

imagem = Image.open("uploads/image copy.png")

codigos = decode(imagem)

print(codigos)