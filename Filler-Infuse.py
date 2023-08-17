#!/usr/bin/env python3

"""
FillerInfuse

Este script toma el canal alfa de la imagen que le pasen como primer argumento y el color en hexadecimal o una imagen en segundo argumento y rellena el fondo de la imagen con ese color o imagen. Si el segundo argumento es una imagen JPG u otro formato, la convertirá a PNG antes de usarla como fondo.

Ejemplo de uso: python3 Filler-Infuse.py imagen.png FFFFFF
                python3 Filler-Infuse.py imagen.png fondo.jpg

Autor: 4DRIAN0RTIZ
Versión: 1.0.0
Fecha: 16-08-2023
"""

import re
import sys
from PIL import Image

def fill_image_with_color(image_path, background_color_hex):
    try:
        # Abrir la imagen
        image = Image.open(image_path)

        # Verificar si el color hexadecimal es válido
        if re.match(r'^(?:#)?(?:[0-9a-fA-F]{3}){1,2}$', background_color_hex):
            # Eliminar "#" si está presente en el código de color
            background_color_hex = background_color_hex.lstrip("#")
            # Convertir el color hexadecimal a una tupla RGB
            background_color_rgb = tuple(int(background_color_hex[i:i+2], 16) for i in (0, 2, 4))

            # Verificar si la imagen tiene un canal alfa adecuado
            if image.mode not in ('RGBA', 'LA') and (image.mode != 'P' or 'transparency' not in image.info):
                print('La imagen no tiene canal alfa. Asegúrate de que la imagen es PNG con transparencia.')
                sys.exit()

            # Obtener el canal alfa de la imagen
            alpha_channel = image.split()[-1]

            # Crear una nueva imagen rellenada con el color y la imagen original
            filled_image = Image.new('RGB', image.size, background_color_rgb)
            filled_image.paste(image, mask=alpha_channel)

            result_path = "resultado.png"
            filled_image.save(result_path)
            print("Imagen rellenada con el color", background_color_hex, "y guardada con éxito en", result_path)
        else:
            print("El segundo argumento no es un color hexadecimal válido.")
    except Exception as e:
        print(f"Error: {e}")

def convert_image_to_png(input_path, output_path):
    try:
        # Abrir la imagen y convertirla a PNG
        img = Image.open(input_path)
        img.save(output_path, "PNG")
        print("Imagen convertida a png de manera correcta")
    except Exception as e:
        print(f"Error al convertir la imagen a PNG: {e}")
        sys.exit()

def overlay_images_with_transparency(front_image_path, background_image_path, output_path):
    try:
        # Abrir las imágenes de primer plano y fondo
        front_image = Image.open(front_image_path)
        background_image = Image.open(background_image_path)

        # Crear una nueva imagen en blanco con canal alfa
        merged_image = Image.new("RGBA", front_image.size, (0, 0, 0, 0))

        # Pegar la imagen de fondo en la imagen en blanco
        merged_image.paste(background_image, (0, 0))

        # Pegar la imagen frontal con transparencia
        merged_image.paste(front_image, (0, 0), front_image)

        # Guardar la imagen resultante
        merged_image.save(output_path, format="PNG")
        print("Imágenes combinadas y guardadas con éxito en", output_path)
    except Exception as e:
        print(f"Error: {e}")

def fill_image_background(image_path, background_path):
    try:
        # Abrir la imagen
        image = Image.open(image_path)

        # Verificar si el fondo es una imagen JPG
        if background_path.lower().endswith('.jpg'):
            background_png_path = "background.png"
            # Convertir la imagen de fondo a PNG
            convert_image_to_png(background_path, background_png_path)
            # Combinar la imagen de primer plano con el fondo convertido
            overlay_images_with_transparency(image_path, background_png_path, "resultado.png")
        else:
            # Combinar la imagen de primer plano con el fondo proporcionado
            overlay_images_with_transparency(image_path, background_path, "resultado.png")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 script.py <imagen> <color_hexadecimal_o_imagen_fondo>")
        sys.exit()

    # Obtener los caminos de las imágenes de primer plano y fondo
    image_path = sys.argv[1]
    background_path = sys.argv[2]

    # Verificar si la imagen de primer plano no es PNG y convertirla si es necesario
    if not image_path.lower().endswith('.png'):
        converted_image_path = "converted_image.png"
        convert_image_to_png(image_path, converted_image_path)
        image_path = converted_image_path

    # Verificar si el fondo es un color hexadecimal válido o una imagen
    if re.match(r'^(?:#|0x)?(?:[0-9a-fA-F]{3}){1,2}$', background_path):
        background_color = background_path
        # Rellenar la imagen con el color proporcionado
        fill_image_with_color(image_path, background_path)
    else:
        # Rellenar la imagen con el fondo proporcionado
        fill_image_background(image_path, background_path)
