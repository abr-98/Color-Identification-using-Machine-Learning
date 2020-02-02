import cv2
import numpy as np

name='images/inst_1.png'
name_ext=name[:len(name)-4]
image=cv2.imread(name)
cv2.imshow('Original Image',image)
cv2.waitKey(0)

width,hieght=image.shape[:2]
print(image.shape)
start_row,start_col=int(0),int(0)
j=0
k=1
while j<3: 
    i=0

    while i<3:
        if i==0 and j==0:
            start_col,start_row=int(0),int(0)
            end_col,end_row=int((j+1)*hieght*0.33), int((i+1)*width* 0.33)
        elif i==0 and j!=0:
            start_col,start_row=int(j*hieght*0.33), int(0)
            end_col,end_row=int((j+1)*hieght*0.33), int ((i+1)*width*0.33)
        elif i!=0 and j==0:
            start_col,start_row=int(0),int((i)*width*0.33)
            end_col,end_row=int((j+1)*hieght*0.33), int ((i+1)*width*0.33)
        else:
            start_col,start_row=int(j*hieght*0.33), int(i*width*0.33)
            end_col,end_row=int((j+1)*hieght*0.33), int((i+1)*width*0.33)
        i+=1
        cropped_im=image[start_row:end_row,start_col:end_col]
       # cv2.imshow('Cropped Image', cropped_im)
      #  cv2.waitKey(0)
        cv2.imwrite(name_ext+'_'+str(k)+'.png',cropped_im)
       # cv2.destroyAllWindows()
        k+=1
    j+=1

    

        
