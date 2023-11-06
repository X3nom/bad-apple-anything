import cv2,os,time
# webcam to ascii
# Works best with VScode terminal
characters = r"  `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
#characters = characters[::-1]

video_path = 0#r'.\data\【東方】Bad Apple!! ＰＶ【影絵】.mp4'

cap = cv2.VideoCapture(video_path)
success, image = cap.read() #get frame
row = ''
size = [60,240] #set size
frame_rate_divisor = 1 # set to 2 or more if video runs too slow, scales down framerate
time_offset = 0.001
last_frame_time = 0
while success:
  image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  resizedImage = cv2.resize(image,(size[1],size[0])) #resize frame to fit command line
  frame = ""#'\033[H \033[2J'
  for x in range(0,size[0]-1):
    frame += "\n"
    for y in range(0,size[1]-1):
      v = resizedImage[x, y] #pick value of  pixel
      for i in range(1):
        frame += characters[(int((len(characters)-1)*v/255))]
  time_between_frames = time.time()-last_frame_time
  if time_between_frames < 0.03:
    time.sleep(0.03-time_between_frames) # wait if frame rate is higher than 30fps
  last_frame_time = time.time()
  os.system('cls')
  print(frame)
  cv2.imshow("oo",image)
  cv2.waitKey(1)
  for i in range(frame_rate_divisor):
    success, image = cap.read() #get frame
cap.release()
cv2.destroyAllWindows()