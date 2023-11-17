Como funciona?
1. en la carpeta version_a subir las imagenes de los escenarios de prueba de la version a
2. en la carpeta version_b subir las imagenes de los escenarios de prueba de la version b con los mismos nombres de los escenarios del paso 1.
3. solo acepta archivos .png o .jpg
4. intalar :
import os
import imageio
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from html import escape
con el comando pip install imageio numpy Pillow scikit-image
5. ejecutar controller.py
