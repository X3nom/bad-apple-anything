import cv2,os,time
# generate ascii version of bad apple in real time
video_path = r'.\data\【東方】Bad Apple!! ＰＶ【影絵】.mp4'
cap = cv2.VideoCapture(video_path)
success, image = cap.read()
count = 0
row = ''
size = [36,22]
while success:
  resizedImage = cv2.resize(image,(size[1],size[0])) #resize frame to fit command line
  os.system('cls')
  count += 1
  for x in range(0,size[0]-1):
    print(row)
    row = ''
    for y in range(0,size[1]-1):
      v = resizedImage[x, y] #pick value of  pixel
      if v[0] == 0:
        row += '     '
      elif v[0] == 255:
        row += '#####'
      else:
        row += '+++++'
  success, image = cap.read()
cap.release()
cv2.destroyAllWindows()