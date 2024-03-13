import cv2
import numpy as np
import matplotlib.pyplot as plt
# Wczytanie obrazu
image_path = "rozmyte.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Wyświetlenie obrazu
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.show()

# Dyskretna transformaty Fouriera (DFT)
dft = np.fft.fft2(image)
dft_shift = np.fft.fftshift(dft)
# Wyświetlenie widma częstotliwościowego
magnitude_spectrum = 20 * np.log(np.abs(dft_shift))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.axis('off')
plt.show()


# Tworzenie maski dolnoprzepustowej
rows, cols = image.shape
crow, ccol = rows // 4, cols // 4
mask = np.zeros((rows, cols), np.uint8)
r = 800
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 10
# Filtracja w dziedzinie częstotliwości
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_filtered = np.fft.ifft2(f_ishift)
img_filtered = np.abs(img_filtered)
# Wyświetlenie obrazu po filtracji
plt.imshow(img_filtered, cmap='gray')
plt.title('Image after Filtering')
plt.axis('off')
plt.show()

