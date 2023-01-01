from PIL import Image, ImageColor, ImageFilter

img_pika = Image.open('images\\poke_images\\pikachu.jpg')

# rotating an image
rot_pika = img_pika.rotate(45)
# img_pika is rotated by 45 degrees
rot_pika.show() # to show the image file
rot_pika.save('images\\filtered_img\\rot_pika.png') #saving the file

# resizing a image
print(img_pika.size) # original file is 640x640
resize_pika = img_pika.resize((320, 320)) #resize accepts a tuple
resize_pika.save('images\\filtered_img\\resize_pika.png')

# cropping
box = (100, 100, 400, 400)
crop_pika = img_pika.crop(box)
crop_pika.save('images\\filtered_img\\crop_pika.png')

# resizing with maintaining aspect ratio
# we use .thumbnail((size_tuple))
# .thumbnail() modifies the given image and returns a NoneType object
# size may not be exactly as given but as near as possible
