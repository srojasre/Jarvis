import tkinter as tk
from tkinter import ttk
from voice_rec import StartRecording

class Window:
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.record_controller = StartRecording('preuba01')
       
        self.root.title("AI Assistant Recorder")
        self.is_recording = False  # Stauts
        
        self.record_button = ttk.Button(self.root, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack(pady=20)
    
    def toggle_recording(self):
        """
        This function toggles the recording state. Replace print statements with the actual recording functions.
        """
        if self.is_recording:
            # Stop recording
            self.is_recording = False
            self.record_button.config(text='Start Recording')
            self.record_controller.__close__() #Functions not implemented

            
        else:
            # Start recording
            self.is_recording = True
            self.record_button.config(text='Stop Recording')
            self.record_controller.__save__(self.record_controller.record())
            
            
    def start(self):
        self.root.mainloop()
            