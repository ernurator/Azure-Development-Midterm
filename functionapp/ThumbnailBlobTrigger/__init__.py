import io
import logging

import azure.functions as func

from PIL import Image

def generate_thumbnail(blob: func.InputStream, size=(128, 128)):
    pil_image = Image.open(blob)
    in_memory_file = io.BytesIO()
    pil_image.thumbnail(size, Image.ANTIALIAS)

    pil_image.save(in_memory_file, format=pil_image.format)
    return in_memory_file.getvalue()

def main(blobin: func.InputStream, blobout: func.Out[bytes], context: func.Context):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {blobin.name}\n"
                 f"Blob Size: {blobin.length} bytes")

    thumbnail = generate_thumbnail(blobin)
    blobout.set(thumbnail)

    logging.info(f"Thumbnail generated successfully")
