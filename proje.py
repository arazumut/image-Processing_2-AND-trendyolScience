import cv2
import numpy as np

# Resmi oku
image_path = 'araba.jpg'
image = cv2.imread(image_path)


if image is None:
    print(f'Hata: {image_path} dosyası okunamadı. Dosya yolunu kontrol edin.')
else:

    resized_image = cv2.resize(image, (800, 600))

   
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

  
    blurred_image = cv2.GaussianBlur(grayscale_image, (15, 15), 0)

    # Canny kenar tespiti uygula
    edges = cv2.Canny(blurred_image, 50, 150)

  
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)


    contour_image = np.zeros_like(rgb_image)
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

   
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.imshow('Canny Edges', edges)
    cv2.imshow('RGB Image', rgb_image)
    cv2.imshow('Contours', contour_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
