from pygame import mixer
from datetime import datetime
from time import time


def music_loop(file, stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        input_of_user = input()
        if input_of_user == stop:
            mixer.music.stop()
            break


def log_file_water(msg):
    with open("water.txt", "a") as w:
        w.write(f"{msg} {datetime.now()}\n")


def log_file_eyes(msg):
    with open("eyes.txt", "a") as w:
        w.write(f"{msg} {datetime.now()}\n")


def log_file_exercise(msg):
    with open("exercise.txt", "a") as w:
        w.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    water_time = 59*60
    eyes_time = 30*60
    exercise_time = 45*60

    while True:
        if time() - init_water > water_time:
            print("Please drink some Water. Type 'done' to stop the alarm:")
            music_loop("water.mp3", "done")
            init_water = time()
            log_file_water("Drank water at")

        if time() - init_eyes > eyes_time:
            print("Eyes relaxing time. Type 'done' to stop the alarm:")
            music_loop("eyes.mp3", "done")
            init_eyes = time()
            log_file_eyes("Eyes relaxed at")

        if time() - init_exercise > exercise_time:
            print("Exercise time! Please do some exercise. Type 'done' to stop the alarm:")
            music_loop("exercise.mp3", "done")
            init_exercise = time()
            log_file_exercise("Exercise done at")

