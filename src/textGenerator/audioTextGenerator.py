import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_sentence

class TextGenerator():
    def __init__(self):
        self.r = sr.Recognizer()
    
    def generate_text(self, input_file_path, output_path):
        sound = AudioSegment.from_wav(input_file_path)
        # audio file will be broken down into chunks based on silence
        chucks = split_on_sentence(
            sound,
            min_silence_lenght = 500,
            silence_thresh = sound.dBFS - 14,
            keep_silence = 500
        )

        os.makedirs(output_path, exist_ok=True)

        text = ''
        text_dict = {}
        for i, chunk in enumerate(chucks, start=1):
            filename = os.path.join(output_path, f'chunk_{i}.wav')
            chunk.export(filename, format='wav')
            # speech to text
            with sr.AudioFile(filename) as file:
                audio_recorded = self.r.record(file)
                try:
                    textextracted = self.r.recognize_google(audio_recorded)
                except sr.UnknownValueError as e:
                    Logger.logger('ERROR', e)
                else:
                    textextracted = f'{textextracted.capitalize()}. '
                    text += textextracted
                    text_dict[filename] = textextracted
        
        return text_dict