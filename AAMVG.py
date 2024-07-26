import mutagen
import os
import os.path
import glob
import re
from mutagen.flac import FLAC

title = "None"
artist = "None"
date = "None"
album = "None"
UploaderCommentary = input("Do you have anything to say about this upload?\n")

def videoedit():
    trackstuff = ("Track: "+tracknumber)
    command0 = f"magick \"{bg}\" -resize 2560x1440 \"{bg}\"" #Resizes the background
    command2 = f"magick \"{bg}\" -blur 0x8 ( \"{albumart}\" -resize 725x725 -border 8 -gravity center -geometry -421 ) -composite -alpha Set \"{generated}\"" #Makes the background
    command3 = f"magick \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x200 caption:\"{title}\" -gravity center -geometry +348-258 -composite -alpha Set \"{generated}\""
    command8 = f"magick \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x200 caption:\"{title}\" -gravity center -geometry +346-260 -composite -alpha Set \"{generated}\""
    command4 = f"magick \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x80 caption:\"{artist}\" -gravity center -geometry +348-88 -composite -alpha Set \"{generated}\""
    command9 = f"magick \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x80 caption:\"{artist}\" -gravity center -geometry +346-90 -composite -alpha Set \"{generated}\""
    command5 = f"magick \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x60 caption:\"{date}\" -gravity center -geometry +348+332 -composite -alpha Set \"{generated}\""
    command10 = f"magick \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x60 caption:\"{date}\" -gravity center -geometry +346+330 -composite -alpha Set \"{generated}\""
    command6 = f"magick \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x130 caption:\"{album}\" -gravity center -geometry +347+182 -composite -alpha Set \"{generated}\""
    command11 = f"magick \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x130 caption:\"{album}\" -gravity center -geometry +345+180 -composite -alpha Set \"{generated}\""
    command7 = f"magick \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x70 caption:\"{compartist}\" -gravity center -geometry +348+12 -composite -alpha Set \"{generated}\""
    command12 = f"magick \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x70 caption:\"{compartist}\" -gravity center -geometry +346+10 -composite -alpha Set \"{generated}\"" #Clusterfuck of commands, PLEASE help me fix this
    command13 = f"magick \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x70 caption:\"{trackstuff}\" -gravity center -geometry +348+240 -composite -alpha Set \"{generated}\""
    command14 = f"magick \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x70 caption:\"{trackstuff}\" -gravity center -geometry +346+238 -composite -alpha Set \"{generated}\""
    command15 = f"magick \"{generated}\" -background transparent -fill black -font \"{font}\" -size 675x90 caption:\"{artist}\" -gravity center -geometry +348-43 -composite -alpha Set \"{generated}\""
    command16 = f"magick \"{generated}\" -background transparent -fill white -font \"{font}\" -size 675x90 caption:\"{artist}\" -gravity center -geometry +346-45 -composite -alpha Set \"{generated}\""
    command = f"ffmpeg -loop 1 -framerate 60 -i \"{generated}\" -i \"{src}\" -c:v libx264 -preset veryslow -crf 0 -shortest \"{output}\" -c:a aac -b:a 256k" #Makes the video
    os.system(command0)
    os.system(command2)
    print("Finished with the background")
    os.system(command3)
    os.system(command8)
    if artist == compartist:
        print("The label and artist are the same")
        os.system(command15)
        os.system(command16)
    else:
        print("The label and artist are different")
        os.system(command4)
        os.system(command9)
        os.system(command7)
        os.system(command12)
    os.system(command5)
    os.system(command10)
    os.system(command6) #WHY?
    os.system(command11)
    os.system(command13)
    os.system(command14)
    print("Finished with the metadata on the image")
    os.system(command)
    print("Finished the video")

def descriptionwriter():
    f = open(description, "w+")
    f.write("Song info: \nTitle: "+title+"\nAlbum: "+album+"\nTrack: "+tracknumber+"\nAlbum Artist: "+artist+"\nArtist: "+compartist+"\nDate: "+date+"\nReplay Gain: "+replaygain+"\nInsert\nYour\nDescription\nHere") #Sends the info to a text file, so I only really have to do minimal work in order to publish the description
    if not UploaderCommentary:
        print("You didn't write anything under album commentary")
        return
    else:
        print("Commentary annotated")
        f.write("\nAlbum commentary: "+UploaderCommentary)
    print("Finished writing the description")
    f.close()

def GetTags(sourcePath):    
    global title
    global artist
    global date
    global album
    global compartist
    global tracknumber
    #global tracktotal
    global websites
    global replaygain
    global catalog
    fileType = os.path.splitext(sourcePath)[1]
    metadata = FLAC(sourcePath)
    title = metadata["title"][0]
    artist = metadata["artist"][0]
    compartist = metadata["artist"][0]
    date = metadata["date"][0]
    album = metadata["album"][0]
    replaygain = metadata["replaygain_track_gain"][0]
    #catalog = metadata["catalognumber"][0]
    tracknumber = metadata["tracknumber"][0]
    #tracktotal = metadata["tracktotal"][0]
    print("Finished getting tags")
        
os.chdir("./songs")
for file in glob.glob("*.flac"):
    src = file
    GetTags(src)
    mainset = tracknumber+" - "+title+" - "+album
    subset = re.sub(r"[()\"#/@;:<>{}`+=~|!?,]", "", mainset)
    output = subset+".mov"
    generated = subset+".png"
    description = subset+".txt"
    bg = "background.png"
    font = "font.ttf"
    albumart = "album.jpg"
    descriptionwriter()
    videoedit()
