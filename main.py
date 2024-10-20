import time
from selenium import webdriver
import os
import platform
import urllib.parse


# Function to generate the correct file URL for both Windows and macOS
def get_file_url(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)

    if platform.system() == "Windows":
        # Convert Windows path to URL format
        file_url = f"file:///{urllib.parse.quote(file_path.replace('\\', '/'))}"
    else:
        # For macOS and Linux, just use the regular file path
        file_url = f"file:///{urllib.parse.quote(file_path)}"

    return file_url


# Helper function to play a video by filename and duration
def play_video(filename, duration):
    driver = webdriver.Chrome()
    driver.maximize_window()
    video_url = get_file_url(filename)
    driver.get(video_url)
    time.sleep(duration)
    driver.quit()


# Play different videos
def momazosdiego():
    play_video('diego.mp4', 13)


def momazospablo():
    play_video('Pablo.mp4', 6.5)


def momazosluis():
    play_video('Luis.mp4', 7)


def momazosjuan():
    play_video('Juan.mp4', 15)


# Call the functions
while True:
    momazosdiego()
    momazospablo()
    momazosluis()
    momazosjuan()

