from PIL import Image
img = Image.open('img.jpg')
exif_data = img._getexif()

out = open("test.txt","w")
out.write(exif_data)