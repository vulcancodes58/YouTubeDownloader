#just imports the two functions
from YouTubeDownloader import *

#an infinite loop (essentially, it doesn't stop unless you type "STOP" or close the terminal window)
#if you discover a bug, and the url provided still throws out an error in the window,
#please let me know and I will try to fix it :).
while True:
    url = input("Enter url: ")
    if url == 'STOP':
        break
    else:
        try:
            #comment either out using a hashtag in front of it if you just want one or the other
            downloadVideo(url)
            downloadAudio(url)
        except:
            print("error")

