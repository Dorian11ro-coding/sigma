import time
from selenium import webdriver
import os


def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)

    if not os.path.exists(file_path):
        file_path = input(f"Enter the full path for {filename}: ")

    return f"file:///{file_path}"


def play_video(filename, duration):
    driver = webdriver.Chrome()
    driver.maximize_window()
    video_path = get_file_path(filename)
    driver.get(video_path)
    time.sleep(duration)
    driver.quit()


def momazosdiego():
    play_video('diego.mp4', 13)


def momazospablo():
    play_video('momazos pablo.mp4', 6.5)


def momazosluis():
    play_video('Momazos Luis.mp4', 7)


def momazosjuan():
    play_video('momazos Jua.mp4', 15)


momazosdiego()
momazospablo()
momazosluis()
momazosjuan()
