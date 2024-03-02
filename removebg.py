#Not working RN
from rembg import remove
from PIL import Image
input_path = 'raw.jpeg'
output_path = 'bgremoved.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
