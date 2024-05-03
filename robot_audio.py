from pedalboard import Pedalboard, Reverb, Chorus, Gain
from pedalboard.io import AudioFile
import numpy as np
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def apply_robotic_effect(audio_file_path, gain_db=5, chorus_params=None, reverb_params=None):
    sample_rate=0
    audio=0
    try:
        # Validate the input file path
        if not os.path.isfile(audio_file_path):
            logging.error(f"The file {audio_file_path} does not exist.")
            return None

        # Load the audio file
        with AudioFile(audio_file_path, 'r') as f:
            audio, sample_rate = f.read(f.frames)
        if audio.ndim == 2:
            # Convert to mono by averaging the channels
            audio = np.mean(audio, axis=1)
        # Create a pedalboard with a chain of effects
        print(f"ssample rate {sample_rate}")
        print(f"saudio rate {audio}")
        
        board = Pedalboard([
            Gain(gain_db=gain_db),
            Chorus() if chorus_params is None else Chorus(**chorus_params),
            Reverb(room_size=0.5) if reverb_params is None else Reverb(**reverb_params)
        ])

        # Apply the effects
        # Ensure audio is in the correct shape for processing (2D array)
        if audio.ndim == 1:
            audio = audio[:, np.newaxis]
        effected = board.process(audio, sample_rate=sample_rate)

        # Get the directory and filename
        directory = os.path.dirname(audio_file_path)
        base_name = os.path.basename(audio_file_path)
        file_name, _ = os.path.splitext(base_name)

        # Ensure the output directory exists
        output_dir = os.path.join(directory, "studio")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Construct the new filename
        new_file_path = os.path.join(output_dir, f"{file_name}_robot.mp3")

        # Write the effected audio back to a new file
        # Ensure the audio is in the correct shape for writing (2D array)
        if effected.ndim == 1:
            effected = effected[:, np.newaxis]
        with AudioFile(new_file_path, 'w', sample_rate, effected.shape[1]) as f:
            f.write(effected)

        logging.info(f"Robotic voice audio saved to: {new_file_path}")
        return new_file_path
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return None

if __name__=='__main__':
    output_path = apply_robotic_effect("C:/Users/msr/Desktop/images/videos/p1/s1.mp3")
    print(f"Robotic voice audio saved to: {output_path}")
