from pytube import YouTube
from moviepy.editor import AudioFileClip


def download_audio(url):
    try:
        youtube = YouTube(url)
        audio = youtube.streams.filter(only_audio=True).first()
        audio.download()
        audio_file = audio.default_filename

        audio_clip = AudioFileClip(audio_file)
        audio_clip.write_audiofile(f"{audio.default_filename[:-4]}.mp3")

        audio_clip.close()
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    video_url = input("Enter the URL of the YouTube video: ")
    download_audio(video_url)

