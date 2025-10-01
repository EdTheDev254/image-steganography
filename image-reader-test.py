import cv2

#read image
image = cv2.imread('copilot-bot.png')

#display window
display_window = 'Image Display'
cv2.namedWindow(display_window, cv2.WINDOW_NORMAL)
cv2.resizeWindow(display_window, 600, 600) 

#display image
cv2.imshow(display_window, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
