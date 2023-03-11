from PIL import Image


def image_resize(image_path):
    image = Image.open(image_path)
    print('images found')

    image.thumbnail((720, 433))
    image.save('image_thumbnail.jpg')
    print(image.size)  # Output: (400, 350)
