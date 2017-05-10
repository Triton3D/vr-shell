##import cv2
##DEV = 0
##
##if __name__ =='__main__':
##    cv2.namedWindow('Camera',cv2.WINDOW_AUTOSIZE)
##    capture=cv2.VideoCapture(0)
##    key=''
##    while key!='q':
##        
##        gray=cv2.cvtColor(1,cv2.COLOR_BAYER_BG2BGR)
##        cv2.imshow('frame',gray)
##        
##        key=cv2.waitKey()
##    capture.release()
##    cv2.destroyAllWindows()    
####    highgui.cvNamedWindow('Camera',highgui.CV_WINDOW_AUTOSIZE)
####    highgui.cvMoveWindow('Camera',10,10)
####    capture=highgui.cvCreateCameraCapture(DEV)
####    key=''
####    while key !='q':
####        frame=highgui.cvQueryFrame(capture)
####        highgui.cvShowImage('Camera',frame)
####        key=highguicv.WaitKey(5)
####
##

import cv2

# Camera 0 is the integrated web cam on my netbook
camera_port = 0

#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

# Captures a single image from the camera and returns it in PIL format
def get_image():
# read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im

    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in xrange(ramp_frames):
        temp = get_image()
        print("Taking image...")
        # Take the actual image we want to keep
        camera_capture = get_image()
        file = "c:/1.png"
        # A nice feature of the imwrite method is that it will automatically choose the
        # correct format based on the file extension you provide. Convenient!
        cv2.imwrite(file, camera_capture)
    
    # You'll want to release the camera, otherwise you won't be able to create a new
    # capture object until your script exits
    del(camera)
