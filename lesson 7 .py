import cv2
image=cv2.imread('leapord.jfif')
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized_image=cv2.resize(grey_image,(224,224))
cv2.imshow('processed image',resized_image)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite('greyscale_resized_image.jpg',resized_image)
    print("image is saved")
else:
    print("image not saved")
cv2.destroyAllWindows()
print("processed image dimensions : {resized_image.shape}")