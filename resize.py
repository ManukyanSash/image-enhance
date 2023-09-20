from PIL import Image

def resizing(image, scale=4):
    with Image.open(image) as img:
        s = img.size
        new_size = tuple(x // scale for x in s)  
        resized_img = img.resize(new_size)

        resized_img.save(image)
