# Package/Library Overview

## What is PyTube?

#### Purpose
PyTube is lightweight, simple-to-use, and uses Python's built in web libraries. It's designed for allowing users to easily interact with the YouTube API in various different ways. It abstracts the complexities of interacting with YouTube's backend, making it easy for developers to integrate YouTube video downloading functionality into their Python applications.

#### How do you use it?
* ##### Get information about a specific video:
    * PyTube can retrieve various details about a specific YouTube video, including its title, author, duration in seconds, number of views, publish date, description, video ID, thumbnail URL, and available captions or subtitles. Users can access information about the video's streams. This comprehensive set of information allows developers to programmatically gather insights about YouTube videos, facilitating tasks such as content curation, analysis, or creating applications that involve working with YouTube video metadata.[here](https://pytube.io/en/latest/api.html)



*  ##### Video Filtering and Searching
    * PyTube includes functionality to search on youtube and get nearly identical results to what you would get from using the YouTube search bar. This direct search integration means you can get youtube objects and inspect their elements without needing to do any additional processing. The search feature also allows developers to grab auto-complete results for searches.[here](https://pytube.io/en/latest/api.html)

*  ##### Downloading Video Streams

    * PyTube allows developers to process and download video streams. PyTube's versatile stream management enables users to choose from a range of resolutions and formats, tailoring the download to their specific preferences. This comprehensive set of features makes PyTube an invaluable tool for tasks such as offline content storage, archival purposes, and creative projects requiring seamless YouTube video integration. [here](https://pytube.io/en/latest/api.html)

#### In Action ->

##### The video we will be using and abusing:

[![](https://img.youtube.com/vi/pNF8qHThGP4/0.jpg)](https://youtu.be/pNF8qHThGP4)

* Get the channel URL from a youtube video
```
YouTube('https://youtu.be/pNF8qHThGP4').channel_url
```
Our outout will be:

[https://www.youtube.com/channel/UC1wl01rBPVVf2bd8dAsi4pg](https://www.youtube.com/channel/UC1wl01rBPVVf2bd8dAsi4pg)

* Get the thumbnail for the video (this is really usefule for cover art)
```
YouTube('https://youtu.be/pNF8qHThGP4').thumbnail_url
```
Our output will be:

[![](https://i.ytimg.com/vi/pNF8qHThGP4/hq720.jpg)](https://i.ytimg.com/vi/pNF8qHThGP4/hq720.jpg)

* Get all general information of a video
```
YouTube('https://youtu.be/pNF8qHThGP4').streams 
```
Our output is:

```[<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="8fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001f" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">```

## My Experience

#### Why did I choose PyTube?
 I love music and love listening to it wherever I go. I have subscriptions to both Youtube Premium (rest in peace google play music my beloved) and Spotify Premium. Both services are great, but no streaming service is going to let me stream songs into the CD player in my 2004 pile of rust on wheels of a car or my 1st gen iPod touch. PyTube offers a safe solution for that. It allows you to download youtube videos, which I can then use to convert to whatever format I please without any add/virus ridden online tools. It also made the perfect addition to my previous MoviePy project :) !

 #### So, what did I learn?
 PyTube has incredible documentation found [here](https://pytube.io/en/latest/user/quickstart.html) that made it super easy to understand all the functions and how exactly they work. In using PyTube I've learned how versatile API tools can be, and how finicky and error prone they can be too if you're not careful. I'd say that this library has helped me understand better how I can use APIs to streamline and automate tasks that otherwise may be resource intensive or annoying.

 #### Final thoughts
I would absolutely recommend PyTube to anyone looking to play around with API requests and learning about how programs can interact with web content (or wants to download YouTube videos safely). PyTube is especially nice too since it doesn't require any outside dependencies (those that aren't already included with python by default) which means you don't have to worry about platform specific compatibility or any closed source code.

