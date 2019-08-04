#Two-dimensional Fourier Transform 
import cv2
import numpy as np

img = cv2.imread('mill.jpg',0)
scaled = cv2.resize(img, dsize=(150, 150))
f = np.fft.fft2(scaled)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
magnitude_spectrum = magnitude_spectrum.astype(np.uint8)
height, width = scaled.shape
mask = np.zeros((height, width)) #マスク
ifimage = np.zeros((height, width),dtype=complex) 
IFFT2 = np.fft.ifftshift(ifimage) #逆フーリエ変換後の画像 
IFFT2 =np.fft.ifft2(IFFT2)
IFFT2 = IFFT2.real
Sin = np.zeros((height, width),dtype=complex) #クリックした場所のサイン波

# マウスイベント時に処理を行う
def mouse_event(event, x, y, flags, param):
    global mask, ifimage, IFFT2, Sin
    if flags == cv2.EVENT_LBUTTONDOWN:
        if(y>height):
            y = height-1
        if(y<0):
            y = 0
        if(x>width):
            x = width-1
        if(x<0):
            x = 0
        mask[y, x] = 1
        #ifimage = mask*fshift
        ifimage[y, x] = fshift[y, x]
        IFFT2 = np.fft.ifftshift(ifimage)
        IFFT2 = np.fft.ifft2(IFFT2)
        IFFT2 = IFFT2.real
        SinCoordinate = np.zeros((height, width),dtype=complex)
        SinCoordinate[y, x] = fshift[y, x]
        Sin = np.fft.ifftshift(SinCoordinate)

while (True):
    cv2.imshow("Input Image", scaled)
    cv2.imshow("Magnitude Spectrum", magnitude_spectrum)
    cv2.imshow("ifft2", IFFT2.astype(np.uint8))
    cv2.imshow("mask", mask)
    cv2.imshow("sin", np.fft.ifft2(Sin).real)
    cv2.setMouseCallback("mask", mouse_event)
    #ESCキーで終了
    if cv2.waitKey(1) & 0xFF == 27:
        break
 
cv2.destroyAllWindows()