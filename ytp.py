import os
from moviepy.editor import VideoFileClip
from pytube import YouTube, Playlist
from tqdm import tqdm
import time

def process_video(vid_input, output, start, end, resize_scale, bit_in):
    if start and end != -1:
        clip = VideoFileClip(vid_input).subclip(start, end)
        clip.resize(float(resize_scale)).write_videofile(output, fps=30, codec='libx264', bitrate=bit_in)
    else:
        clip = VideoFileClip(vid_input).resize(float(resize_scale)).write_videofile(output, fps=30, codec='libx264', bitrate=bit_in)

def download_and_convert_to_mp3(url, output_path='.'):
    try:
        if 'playlist' in url.lower():
            # If the URL is for a playlist
            playlist = Playlist(url)
            for video in tqdm(playlist.videos, desc="Downloading Playlist"):
                video_stream = video.streams.get_highest_resolution()
                with tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc=f"Downloading {video.title}") as pbar:
                    video_stream.download(output_path, filename_prefix=str(video.video_id))
                    pbar.update(video_stream.filesize)
                    video_file = os.path.join(output_path, f"{video.video_id + video.title}.mp4")

                # Wait for the file to be fully downloaded
                while not os.path.exists(video_file):
                    time.sleep(1)

                # Convert to mp3
                output_file = os.path.join(output_path, f"{video.title}.mp3")
                clip = VideoFileClip(video_file)
                audio = clip.audio
                audio.write_audiofile(output_file, codec='mp3')

                while not os.path.exists(output_file):
                    time.sleep(1)
                
        else:
            # If the URL is for a single video
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            with tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc=f"Downloading {yt.title}") as pbar:
                video_stream.download(output_path, filename_prefix=str(yt.video_id))
                pbar.update(video_stream.filesize)
                video_file = os.path.join(output_path, f"{yt.video_id + yt.title}.mp4")

            # Wait for the file to be fully downloaded
            while not os.path.exists(video_file):
                time.sleep(1)

            # Convert to mp3
            output_file = os.path.join(output_path, f"{yt.title}.mp3")
            clip = VideoFileClip(video_file)
            audio = clip.audio
            audio.write_audiofile(output_file, codec='mp3')

            while not os.path.exists( output_file):
                time.sleep(1)

        
        print(f"Video(s) downloaded and converted to MP3. Files saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main program
output_folder = os.path.expanduser("~\output")

# Create the "output" folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

operation = input("Would you like to (1) Download and edit a YouTube video or (2) Download and convert a video or playlist to mp3? (Type '1' or '2'): ")

if operation == "1":
    video_url = input("Enter the YouTube video URL: ")

    start = int(input("Please select start time (seconds): "))
    end = int(input("Please select end time (seconds): "))
    resize_scale = float(input("Type in resize scale (type 1.0 to leave as is): "))
    bit_in = input("Type in desired bitrate (e.g., 1000000 for 1mbs, none to leave unchanged): ")

    process_video(os.path.join(output_folder, f"{YouTube(video_url).video_id + YouTube(video_url).title}.mp4"), 
                   os.path.join(output_folder, f"(Edited){YouTube(video_url).title}.mp4"), 
                   start, end, resize_scale, bit_in)

elif operation == "2":
    video_url = input("Enter the YouTube video or playlist URL: ")

    download_and_convert_to_mp3(video_url, output_folder)

else:
    print("Invalid operation. Please type '1' or '2'.")
