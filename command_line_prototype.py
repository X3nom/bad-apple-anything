import cv2,os,time

video_path = r'.\data\【東方】Bad Apple!! ＰＶ【影絵】.mp4'
cap = cv2.VideoCapture(video_path)
success, image = cap.read()
count = 0
row = ''
while success:

  os.system('cls')
  count += 1
  for x in range(0,36-1):
    print(row)
    row = ''
    for y in range(0,22-1):
      v = cv2.resize(image,(22,36))[x, y]
      if v[0] == 0:
        row += '     '
      elif v[0] == 255:
        row += '#####'
      else:
        row += '+++++'
  success, image = cap.read()
cap.release()
cv2.destroyAllWindows()