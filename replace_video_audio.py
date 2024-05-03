import os
from moviepy.editor import VideoFileClip, AudioFileClip

def setAudioToVideo(video_file_path: str, audio_file_path: str) -> str:
    try:
        file_name_without_ext, _ = os.path.splitext(video_file_path)
        output_video_file_path = os.path.join('studio', f'{file_name_without_ext}_with_new_audio.mp4')        
        video_clip = VideoFileClip(video_file_path)
        new_audio_clip = AudioFileClip(audio_file_path)
        video_clip = video_clip.set_audio(new_audio_clip)
        video_clip.write_videofile(output_video_file_path, codec='libx264', audio_codec='aac')
        new_audio_clip.close()
        video_clip.close()
        return output_video_file_path
    except Exception as e:
        return f"An error occurred: {e}"

import subprocess

def setAudioToVideo_ffmpeg(video_file_path: str, audio_file_path: str) -> str:
    file_name_without_ext, _ = os.path.splitext(video_file_path)
    output_video_file_path = os.path.join('studio', f'{file_name_without_ext}_with_new_audio.mp4')        
    command = [
        'ffmpeg',
        '-i', video_file_path,
        '-i', audio_file_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_video_file_path
    ]
    try:
        subprocess.run(command, check=True)
        return output_video_file_path
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

# Example usage:
if __name__ == '__main__':
    video_path = 'C:/Users/msr/Desktop/images/videos/p1/v1.mp4'
    audio_path = 'C:/Users/msr/Desktop/images/videos/p1/s1.mp3'
    edited_video_path = setAudioToVideo_ffmpeg(video_path, audio_path)
    print(f'New Video With New Audio saved to: {edited_video_path}')
