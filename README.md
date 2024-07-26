## 2024 Update
I've co-opted this project as the old code from 2019 was a little deprecated and broken. At the moment the script still works largely the same, but the plan is to update it a little to make it a little easier to work with. I've added some details and notes at the bottom to clarify some things and help others get their videos generated a little faster.

# Album-Art-Music-Video-Generator
Python / FFMPEG / Imagemagick script to generate album art music videos using a style which I really like.
Also note that aside from this being my first published code on github, I'm still a newbie when it comes to coding, so it still looks like spaghetti.
Originally this was based on:  **[Music-Video-Generator](https://github.com/JPBotelho/Music-Video-Generator)**
But because I changed the code too much, I decided to open a new repo.

## Features
Generates a video using a set of images which are defined by the user and also writes 'some' metadata to a text file, so you can post it on a streaming website in an easy way.
Allows the user to make a commentary which will then be sent to each text file as an "album commentary:"

## Things that need help fixing:
1. There's too much code for something that *should* be a fairly simple task.
2. Imagemagick was used because I wasn't able to get FFMPEG to work based on what I wanted to do, and even still, it was done in a sloppy way because I wasn't able to separate the command into chunks, so the easiest way was to just make a bunch of commands that did work.
3. The metadata may be missing depending on whether it exists or not (obviously), but I don't really know how to write an if statement so it writes something else based on it's presence.


# Example (A slight bit deprecated but it's the general idea)
##### Here's how it will look if you've done everything right:
![9 - タイニーリトル・アジアンタム - TOHO BOSSA NOVA 2](https://user-images.githubusercontent.com/62615566/120726983-c813e500-c4af-11eb-8647-28bf46495dcf.png)
*innit cool?*

# Requirements
- FFMPEG;
- imagemagick;
- python3;
- it's also a good idea to install the requirements for python such as mutagen and glob, check the imports in renderer.py if something is amiss;

For creating the actual video, make a folder called "songs" and place the following files in it:
1. A background image named "background.png"
2. An album cover art named "album.jpg"
3. A font file named "font.ttf" (I used Mplus 1p Light)
4. The actual music files in .flac format
5. The music files *must* be tagged with certain things:
     -  Title
     -  Artist
     -  Album
     -  Track #
     -  Replaygain
     -  date

You can use a program like [mp3tag](https://www.mp3tag.de/en/) to easily add most of these tags, while replaygain is a little more difficult. [rsgain](https://github.com/complexlogic/rsgain?tab=readme-ov-file) is a good, fairly simple to use command-line tool that should write those tags for you.

The script will run a for loop until it finishes with the files, so the usual idea is to place an entire album in the folder and wait till it's done.

# Notes
- If running on Windows, Python is easily installed through the Windows store. It automatically installs the utility pip, which will let you install the needed libraries using a simple `pip install mutagen glob`.
- FFMpeg binaries can be found [here](https://www.gyan.dev/ffmpeg/builds/) for Windows. FFMpeg can be installed to an easy-to-remember location and added to the path, or else it can be added to the 'songs' folder and the script will find it there.
- Imagemagick can be found [here](https://imagemagick.org/script/download.php). Unlike FFMpeg it installs normally with an installer, so there is no need to add it to your path or to move it to the songs folder.
- The script is currently set to generate an image at 2560x1440 and a video at 60fps, this makes it take a while to generate a video but this way when the video is uploaded to Youtube it automatically uses the superior vp09 codec which saves your video from looking crunchy. This can be changed by modifying the ffmpeg command in the script and the first imagemagick command which sets a resolution for the generated composite. The original script used 1920x1080 and 1fps.
