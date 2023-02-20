import cv2,os,time,discord

token = 'bot token' #set token!

client = discord.Client()

@client.event
async def on_ready():
    print("logged in")
@client.event
async def on_message(message):
    if message.content == 'bad apple': # start by sending 'bad apple' to discord channel
        await message.channel.send('BadApple') # sends it's own message
    if message.content == 'BadApple' and message.author == client.user : # if message is it's own then start playing
        # generate ascii version of bad apple in real time
        video_path = r'.\data\【東方】Bad Apple!! ＰＶ【影絵】.mp4'
        cap = cv2.VideoCapture(video_path)
        success, image = cap.read() #get frame
        count = 0
        size = [13,20] #set size
        frame_rate_divisor = 29 # set to 2 or more if video runs too slow, scales down framerate
        time_offset = 0.001
        last_frame_time = 0
        while success:
            print(count)
            count += frame_rate_divisor
            resizedImage = cv2.resize(image,(size[1],size[0])) #resize frame to fit command line
            frame = ''
            for x in range(0,size[0]-1):
              frame += "\n"
              for y in range(0,size[1]-1):
                v = resizedImage[x, y] #pick value of  pixel
                if v[0] == 0:
                  frame += '  '
                elif v[0] == 255:
                  frame += '##'
                elif v[0] < 128:
                  frame += '..'
                else:
                  frame += '++'
            time_between_frames = time.time()-last_frame_time
            if time_between_frames < 1:
              time.sleep(1-time_between_frames) # wait if frame rate is higher than 1fps (the best discord message edit rate can do)
            last_frame_time = time.time()
            await message.edit(content='`'+frame+'`')
            for i in range(frame_rate_divisor):
              success, image = cap.read() #get frame
        cap.release()
        cv2.destroyAllWindows()

client.run(token)