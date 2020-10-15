import os
import pdf2image

files = os.listdir()

for item in files:

    ext = item.split('.')
    ext = ext[-1].lower()
    
    if ext == 'pdf':

        pages = pdf2image.convert_from_path(item, 500)
        filename = ''
        
        for index,page in enumerate(pages):

            fiename = str(index) + '_' + item + '.png'
            page.save(fiename,'PNG')
            print(fiename + 'is generate')
