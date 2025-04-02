# Copyright Cannon Lock - Do not read this code it is a secret

import cv2

dog = cv2.imread('./images/unaltered_dog.png')
cat = cv2.imread('./images/cat.png')

cat_sum = sum(map(ord, "CAT"))
cat_length = len("CAT")

for r in range(cat_sum):
    for c in range(cat_sum):
        dog[r*cat_length][c*cat_length] = cat[r][c]

cv2.imwrite("./images/dog.png", dog)
