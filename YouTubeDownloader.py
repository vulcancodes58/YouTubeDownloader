#used for special characters
import re
#used for youtube functions
import pytube

#optional tags/catagories for organization, simply input the artist's name into this list
countryLst = ['Morgan Wallen', 'Luke Combs']
rapLst = ['2Pac', 'The Notorious B.I.G.']
popLst = ['Katy Perry', 'Lorde']

# Download Video fxn.
def downloadVideo(url):
    url = f'{url}'
    youtube = pytube.YouTube(url)
    author = youtube.author
    video = youtube.streams.get_highest_resolution()

    #some of the video titles are weird while using the pytube, and this helps mitigate that
    title = re.sub(r'[^\w\-_\. ]', '_', youtube.title)

    #change this if you want different file names, I just figured this would be the best default option
    name = title + ' by ' + author
    newName = f'{name}.mp4'

    #if you don't care about the tags/catagories, then you can comment these out/modify it
    if author in countryLst:
        outputFolder = "C:/Users/paern/Videos/Country"
    elif author in rapLst:
        outputFolder = "C:/Users/paern/Videos/Rap"
    elif author in popLst:
        outputFolder = "C:/Users/paern/Videos/Pop"
    else:
        outputFolder = "C:/Users/paern/Videos"

    video.download(output_path=outputFolder, filename=newName)

# Download Audio fxn.
#essentially the exact same except for .mp3 files (audio files)
def downloadAudio(url):
    youtube = pytube.YouTube(url)
    author = youtube.author
    title = re.sub(r'[^\w\-_\. ]', '_', youtube.title)
    audio = youtube.streams.filter(only_audio = True).first()
    name = title + ' by ' + author
    newName = f'{name}.mp3'

    if author in countryLst:
        outputFolder = "C:/Users/paern/Music/Country"
    elif author in rapLst:
        outputFolder = "C:/Users/paern/Music/Rap"
    elif author in popLst:
        outputFolder = "C:/Users/paern/Music/Pop"
    else:
        outputFolder = "C:/Users/paern/Music"
    
    audio.download(output_path=outputFolder, filename=newName)