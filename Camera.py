import os
import cv2
from picamera2 import Picamera2
from PIL import Image
from datetime import date

class Camera:
    picam = Picamera2()

    def __init__(self, shotWidth=1640, shotHeight=1232, frames=33):
        self.shotWidth = shotWidth;
        self.shotHeight = shotHeight;
        self.frames = frames * 1010;        # Converting frames to hz
        self.makeDefaultConfig()
    
    def makeDefaultConfig(self):
        self.picam_config = self.picam.create_video_configuration(
            main={
                "format": "BGR888",
                "size": (self.shotWidth, self.shotHeight)
            }
        )
        self.picam_config['controls']['FrameDurationLimits'] = (self.frames, self.frames)
        self.picam_config['controls']['NoiseReductionMode'] = 1
        
    def configure(self):
        ''' Define Picamera2 configuration & User defined settings '''
        print("[*] Starting Picamera2 configuration method")
        self.picam.configure(self.picam_config)



    def startPlateCapture(self, trapNum):
        ''' PiCamera2 frame capture loop with Opencv2 image interface '''
        self.trapNum = trapNum

        # Start picamera
        self.picam.start()
            
        # Data capture array
        c = 1
        self.imageIdCount = 1

        # Getting numpy image array from camera module
        img = self.picam.capture_array()

        self.imageShot(img)
        self.picam.stop() # Closing camera to open again
    


    def imageShot(self, img):
        ''' Take a image shot from opencv camera module (picamera numpy array)
            @arg img ==> Numpy array
        '''
            # Get image from frame numpy array
        img_conv = Image.fromarray(img)
        
        
        
        # Saving image file (original)
        img_string = ("imagem", self.trapNum, "-", self.imageIdCount)
        img_string_png = img_string + ".png"

        
        #Change Directory
        directory = os.path.abspath("../img")
        img_conv.save(os.path.join(directory, img_string_png))
        self.imageIdCount+=1



        # Image cropping object
        mid_img = 608 / 2
        img_crop = cv2.imread(os.path.join(directory, img_string_png))
        print("[*] Cropping image '" + img_string_png + "'...\n", img_crop.shape)

        # Image dimensions
        height, width, c = img_crop.shape
        print("\theight:" + str(height/2) + "\n\twidth:" + str(width/2))

        # Cropping data shape
        img_cropped = img_crop[(int)(height/2 - mid_img):(int) (height/2 + mid_img), (int)(width/2 - mid_img): (int) (width/2 + 304)]
        img_cropped_name = img_string + "_cropped.jpg"
        
        cv2.imwrite(os.path.join(directory, img_cropped_name), img_cropped)
        print("[*] Image Successfully Cropped!")