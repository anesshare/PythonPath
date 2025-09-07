import time
import datetime
import pygame
def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    soundFile = "sound.mp3"
    isRunning = True
    while isRunning:
        currTime = datetime.datetime.now().strftime("%H:%M:%S") #UZIMAMO TRENUTNO VREME
        print(currTime)
        time.sleep(1) #DA ISPISUJE SVAKU SEKUNDU
        if currTime == alarm_time:
             print("WAKE UPP!!!!")
             pygame.mixer.init() #Konstruktor za ovaj mixer
             pygame.mixer.music.load(soundFile) #Dodajemo soundfile na ovja mixer
             pygame.mixer.music.play()
             while pygame.mixer.music.get_busy():
                time.sleep(1)
                isRunning = False
           

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ") #UBACUJEMO ZELJENO VREME 
    set_alarm(alarm_time)