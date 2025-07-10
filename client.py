# # my_server/client.py
# import os
# import socket
# import pyautogui
# import requests
# from PIL import Image
# from io import BytesIO
# import time

# def take_screenshot():
#     screenshot = pyautogui.screenshot()
#     return screenshot

# def send_screenshot_to_server(server_ip, server_port, screenshot):
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((server_ip, server_port))

#     buffer = BytesIO()
#     screenshot.save(buffer, format="JPEG")
#     img_str = buffer.getvalue()

#     client_socket.sendall(img_str)
#     client_socket.close()

# def main():
#     server_ip = '91ae-212-8-253-162.ngrok-free.app'  # Replace with your server's IP address or domain
#     server_port = 9999

#     while True:
#         screenshot = take_screenshot()
#         send_screenshot_to_server(server_ip, server_port, screenshot)
#         # Wait for a specified interval before taking the next screenshot
#         time.sleep(10)  # Adjust the interval as needed

# if __name__ == "__main__":
#     main()




import pyautogui
import requests
from io import BytesIO
import time

def take_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

def send_screenshot_to_server(server_url, screenshot):
    buffer = BytesIO()
    screenshot.save(buffer, format="JPEG")
    img_bytes = buffer.getvalue()

    files = {'file': ('screenshot.jpg', img_bytes, 'image/jpeg')}
    response = requests.post(server_url, files=files)
    return response.text

def main():
    server_url = 'http://localhost:5000/upload'  # Replace with your server URL if remote

    while True:
        screenshot = take_screenshot()
        response = send_screenshot_to_server(server_url, screenshot)
        print(response)
        time.sleep(10)

if __name__ == "__main__":
    main()



