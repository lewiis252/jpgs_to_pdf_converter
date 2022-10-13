from PIL import Image
from os import listdir
from os.path import isfile, join

rotate_rate = int(input('Please enter degree of rotate (integer): '))
name_of_file = input('Please enter name of pdf you want to create: ')

# get names of all files in folder

images = [f for f in listdir('files_to_convert') if isfile(join('files_to_convert', f))]
to_convert = []

# convert images
for image in images[1:]:
    im = Image.open(fr'files_to_convert\{image}')
    im = im.rotate(rotate_rate) # rotate image if needed

    to_convert.append(im.convert('RGB'))

image_1 = Image.open(fr'files_to_convert\{images[0]}').rotate(rotate_rate)
im_1 = image_1.convert('RGB')

# make pdf
im_1.save(fr'{name_of_file}.pdf', save_all=True, append_images=to_convert)
