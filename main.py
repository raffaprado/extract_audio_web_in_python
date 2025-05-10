from moviepy.editor import VideoFileClip
import yt_dlp as youtube_dl
import requests

def download_video(url, output_path, resolution='1080p'):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': output_path.replace('.mp4', '.%(ext)s'),
        'merge_output_format': 'mp4'
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Vídeo baixado com sucesso!")
    except Exception as e:
        print("Erro ao baixar o vídeo:", e)

def extract_audio(input_video, output_audio):
    try:

        video = VideoFileClip(input_video)

        audio = video.audio


        audio.write_audiofile(output_audio)


        video.close()


        print("Áudio extraído com sucesso!")
    except Exception as e:

        print("Erro ao extrair o áudio:", e)

video_url = "https://vimeo.com/950195113"
output_video_path = "/Users/rafaelprado/Documents/videos_baixados/video_test3.mp4"
output_audio_path = "/Users/rafaelprado/Documents/audios_baixados/audio_teste1.mp3"

download_video(video_url, output_video_path)
extract_audio(output_video_path, output_audio_path)