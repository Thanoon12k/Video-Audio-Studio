import os
from moviepy.editor import VideoFileClip

def extractAudioFromVideo(video_file_path:str)->str:
    try:
        file_name_without_ext, _ = os.path.splitext(video_file_path)
        out_audio_path = os.path.join('studio', f"{file_name_without_ext}.mp3")
   
        video_clip = VideoFileClip(video_file_path)
        
        # Extract audio from the video
        audio_clip = video_clip.audio
        
        # Define the output audio file path
        
        # Write the audio file to the defined path in the best quality
        audio_clip.write_audiofile(out_audio_path, codec='mp3', bitrate='320k')
        
        # Close the clips to release their resources
        audio_clip.close()
        video_clip.close()
        
        # Return the path of the audio file
        return out_audio_path
    except Exception as e:
        return f"error happend-> {e}"
# Example usage:

if __name__ == '__main__':
    audio_path = extractAudioFromVideo('C:/Users/msr/Desktop/images/videos/20240501_101859.mp4')
    print(f'Audio file saved to: {audio_path}')
