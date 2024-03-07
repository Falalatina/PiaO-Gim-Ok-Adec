import cv2
import numpy as np
import matplotlib.pyplot as plt
def load_image(image_path):
 """
 Wczytuje obraz z podanej ścieżki.
 Parameters:
 - file_path (str): Ścieżka do pliku obrazu.
 Returns:
 - image (numpy.ndarray): Wczytany obraz.
 """
 image = cv2.imread(image_path)
 return image
def create_damage_mask(image_shape):
 """
 Tworzy pustą maskę o wymiarach zgodnych z obrazem.
 Parameters:
 - image_shape (tuple): Kształt obrazu (wysokość, szerokość, liczba kanałów).
 Returns:
 - damage_mask (numpy.ndarray): Pusta maska uszkodzeń.
 """
 damage_mask = np.zeros(image_shape[:2], dtype=np.uint8)
 return damage_mask
def mark_damaged_areas(image, damage_mask):
 """
 Oznacza obszary uszkodzeń na obrazie na podstawie podanej maski.
 Parameters:
 - image (numpy.ndarray): Obraz do oznaczenia.
 - damage_mask (numpy.ndarray): Maska uszkodzeń.
 Returns:
 - marked_image (numpy.ndarray): Obraz z oznaczonymi uszkodzonymi obszarami.
 """
 marked_image = image.copy()
 marked_image[damage_mask > 0] = [0, 0, 255] # Oznaczenie na czerwono
 return marked_image
def restore_damaged_areas(image, damage_mask):
 """
 Przywraca uszkodzone obszary na obrazie przy użyciu inpaintingu.
 Parameters:
 - image (numpy.ndarray): Obraz z uszkodzeniami.
 - damage_mask (numpy.ndarray): Maska uszkodzeń.
 Returns:
 - restored_image (numpy.ndarray): Obraz z przywróconymi obszarami.
 """
 img = cv2.imread('maski.jpg', 0)
 type(img)

 img.shape
 

 restored_image = cv2.inpaint(image, damage_mask, inpaintRadius=10, flags=cv2.INPAINT_TELEA)
 return restored_image
def display_images(original_image, marked_image, restored_image):
 """
 Wyświetla obraz przed i po procesie restauracji.
 Parameters:
 - original_image (numpy.ndarray): Oryginalny obraz.
 - marked_image (numpy.ndarray): Obraz z oznaczonymi uszkodzonymi obszarami.
 - restored_image (numpy.ndarray): Obraz z przywróconymi obszarami.
 """
 plt.figure(figsize=(15, 5))
 plt.subplot(1, 3, 1)
 plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
 plt.title("Original Image")
 plt.axis("off")
 plt.subplot(1, 3, 2)
 plt.imshow(cv2.cvtColor(marked_image, cv2.COLOR_BGR2RGB))
 plt.title("Damaged Areas Marked")
 plt.axis("off")
 plt.subplot(1, 3, 3)
 plt.imshow(cv2.cvtColor(restored_image, cv2.COLOR_BGR2RGB))
 plt.title("Restored Image")
 plt.axis("off")
 plt.show()
# Ścieżka do pliku z obrazem starych fotografii
image_path = "stare2.jpg"
# Wczytaj obraz
old_photo = load_image(image_path)
# Stwórz maskę uszkodzeń (na razie pustą)
damage_mask = create_damage_mask(old_photo.shape)

print(damage_mask)
test = 'maski.jpg'

img = cv2.imread('maski.jpg', 0)


i = img.shape
str(i)
b = np.matrix(img)
print(b)

# Oznacz obszary uszkodzeń (interaktywne narzędzie graficzne lub ręczne zaznaczanie)
# Tutaj możesz dodać kod do interaktywnego zaznaczania obszarów na obrazie.
# Przywróć uszkodzone obszary
restored_photo = restore_damaged_areas(old_photo, b)
# Wyświetl wyniki
display_images(old_photo, mark_damaged_areas(old_photo, b), restored_photo)