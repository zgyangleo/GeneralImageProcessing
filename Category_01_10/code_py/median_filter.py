import cv2
import numpy as np


# Median filter
def median_filter(img, K_size=3):
    H, W, C = img.shape

    ## Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
    out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad+y, pad+x, c] = np.median(tmp[y:y+K_size, x:x+K_size, c])

    out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

    return out


# Read image
img = cv2.imread("../hfut_noise.jpg")


# Median Filter
out = median_filter(img, K_size=3)

# opencv API
# img = cv2.medianBlur(img,5)
# font=cv2.FONT_HERSHEY_SIMPLEX

# Save result
cv2.imwrite("../result_image/median_filter.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
