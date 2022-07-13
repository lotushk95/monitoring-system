import os

SAVEDIR = '/home/pi/ex7'

def camera():
    
    filename = SAVEDIR + '/face.jpg'
    
    command = 'fswebcam -r 320x240 -d /dev/video0 ' + filename
    os.system(command)
    
    os.system('sync')
    
    return filename

'''
test code
if __name__ == '__main__':
    camera()
'''