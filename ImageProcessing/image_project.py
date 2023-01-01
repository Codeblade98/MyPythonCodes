from sys import argv
from pathlib import Path
from PIL import Image

input_path = argv[1]
out_dir = argv[2]

try:
    p = Path(f'D:\\PYTHONCODES\\ImageProcessing\\images\\{out_dir}')
    p.mkdir()

except FileExistsError:
    print('Using the already created folder for generating output')

else:
    print('Creating a new folder of the given name')

p = Path(input_path)
count = 0
for images in p.iterdir():
    img = Image.open(images)
    count += 1
    png = img.save(f'D:\\PYTHONCODES\\ImageProcessing\\images\\{out_dir}\\converted{count}.png','png')


