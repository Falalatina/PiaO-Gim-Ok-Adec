import cv2
import numpy as np

sciezka = './stare2.jpg'

def create_mask(image):
 # Utworzenie maski - tutaj zakładamy, że obszary do przetworzenia to obszary o niskiej 
 #intensywności pikseli
 mask = cv2.inRange(image, np.array([20 ,20, 20]), np.array([100, 100, 100]))
 return mask
def eliminacja_zarysowan(obraz):
 # Zastosowanie filtra do eliminacji zarysowań (np. MedianBlur)
 obraz_wyjsciowy = cv2.medianBlur(obraz, 3)
 return obraz_wyjsciowy
def wypelnij_brakujace_fragmenty(obraz):
 # Zastosowanie algorytmu Inpainting do wypełnienia brakujących fragmentów
 maska = cv2.inRange(obraz, np.array([0, 0, 0]), np.array([70, 70, 70]))
 obraz_wyjsciowy = cv2.inpaint(obraz, maska, 3, cv2.INPAINT_TELEA)
 return obraz_wyjsciowy
def testowanie_i_ocena_skutecznosci(obraz_wejsciowy):
 # Przetestowanie narzędzia na różnych starych fotografiach
 obraz_po_elim_zarysowan = eliminacja_zarysowan(obraz_wejsciowy)
 obraz_po_wypelnieniu = wypelnij_brakujace_fragmenty(obraz_po_elim_zarysowan)
 # Wyświetlenie obrazów przed i po zastosowaniu narzędzia
#  cv2.imshow('Obraz przed', obraz_wejsciowy)
#  cv2.imshow('Obraz po eliminacji zarysowań', obraz_po_elim_zarysowan)
#  cv2.imshow('Obraz po wypełnieniu brakujących fragmentów', obraz_po_wypelnieniu)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()

def wczytaj_obraz(sciezka):
 # Wczytanie obrazu z podanej ścieżki
 obraz = cv2.imread(sciezka)
 return obraz

if __name__ == "__main__":
 # Wczytanie starej i uszkodzonej fotografii
 sciezka_do_obrazu = sciezka
 stara_fotografia = wczytaj_obraz(sciezka_do_obrazu)
 # Utworzenie maski
 maska = create_mask(stara_fotografia)
 # Ścieżka do zapisu maski
 mask_path = 'maski.jpg'
 # Zapis maski do pliku
 cv2.imwrite(mask_path, maska)
 # Testowanie i ocena skuteczności narzędzia
 testowanie_i_ocena_skutecznosci(stara_fotografia)