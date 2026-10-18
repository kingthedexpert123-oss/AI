import cv2
image=cv2.imread('leopard1.jfif')
cv2.nameWindow('Loaded image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('loaded image',800,500)
cv2.imshow('loaded image',image)
cv2.waitkey(0)
cv2.destroeAllWindows()
print("image dimension:{image.shape}")