from rembg import remove
import os

input_path = 'images/hasbackground/'
output_path = 'images/nobackground/'


# walk through input_path images and remove each of their background, save the images name as the original with 'rmbg_' at the begging of the name
with os.scandir(input_path) as entries:
    for entry in entries:
        if entry.is_file():
            with open(input_path + entry.name, 'rb') as i:
                with open(output_path + 'rmbg_' + entry.name, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)