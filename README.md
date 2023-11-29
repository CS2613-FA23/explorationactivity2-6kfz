# YT Processor


## Description

YT Processor is a Python command-line utility that provides a versatile interface for downloading YouTube videos and playlists with the YouTube API through the PyTube library, allowing users to either edit video files or convert them to MP3 audio format, great for getting music or videos on an old obsolete iPod or mp3 player. The program utilizes the PyTube library for downloading YouTube content and MoviePy for video editing and audio conversion.

## Getting Started

### Dependencies

* Minimum requirements: Windows 10, [Python 2.7](https://www.python.org/download/releases/2.7/) ([Python 3.12](https://www.python.org/downloads/) is recommended)
* Additional requirements: [pip](https://pip.pypa.io/en/stable/) (easiest way to install MoviePy + PyTube) 
 ```pip install moviepy   ```and  ```pip install pytube```


### Executing program

* After downloading open your terminal and open the directory containing ytp.py, then run
```
python ytp.py
```
* You'll be first greeted with the following message. In our example lets choose '2' (a folder in your user folder labeled 'output' will appear, this is where all the processed data will be stored for you)
```
Would you like to (1) Download and edit a YouTube video or (2) Download and convert a video or playlist to mp3? (Type '1' or '2'):
```
* Next we'll have to give the program a youtube URL. This can be either a single video or a playlist. (playlists that contain hidden entries will not process)
* Let's use 'https://youtu.be/pNF8qHThGP4'
```
Enter the YouTube video or playlist URL:
```

* A loading bar should then appear showing the download status, then the conversion status:
```
Downloading Wet Hands Minecraft Remix: 100%|██████████████████████████████████████| 3.66M/3.66M [00:02<00:00, 1.43MB/s]
```
* The program should then give you the directory to where the files were saved.
```
Video(s) downloaded and converted to MP3. Files saved to C:\Users\rusty\output
```
* A full run of the program should look like this (with more loading bars if you downloaded a whole playlists)
```
PS C:\Users\rusty\Documents> python ytp.py
Would you like to (1) Download and edit a YouTube video or (2) Download and convert a video or playlist to mp3? (Type '1' or '2'): 2
Enter the YouTube video or playlist URL: https://youtu.be/pNF8qHThGP4
Downloading Wet Hands Minecraft Remix: 100%|██████████████████████████████████████| 3.66M/3.66M [00:02<00:00, 1.43MB/s]
MoviePy - Writing audio in C:\Users\rusty\output\Wet Hands Minecraft Remix.mp3
MoviePy - Done.
Video(s) downloaded and converted to MP3. Files saved to C:\Users\rusty\output
```

### Example

We start with this video:

[![](https://img.youtube.com/vi/pNF8qHThGP4/0.jpg)](https://youtu.be/pNF8qHThGP4)

Run the program like we did before


And we get this:

![](https://media.discordapp.net/attachments/627221397806120961/1179182461821927455/image.png?ex=6578da3f&is=6566653f&hm=3abfeee9717ebe40b2986083b9ae9a09ea115d1ed6992f36554c7e2fd9bae4e9&=&format=webp&width=141&height=25)

## Note
When using the video function (option 1) the steps are nearly identical until after you input your link, [this](https://github.com/CS2613-FA23/explorationactivity1-6kfz) has instructions on how to edit and process the videos (Quick Clip Editor)

## Help

* If you run into: 

```
module 'PIL.Image' has no attribute 'ANTIALIAS'
```
when trying to run refer to [this](https://github.com/Zulko/moviepy/issues/2002) for help

* If the program hangs or stalls make sure to check for unavailable tracks in the playlist

## Authors

Rusty Harker  
@6kfz (Discord)




## Acknowledgments

* [MoviePy Documentation](https://zulko.github.io/moviepy/)
* [zip() code snippets](https://www.geeksforgeeks.org/zip-in-python/)
* [Python OS Module Documentation](https://docs.python.org/3/library/os.html)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PyTube Documentation](https://pytube.io/en/latest/api.html)
