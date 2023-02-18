import cv2,os,time
# generate ascii version of bad apple in real time
video_path = r'.\data\【東方】Bad Apple!! ＰＶ【影絵】.mp4'
cap = cv2.VideoCapture(video_path)
success, image = cap.read() #get frame
row = ''
size = [36,22]
time_offset = 0.001
last_frame_time = 0
while success:
  resizedImage = cv2.resize(image,(size[1],size[0])) #resize frame to fit command line
  if time.time()-last_frame_time < 0.03:
    time.sleep(0.03-(time.time()-last_frame_time))
  last_frame_time = time.time()
  os.system('cls')
  for x in range(0,size[0]-1):
    print(row)
    row = ''
    for y in range(0,size[1]-1):
      v = resizedImage[x, y] #pick value of  pixel
      if v[0] == 0:
        row += '     '
      elif v[0] == 255:
        row += '#####'
      elif v[0] < 128:
        row += ' ... '
      else:
        row += '+++++'
  success, image = cap.read() #get frame
cap.release()
cv2.destroyAllWindows()