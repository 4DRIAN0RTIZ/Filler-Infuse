# Filler-Infuse

Este script toma el canal alfa de la imagen que le pasen como primer argumento y el color en hexadecimal o una imagen en segundo argumento y rellena el fondo de la imagen con ese color o imagen. Si el segundo argumento es una imagen JPG u otro formato, la convierte a PNG y la escala al tamaño de la imagen de entrada antes de usarla como fondo.

## Dependencias

Este script utiliza la biblioteca Python Pillow, que se puede instalar con el siguiente comando:
```bash
pip install pillow
```

## Funcionalidades

El script proporciona las siguientes funcionalidades:

1. Rellenar una imagen con un color hexadecimal dado.
2. Rellenar una imagen con una imagen de fondo (Conversión a PNG y escalado automático).
3. Combinar imágenes con transparencia para crear una imagen final.

## Uso

Asegúrate de tener Python 3 instalado en tu sistema. Luego, ejecuta el script de la siguiente manera:
```bash
python3 Filler-Infuse.py <imagen> <color_hexadecimal_o_imagen_de_fondo>
```

- `<imagen>`: Ruta a la imagen de primer plano.
- `<color_hexadecimal_o_imagen_de_fondo>`: Color hexadecimal o ruta a la imagen de fondo.

Si proporcionas un color hexadecimal, la imagen se rellenará de ese color. Si proporcionas una imagen de fondo, la imagen de fondo se convertirá a PNG y se escalará al tamaño de la imagen de primer plano antes de rellenar la imagen de primer plano.

## Próximas funcionalidades

En un futuro, pretendo agregar al script las siguientes funcionalidades:

- [ ] Permitir escoger el tamaño de la imagen de salida.
- [ ] Hacer uso de la API de `Remove.bg` para eliminar el fondo de la imagen de primer plano de forma automática en caso de que tenga un fondo.
- [ ] Permitir ajustar la opacidad de la imagen de fondo.

## Contribuciones

Este script es un trabajo en progreso. Siéntete libre de contribuir a este proyecto. Si encuentras algún error o quieres añadir una nueva funcionalidad, puedes abrir un *issue* o enviar un *pull request*. ¡Toda ayuda es bienvenida!
