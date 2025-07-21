# from yt_dlp import YoutubeDL

# def download_video(url):
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio/best',
#         'outtmpl': '%(title)s.%(ext)s',  
#         'merge_output_format': 'mp4',
#         'quiet': False
#     }

#     with YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

# url = input("Enter YouTube URL: ")
# download_video(url)
# print(" Download complete!")


from yt_dlp import YoutubeDL
import whisper
import os

# Step 1: Download the YouTube video
def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': False
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".mp4").replace(".mkv", ".mp4")
        return filename

# Step 2: Transcribe the video
def transcribe_video(video_path):
    model = whisper.load_model("base")  # or "small", "medium", "large"
    print(" Transcribing...")
    result = model.transcribe(video_path)
    print(" Transcription complete!\n")
    print(result["text"])

# Step 3: Run it all
if __name__ == "__main__":
    url = input(" Enter YouTube URL: ")
    video_path = download_video(url)
    print(f" Video downloaded: {video_path}")
    transcribe_video(video_path)
