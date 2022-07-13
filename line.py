import requests

line_notify_token = 'clZ01XUGBZRv3BR3WvzNRdy5X5DLdkT4sUtzUtX3hz8'
url = 'https://notify-api.line.me/api/notify'

def send_message(notification_message):
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    message = {'message': f'{notification_message}'}
    requests.post(url, headers = headers, data = message)

def send_message_and_image(notification_message, notification_image):

    headers = {'Authorization': f'Bearer {line_notify_token}'}
    message = {'message': f'{notification_message}'}
    files = {'imageFile': open(notification_image, 'rb')}
    requests.post(url, headers = headers, data = message, files = files)
 
'''
test code
if __name__ == '__main__':
    send_message_and_image('Hello World!', 'face.jpg')
'''

