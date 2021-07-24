import cv2

n = 20

im = cv2.imread('input/ship.jpg')
h, w, a = im.shape
h_unit = h // n; w_unit = w // n

for i in range(n):
    start_x = h_unit * i
    for j in range(n):
        #print(i, j)
        start_y = w_unit * j
        cv2.imwrite(
            'input/large_input/ship_%i_%i.jpg' % (i, j),
            im[start_x : start_x + h_unit, start_y : start_y + w_unit, :]
        )

print('Done.')
