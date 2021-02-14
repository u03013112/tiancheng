from ffpyplayer.player import MediaPlayer

vid = 'rtmp://pull.dearballoon.com/live/8377911_1613266674?txSecret=4b405547606da733118c84dda81782d8&txTime=6028E705 live=1'
player = MediaPlayer(vid)
val = ''
while val != 'eof':
    frame, val = player.get_frame()
    # if val != 'eof' and frame is not None:
    #     img, t = frame
    #     print(img, t)