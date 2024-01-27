from rembg import remove

input_path = 'images/nobackground/rmbg_fractal.png'
output_path = 'images/nobackground/rmbg_fractal2.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)