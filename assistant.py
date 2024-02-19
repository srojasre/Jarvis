from voice_rec import Speak, Voice
from openai import OpenAI
from config import *
class Jarvis:
    """
    Jarvis class is the mains assitant of the project called Jarvis 
    
    *** createAssistant:
    *** createThread:
    *** triggerThread:
    *** listen:
    *** speak:
    *** proccesCommand:
    *** start:
    """ 
    #More detail info into update 5
    def __init__(self, model, name="Jarvis",system="You are Jarvis") -> None:
        self.name = name
        self.system = system
        self.model  = model
        self.jarvis = OpenAI()

        speaker_model = 'tts-1'
        voice_record_model = 'whisper-1'
        self.speaker = Speak(model=speaker_model, file_path='prueba01' )
        self.voice_record = Voice(model=voice_record_model, file='prueba01')
        
        
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
        
        return thread
    
    def triggerThread(self, thread, assistant):
        self.jarvis.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        
    def listen(self):
        text = self.voice_record.voiceTranslation()
        
        return text
    
    def speak(self, message):
        self.speaker.voiceSpeaker(message, 'test01')
        
    def proccesComand(self, text, assitant): # not finish #TODO
        pass
    
    def start(self):
        command = self.listen()
        assistant = self.createAssistant()
        
        thread = self.createThread() # Thread creator
        self.triggerThread(thread, assistant)
        
        response = self.proccesComand(command, assitant=assistant)
        self.speak(response)
        
        
        
    
        