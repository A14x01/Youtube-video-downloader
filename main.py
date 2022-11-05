import time
from pytube import YouTube

print("This is YouTube video downloader")

print("Write 1 if you want to continue.\nWrite 2 if you want to exit.")

while True:
    answer = input()
    if answer == ("1"):
        print("Please enter the url: ")
        break
    elif answer == ("2"):
        print("Bye!")
        time.sleep(2)
        exit()
    else:
        print("Wrong number, try again!")

link = input()
yt = YouTube(link)

print("Title: ", yt.title)
print("Author: ", yt.author)
print("View: ", yt.views)

print("Write 1 if you want to have highest resolution.\nWrite 2 If you want to have the lowest resolution.")

while True:
    answer = input()
    if answer == ("1"):
        yd = yt.streams.get_highest_resolution()
        yd.download('/Videos')
        break
    elif answer == ("2"):
        yd = yt.streams.get_lowest_resolution()
        yd.download('/Videos')
        break
    else:
        print("Wrong number, try again!")

print("Your video has been downloaded in C:/Videos")
time.sleep(5)