# Watermarking Script
<img src=https://img.shields.io/github/license/pabloniklas/wm> <img src=https://img.shields.io/github/languages/top/pabloniklas/wm>

## Descripción

Este script en Python aplica una marca de agua a imágenes, con opciones para formatear las imágenes para Instagram (recortarlas a un formato cuadrado). También valida que el archivo de marca de agua exista antes de procesar las imágenes.

## Requisitos

- Python 3
- Biblioteca Pillow (`PIL`)
- Biblioteca NumPy

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install pillow numpy
```

## Uso

El script se utiliza desde la línea de comandos y acepta los siguientes argumentos:

## Argumentos

- --watermark: Ruta al archivo de la marca de agua (requerido).
- --instagram: Opcional. Si se especifica, las imágenes serán recortadas a un formato cuadrado antes de aplicar la marca de agua.
- images: Lista de archivos de imagen a los que se aplicará la marca de agua (requerido).

## Ejemplos

Aplicar una marca de agua a imágenes sin formateo para Instagram:

```bash
./your_script.py --watermark /ruta/a/tu/marca_de_agua.png imagen1.jpg imagen2.jpg
```

Aplicar una marca de agua a imágenes y formatear para Instagram (recortar a cuadrado):

```bash
./your_script.py --watermark /ruta/a/tu/marca_de_agua.png --instagram imagen1.jpg imagen2.jpg
```

## Validaciones

El script valida que el archivo de marca de agua especificado exista y sea un archivo válido. Si el archivo de marca de agua no es válido, el script imprimirá un mensaje de error y se detendrá.

## Ejecución del Script

Asegúrate de que el script tiene permisos de ejecución. Puedes hacer esto con el siguiente comando:

```bash
chmod +x your_script.py
```

Luego, ejecuta el script con los argumentos adecuados según sea necesario.

## Autor

Pablo Niklas <pablo.niklas@gmail.com>

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

### Notas sobre el README.md

1. **Descripción**: Explica brevemente qué hace el script.
2. **Requisitos**: Lista las dependencias necesarias y cómo instalarlas.
3. **Uso**: Detalla cómo usar el script, incluyendo ejemplos prácticos.
4. **Validaciones**: Menciona que el script valida el archivo de marca de agua.
5. **Ejecución del Script**: Instrucciones para asegurarse de que el script se pueda ejecutar.
6. **Autor**: Información sobre el autor.
7. **Licencia**: Menciona la licencia bajo la cual se distribuye el script.

Este README.md debería proporcionar a los usuarios toda la información que necesitan para ejecutar y entender el script.
