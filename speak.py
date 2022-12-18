import rich
import playsound
import gtts
import misc

from gtts import gTTS
from playsound import playsound

from rich.console import Console
from rich.prompt import Prompt, Confirm

console = Console()

class Speak:

      def __init__(self):
      
          self.lang = Prompt.ask("[bold red]language?[/]", choices=["ru", "en"])
          self.text = console.input("[bold blue]text: ") 
          
          self.filename = console.input("[bold yellow]audio name: ")
          self.delay = Prompt.ask('[bold green]delay voice[/]', default="0")

          self.Voice()
          
      def Voice(self):

          format_audio = ".mp3"
          
          try:
              audio = gTTS(
                 text = self.text,
                 lang = self.lang,
                 slow = int(self.delay)       
              )
              
              audio.save(self.filename+format_audio)
              console.print(f"'{self.filename}' <- Save.")
              
          except (Exception, ConnectionError) as error:
                 console.print(
                     error,
                     style = "bold"
                 )

          finally:
                 voice = Confirm.ask("[bold red]enable audio?[/]")

                 if voice == "y":
                    os.system(f"mpv {self.filename}.mp3")

                 elif not voice:
                      console.print("https://t.me/termuxtop")
                      
Speak()            
