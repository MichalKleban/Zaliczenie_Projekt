from unicodedata import name
from PIL import Image
import math


#program ma na celu przeanalizowanie zdjęcia pod kątem jego zaciemnienienia i przedstawienia tego w skali od 1-100 odpowiednio 1 oznacza bardzo jasne zdjęcie
#a 100 bardzo ciemne

class Photo():
    def __init__(self, path):
        self.img=Image.open(f"photo/{path}") 

#za pomocą konstruktora program wczytuje zdjęcie z wcześniej przygotowanego folderu

    def analizer(self):
        result=0
        suma=0
        for pixel in iter(self.img.getdata()):
            suma+=1
            result+=100-math.ceil((0.2126*pixel[0])+(0.7152*pixel[1])+(0.0722*pixel[2]))/2.55
            final=result/suma
        return math.ceil(final)
        
#za pomocą funkcji analizer zdjęcie zostaje rozłożone na pixele a także każdy z nich zostaje przeanalizowany pod kątem  barw opisanych
#parametrami RGBA zgodnie ze wzorem zbliżającym widok ludzkiego oka na taną barwę przykładowo ludzkie oko mocniej widzi barwy zielone niż czerwone
#w tym celu każdy z parametrów ma inny zapis przy przeliczeniu w rezultacie funkcja zwraca nam wynik w skali od 1 do 100

    def dark_or_bright(self):
        name=""
        if photo.analizer()<40:
            name="bright"
        elif photo.analizer()>=40 and photo.analizer()<=60:
            name="disputed"
        else:
            name="dark"
        return name

#za pomocą funkcji dark_or_bright program przypisuje dane zdjęcie do jego nazwy i stopnia "ciemności"

    def photo_convert(self, path):
        img = Image.open(f"photo/{path}")
        width, heigt=img.size
        new_img=img.resize((int(640), int(360)))
        if photo.dark_or_bright()=="bright":    
            convert_img = new_img.save(f"bright_photos/{photo.dark_or_bright()}{photo.analizer()}.jpg")
        elif photo.dark_or_bright()=="disputed":
            convert_img = new_img.save(f"disputed_photos/{photo.dark_or_bright()}{photo.analizer()}.jpg")
        else:
            convert_img = new_img.save(f"dark_photos/{photo.dark_or_bright()}{photo.analizer()}.jpg")

#za pomocą funkcji photo_convert program zmienia rozdzielczość każdego zdjęcia na jednakową a także zmienia nazwę zdjęciom,
#oraz zmienia ich lokalizację do odpowienich folderów (bright, disputed, dark)

for i in range(10,11):
    photo=Photo(f"p{i}.jpg")
    print(photo.analizer())
    photo.photo_convert(f"p{i}.jpg")
    