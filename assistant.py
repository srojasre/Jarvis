from voice_rec import Speak, Voice
from openai import OpenAI
from config import *
class Jarvis:
    def __init__(self, model, name="Javrvis",system="You are Jarvis") -> None:
        self.name = name
        self.system = system
        self.model  = model
        self.jarvis = OpenAI()

        speaker_model = 'tts-1'
        voice_record_model = 'whisper-1'
        self.speaker = Speak(model=speaker_model, file_path='prueba01' ).setup()
        self.voice_record = Voice(model=voice_record_model, file='prueba01').setup()
        
        
    def setup(self):
        self.jarvis.api_key = API_KEY
        
        
        
    def createAssistant(self):
        assistant = self.jarvis.beta.assistants.create(name=self.name,
                                           instructions=self.system,
                                           tools='UNDEFINE',
                                           model=self.model
        )
        
        return assistant
        
    def createThread(self):
        thread = self.jarvis.beta.threads.create()
        
        message = self.jarvis.beta.threads.messages.create(thread_id=thread.id,
                                                           role='user',
                                                           content='UNDEFINE')
        
        
        
    
        