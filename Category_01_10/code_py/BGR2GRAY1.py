import cv2
import numpy as np

# Gray scale
def BGR2GRAY(img):
	b = img[:, :, 0].copy()
	g = img[:, :, 1].copy()
	r = img[:, :, 2].copy()

	# Gray scale
	out = 0.2126 * r + 0.7152 * g + 0.0722 * b
	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("../hfut.jpg").astype(np.float)

# Grayscale
out = BGR2GRAY(img)

# opencv API
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Save result
# cv2.imwrite("../result_image/BGR2GRAY1.jpg", out)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
