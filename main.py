import time
from pytube import YouTube

print("This is YouTube video downloader")

print("Write 1 if you want to continue.\nWrite 2 if you want to exit.")

while True:
    answer = input()
    if answer == ("1"):
        break
    elif answer == ("2"):
        print("Bye!")
        time.sleep(2)
        quit()
    else:
        print("Wrong number, try again!")
while True:
    print("Please enter the url: ")
    try:
        link = input()
        yt = YouTube(link)
        print("\nTitle: ", yt.title)
        print("Author: ", yt.author)
        print("View: ", yt.views)

        print("\nDo you want audio? 1 = yes, 2 = no.")

        while True:
            user_answer = input("")
            if user_answer == "1":
                print("Downloading...")
                yd = yt.streams.get_audio_only()
                yd.download('/Videos')
                print("Your audio has been downloaded in C:/Videos")
                time.sleep(2)
                quit()
            elif user_answer == "2":
                break

        print("Write 1 if you want to have highest resolution.\nWrite 2 If you want to have the lowest resolution.")

        while True:
            answer = input()
            if answer == ("1"):
                print("Downloading...")
                yd = yt.streams.get_highest_resolution()
                yd.download('/Videos')
                break
            elif answer == ("2"):
                print("Downloading...")
                yd = yt.streams.get_lowest_resolution()
                yd.download('/Videos')
                break
            else:
                print("Wrong number, try again!")

        print("Your video has been downloaded in C:/Videos")
        time.sleep(5)
    except:
        print("Wrong url.")
        continue
