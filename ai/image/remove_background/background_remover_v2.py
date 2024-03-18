from PIL import Image
from rembg import remove

input_path = 'images/hasbackground/m3-canva-logo.png_cropped.png'
output_path = 'images/nobackground/rmbg_m3-canva-logo.png_cropped.png'
print('Input:', input_path)

# Open the image file
with Image.open(input_path) as img:
    # Resize the image
    img = img.resize((500, 500))

    # Convert the image to PNG format
    img = img.convert('RGBA')

    # Save the preprocessed image to a temporary file
    img.save('temp.png')

# Open the preprocessed image file
with open('temp.png', 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

def auto_crop(image_path, output_path):
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        gray_img = img.convert('L')

        # Use the `getbbox` method to get the bounding box of the non-zero regions in the image
        bbox = gray_img.getbbox()

        # Crop the image with the bounding box
        cropped_img = img.crop(bbox)

        # Save the cropped image
        cropped_img.save(output_path + '_cropped.png')
        
auto_crop(output_path, output_path)