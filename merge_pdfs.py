from PyPDF2 import PdfMerger
from os import listdir
from os.path import isfile, join, getctime, getmtime


name_of_file = input('Please enter name of pdf you want to create: ')
# get names of all files in folder

pdfs = [fr'files_to_convert/{f}' for f in listdir('files_to_convert') if isfile(join('files_to_convert', f))]
pdfs.sort(key=getmtime)
print(pdfs)




merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(f"{name_of_file}.pdf")
merger.close()

