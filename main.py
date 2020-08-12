
# Main file: Screenshot Parser

import cv2
import pytesseract
import numpy as np
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image = cv2.imread("test_image3.jpg")

x = 783
y = 310
w = 200
h = 38

jump = 56

crop_img = image[y:y+h, x:x+w]

images = {}
names = []
output_image = None
for i in range(5):
    pos = y + jump * i
    images[i] = image[pos:pos+h, x:x+w]

    scale_percent = 300  # percent of original size
    img_h, img_w, img_c = images[i].shape
    width = int(img_w * (scale_percent*3) / 100)
    height = int(img_h * scale_percent / 100)

    dim = (width, height)
    images[i] = cv2.resize(images[i], dim, interpolation=cv2.INTER_AREA)

    text = pytesseract.image_to_string(images[i])
    match = re.search("(.*)\\n", text)
    if match is not None:
        names.append(match.group(1))

    if output_image is None:
        output_image = images[i]
    else:
        output_image = np.vstack((output_image, images[i]))

for n in names:
    print(n)
cv2.imshow("output", output_image)
cv2.waitKey(0)


