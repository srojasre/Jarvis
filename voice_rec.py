from openai import OpenAI
import pyaudio
import wave
from pathlib import Path
from config import *
class Voice:
    
    """
    Voice class allows to pass natural language audio and trasncript it to 
    txt format, it could also put it into Json. 
    
    ***Init: Attributes
    ***Setup: API_KEY 
    ***VoiceTranslation: TTs model of transcription
    """ 
    def __init__(self, model, file) -> None:
        self.tts_controller = OpenAI() #Model init
        self.model = model
        self.file = open(file)
        
    def setup(self):
        self.tts_controller.api_key = API_KEY
        
    def voiceTranslation(self):
        self.tts_controller.audio.transcriptions.create(
            file=self.file,
            model=self.model,
            response_format= "text"
            
        )
    
class StartRecording:
    
    """
    Start recoding class, let the program record the microphone audio
    
    *** Init: Attributes
    *** record: Start Frame capture, and mantaing the procces
    *** Save: Save frame capture
    *** Close: Stop frame capture
    """
    def __init__(self, filename, channel=1, rate=44100, frames_per_buffer=1024) -> None:
        self.filename = filename
        self.channel = channel
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self.audio_format = pyaudio.paInt16
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.audio_format,
                                      channels=self.channel,
                                      rate= self.rate,
                                      input=True,
                                      frames_per_buffer=self.frames_per_buffer)
        
        
    def record(self, duration):
        frames = []
        
        for _ in range(int(self.rate /  self.frames_per_buffer * duration)):
            data = self.stream.read(self.frames_per_buffer)
            frames.append(data)
        return frames
    
    def __save__(self, frames):
        with wave.open(self.filename, 'wb') as wf:
            wf.setnchannels(self.channel)
            wf.setsampwidth(self.audio.get_sample_size(self.audio_format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
            
            
    def __close__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
            
            
class Speak:
    
    """Speak class allow to pass a txt file to convert it into natural language voice
    using openAI tts-1 model
    
    *** Init: Atributtes
    *** nameFile: Path to store the fiel
    *** Setup: API_KEY
    *** voiceSpeaker: OpenAI tts model creation, and save file
    """
    def __init__(self, model, voice, file_path) -> None:
        self.tts_controller = OpenAI()
        self.model = model
        self.voice = voice
        self.file = file_path
        
    def nameFile(self):
        speech_file_path = Path(__file__).parent/ self.file
        
        return speech_file_path
    
    def setup(self):
        self.tts_controller.api_key = API_KEY
    
    def voiceSpeaker(self, text:str, path:function):
        
        voice = self.tts_controller.audio.speech.create(model=self.model,
                                                        voice=self.voice,
                                                        input= text
        )
        
        voice.stream_to_file(path)
        
    
    
    
        
    
        
        
            
        