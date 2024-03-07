import cv2
import numpy as np
import matplotlib.pyplot as plt
def restore_old_photo(image_path, mask_path):
 # Wczytaj obraz starych fotografii
 old_photo = cv2.imread(image_path)
 # Wczytaj maskę obszarów do przywrócenia (maska czarna - uszkodzone obszary)
 damaged_mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
 # Wykonaj inpainting, aby przywrócić uszkodzone obszary
 restored_photo = cv2.inpaint(old_photo, damaged_mask, inpaintRadius=3, 
flags=cv2.INPAINT_TELEA)
 # Wyświetl obraz przed i po przywracaniu
 plt.figure(figsize=(10, 5))
 plt.subplot(1, 2, 1)
 plt.imshow(cv2.cvtColor(old_photo, cv2.COLOR_BGR2RGB))
 plt.title("Old Photo")
 plt.axis("off")
 plt.subplot(1, 2, 2)
 plt.imshow(cv2.cvtColor(restored_photo, cv2.COLOR_BGR2RGB))
 plt.title("Restored Photo")
 plt.axis("off")
 plt.show()
# Ścieżki do obrazu starych fotografii i odpowiadającej mu maski
image_path = "stare2.jpg"
mask_path = "maski.jpg"
# Przywróć i popraw starą fotografię
restore_old_photo(image_path, mask_path)