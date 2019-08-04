# FourierTransform  
マウスで周波数を指定し、画像のフーリエ変換・逆変換をリアルタイムに行う。  
![gif](https://user-images.githubusercontent.com/50540539/62420812-ad199380-b6d3-11e9-9277-d4e85f73141c.gif)  

# Dependency  
Python 3.6.4  
OpenCV 3.4.2  
NumPy 1.14.2  

# Usage  
mask画像で左クリックして周波数を指定することで、ifft2に逆変換後の画像が表示される。  
ESCキーで終了する。  

# References  
・フーリエ変換  
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html  
・マウスイベント  
http://rasp.hateblo.jp/entry/2016/01/24/204539  
