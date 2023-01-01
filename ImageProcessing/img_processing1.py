from PIL import Image, ImageFilter

img_bulba = Image.open('D:\IMAGE PROCESSING\images\poke_images\\bulbasaur.jpg')
print(img_bulba) #prints a PIL object

# using some basic features of Image 
print(img_bulba.format)
print(img_bulba.size)
print(img_bulba.mode)


print(dir(img_bulba))

# Image filtering
    #blurring
blur_bulba = img_bulba.filter(ImageFilter.BLUR)
#blur_bulba.save('images\\filtered_img\\blur_bulba.png')

    #smoothening
smooth_bulba = img_bulba.filter(ImageFilter.SMOOTH)
smoothm_bulba = img_bulba.filter(ImageFilter.SMOOTH_MORE) 
smooth_bulba.save('images\\filtered_img\\smooth_bulba.png')
smoothm_bulba.save('images\\filtered_img\\smoothmore_bulba.png')

# we can do a lot of other things like SHARPEN
# we can also convert to grayscale(using .convert())
# check out documentation


