from PIL import Image, ImageDraw, ImageFont

# Create a blank white image
width, height = 200, 100
image = Image.new('RGB', (width, height), color='white')

# Add text to the image
draw = ImageDraw.Draw(image)

text = "314156"

font = ImageFont.load_default()
draw.text((10, 10), text, font=font, fill='black')



# Save the image
image.save("./sample_image.png")
print("sample_image.png created successfully!")
