# Alarm Clock

import time
import datetime
import pygame
import os

def set_alarm(alarm_time):
  print(f"Alarm set for {alarm_time}")
  sound_file = "my_music.mp3"
  
  if not os.path.exists(sound_file):
    print(f"Error: Sound file '{sound_file}' not found.")
    return
  
  pygame.mixer.init()
  
  try:
    while True:
      current_time = datetime.datetime.now().strftime("%H:%M:%S")
      print(current_time)
      
      if current_time == alarm_time:
        print("🔔 WAKE UP! ⏰")
        
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
          time.sleep(1)
        
        break
      
      time.sleep(1)
  except KeyboardInterrupt:
    print("You stopped the alarm 😃. You are awake!")
  finally:
    pygame.mixer.quit()
    
def validate_time_input(user_input):
  try:
    if len(user_input) == 5:  
      datetime.datetime.strptime(user_input, "%H:%M")
      return user_input + ":00"
    elif len(user_input) == 8:
      datetime.datetime.strptime(user_input, "%H:%M:%S")
      return user_input
    else:
      raise ValueError
  except ValueError:
    print("Invalid time format. Please enter the alarm time (HH:MM or HH:MM:SS).")

if __name__ == "__main__":
  while True:
    alarm_time = input("Enter the alarm time (HH:MM or HH:MM:SS): ")
    alarm_time = validate_time_input(alarm_time)
    if alarm_time:
      set_alarm(alarm_time)
      break

