from pydub import AudioSegment
import os

def mergeAudioFiles(folder_path:str)->str:
  try:
    merged_audio = AudioSegment.empty()
    output_file_path = os.path.join('studio', 'merged_audio.mp3')

    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)
            audio_segment = AudioSegment.from_file(file_path)
            merged_audio += audio_segment
    
   
    merged_audio.export(output_file_path, format='mp3')
  
    return output_file_path
  except Exception as e:
     return f"error happend-> {e}"
if   __name__=='__main__':
    folder_path='C:/Users/msr/Desktop/images/videos/20240501_101859_segments'
    merged_file_path = mergeAudioFiles(folder_path=folder_path)
    print(f'Merged audio created : {merged_file_path}')
