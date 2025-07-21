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
from faster_whisper import WhisperModel
import os

# Step 1: Download the YouTube video
def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': False,

        # Add headers to look like a real browser
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        },

        # Optional: Add retries for reliability
        'retries': 10,
        'fragment_retries': 10,
        'continuedl': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".mp4").replace(".mkv", ".mp4")
        return filename

# Step 2: Transcribe the video using faster-whisper
def transcribe_video(video_path):
    model = WhisperModel("base", device="cpu")  # or device="cuda" for GPU
    print("Transcribing...")

    segments, _ = model.transcribe(video_path)
    transcription = " ".join(segment.text for segment in segments)

    print("Transcription complete!\n")
    print(transcription)

# Step 3: Run it all
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=DWRDNX5Mwlo"
    video_path = download_video(url)
    print(f"Video downloaded: {video_path}")
    transcribe_video(video_path)

# git add youtube_download.py
# git commit -m "Updated input URL in youtube_download.py"
# git push origin reema




