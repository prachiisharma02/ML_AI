import cv2
vid = cv2.VideoCapture(0)
while True:
    flag, img =vid.read()
    if flag:
        #Processing code
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        th,img_bw = cv2.threshold(img_gray, 100,255,cv2.THRESH_BINARY) ## capital-constant,capital camel case -class, camel case-function)
        ##print(type(img_gray))                     
        ##break          
        ##              
                                
        cv2.imshow('Preview',img_bw)
        key = cv2.waitKey(1)
        if key == ord('q'): ## press q for off the live video
            break
    else:
        print('No frame')
        break
    
cv2.destroyAllWindows()
vid.release()

