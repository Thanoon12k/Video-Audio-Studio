from pydub import AudioSegment
import os
import math
def splitAudioFiles(audio_file_path:str, segment_duration:int)-> str:
    try:
        file_name_without_ext, _ = os.path.splitext(audio_file_path)
        segments_folder = os.path.join('studio', f"{file_name_without_ext}_segments")
        os.makedirs(segments_folder, exist_ok=True)
        
        audio = AudioSegment.from_file(audio_file_path)
        
        # Calculate the number of segments
        num_segments = math.ceil(len(audio) / (segment_duration * 1000))
        
        # Create a new folder for the segments
        
        # Split the audio and save segments
        for i in range(num_segments):
            start_time = i * segment_duration * 1000
            end_time = min((i + 1) * segment_duration * 1000, len(audio))
            segment = audio[start_time:end_time]
            segment_file_name = f"{file_name}_{format_time(start_time)}_{format_time(end_time)}.mp3"
            segment_path = os.path.join(segments_folder, segment_file_name)
            segment.export(segment_path, format="mp3")
       
        return segments_folder
    except Exception as e:
        return f"error happend-> {e}"
def format_time(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}_{int(minutes):02}_{int(seconds):02}"

if   __name__=='__main__':
    audio_path='C:/Users/msr/Desktop/images/videos/20240501_101859.mp3'
    segments_path = splitAudioFiles(audio_path, 60*30) # 300 seconds = 5 minutes
