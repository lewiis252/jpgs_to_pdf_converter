from PIL import Image
from os import listdir
from os.path import isfile, join

name_of_file = input('Please enter name of pdf you want to create: ')

# get names of all files in folder

images = [fr'files_to_convert/{f}' for f in listdir('files_to_convert') if isfile(join('files_to_convert', f))]
to_convert = []

# convert images
for image in images[1:]:
    im = Image.open({image})

    to_convert.append(im.convert('RGB'))

image_1 = Image.open(images[0])
im_1 = image_1.convert('RGB')

# make pdf
im_1.save(fr'{name_of_file}.pdf', save_all=True, append_images=to_convert)

