"""

Make shoure pytube in your dependency if not try to download it using pip

"""
try :
    from pytube import YouTube
    from pytube import Playlist
 #   import os
    import sys
except Exception as e:
    print("Modules Error {}".format(e))




url_video= input("Paste your URL please :\t")


inp=input('Please select a number by your need \n 1 - Download video \n 2 - Download audio \n 3 - Download all playlist \n \n\n\n\n\n\n\t\t\t')

if inp == "1":
   
    try :
        ytbd= YouTube(url_video).streams.first().download()
    except Exception as e:
        print("Download Error {}".format(e))
   # print(ytbd)


if inp == "2":
    # creating YouTube object
    yt = YouTube(url_video) 

    # accessing audio streams of YouTube obj.(first one, more available)
    stream = yt.streams.filter(only_audio=True).first()
    # downloading a video would be: stream = yt.streams.first() 

    # download into working directory
    stream.download()
elif inp == "3":
    playlist = Playlist(url_video)
    c=1
    for video in playlist.videos:
        print('Downloading video number ',c) 
        try :
            video.streams.first().download()
            print('Video number ',c,'is downloaded successfully') 
        except Exception as e:
            print("Download Error",e)
        c+=1
else :
    sys.exit()