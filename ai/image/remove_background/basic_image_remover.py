from rembg import remove

input_path = 'images/hasbackground/m3-gpt-logo.png'
output_path = 'images/nobackground/rmbg_m3-gpt-logo.png'
print('Input:', input_path)

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
        print('Output:', output_path)