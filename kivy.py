from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from plyer import filechooser

# Import your functions here
from audio_files_merge import mergeAudioFiles
from audio_splitter import splitAudioFiles
from video_to_audio import extractAudioFromVideo

class MainApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Video to audio conversion
        btn_video_to_audio = Button(text='Convert Video to Audio', size_hint_y=None, height=50)
        btn_video_to_audio.bind(on_release=self.convert_video)
        
        # Audio splitting
        self.input_segment_duration = TextInput(hint_text='Enter segment duration in seconds', multiline=False, size_hint_y=None, height=50)
        btn_split_audio = Button(text='Split Audio', size_hint_y=None, height=50)
        btn_split_audio.bind(on_release=self.split_audio_file)
        
        # Audio merging
        btn_merge_audio = Button(text='Merge Audio Files', size_hint_y=None, height=50)
        btn_merge_audio.bind(on_release=self.merge_audio_folder)
        
        # Adding widgets to the layout
        self.root.add_widget(btn_video_to_audio)
        self.root.add_widget(self.input_segment_duration)
        self.root.add_widget(btn_split_audio)
        self.root.add_widget(btn_merge_audio)
        
        return self.root
    
    def convert_video(self, instance):
        # Use native file chooser
        file_path = filechooser.open_file(title="Select a Video File", filters=[("Video files", "*.mp4")])
        if file_path:
            audio_path = extractAudioFromVideo(file_path[0])
            self.show_popup('Success', f'Audio file saved to: {audio_path}')
    
    def split_audio_file(self, instance):
        # Use native file chooser
        file_path = filechooser.open_file(title="Select an Audio File", filters=[("Audio files", "*.mp3")])
        if file_path:
            segment_duration = int(self.input_segment_duration.text)
            segments_path = splitAudioFiles(file_path[0], segment_duration)
            self.show_popup('Success', f'Segments saved to: {segments_path}')
    
    def merge_audio_folder(self, instance):
        # Use native folder chooser
        folder_path = filechooser.choose_dir(title="Select a Folder with Audio Files")
        if folder_path:
            merged_file_path = mergeAudioFiles(folder_path[0])
            self.show_popup('Success', f'Merged audio created: {merged_file_path}')
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    MainApp().run()
