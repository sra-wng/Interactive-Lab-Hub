
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

#from typing_extensions import ParamSpecArgs
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
import qwiic_button

myButton = qwiic_button.QwiicButton()
if myButton.begin() == False:
   print("\nThe Qwiic Button isn't connected to the system. Please check your connection", file=sys.stderr)
else: 
   print("Qwiic button ready!")

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")

# Load the model
model = tensorflow.keras.models.load_model('my_keras_model.h5')
# Load Labels:
labels=[]
f = open("my_labels.txt", "r")
for line in f.readlines():
   if(len(line)<1):
      continue
   labels.append(line.split(' ')[1].strip())

slouch_tracker = []
append_flag = False
myButton.LED_off()

while(True):
   if webCam:
      ret, img = cap.read()

   rows, cols, channels = img.shape
   data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

   size = (224, 224)
   img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
   #turn the image into a numpy array
   image_array = np.asarray(img)

   # Normalize the image
   normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
   # Load the image into the array
   data[0] = normalized_image_array

   # run the inference
   prediction_probs = model.predict(data)
   prediction = np.argmax(prediction_probs)
   print("Predicted action: ",labels[prediction])
    
   if not append_flag and prediction==0: #if slouch tracker is empty and we get a slouch
      append_flag = True
   
   if append_flag:
      slouch_tracker.append(prediction)

   if len(slouch_tracker)>50:
      slouch_count = slouch_tracker.count(0)
      #check for most recent ten consecutive 'not slouching' to get out of slouch mode
      print(slouch_tracker[-4:])
      reset_slouch_flag = all(x!=0 for x in slouch_tracker[-10:])
      print('reset_slouch_flag: ', reset_slouch_flag)
      if reset_slouch_flag: # once exit slouch mode, reset
         print('Slouch tracker reset')
         myButton.LED_off()
         slouch_tracker = []
         append_flag = False
      elif (slouch_count/len(slouch_tracker) >= 0.95):
         print('Posture check!')
         myButton.LED_on(10)
    #check_water()
    
   if webCam:
      if sys.argv[-1] == "noWindow":
         cv2.imwrite('detected_out.jpg',img)
         continue
      cv2.imshow('detected (press q to quit)',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         cap.release()
         break
   else:
      break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
