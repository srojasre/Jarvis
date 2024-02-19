from voice_rec import StartRecording
from assistant import Jarvis

"""
Main file
"""

def __main__ ():
    """ 
    Metodo de grabación
    recorder = StartRecording(filename='grabacion.wav')
    
    print("Grabando...")
    
    frames = recorder.record(5)
    print("Exito..")
    recorder.__save__(frames=frames)
    recorder.__close__
     """
     
     
    bot = Jarvis('gpt-3.5')
    bot.start()
    
    
    
    
    
    

if __name__ == "__main__":
    __main__()