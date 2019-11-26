# IN DEVELOPMENT DO NOT USE YET

from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4 
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
import time

RATIO = 12.0 / 36.0  
LIMIT = 25 
EXTRA = 0.03

button = Button()
sound = Sound()
grabm = MediumMotor(OUTPUT_A)
liftm = LargeMotor(OUTPUT_B)
basem = LargeMotor(OUTPUT_C)
touch = TouchSensor(INPUT_1)
color = ColorSensor(INPUT_3)


def init():
  color.mode = "COL-REFLECT"
  
  liftm.reset()
  liftm.stop_action = "hold"
  liftm.polarity = "inversed"
  liftm.run_forever(speed_sp = 450)
  while color.value(0) < LIMIT:
    pass
  liftm.stop()

  grabm.reset()
  grabm.stop_action = "hold"
  grabm.run_forever(speed_sp = 400)
  time.sleep(1)
  pos = int(grabm.count_per_rot * -0.25)
  grabm.run_to_rel_pos(speed_sp = 600, position_sp = pos)
  
  basem.reset()
  basem.stop_action = "hold"
  basem.run_forever(speed_sp = 450)
  while not touch.value(0):
    pass
  basem.stop() 
  pos = int(basem.count_per_rot * (0.25 + EXTRA) / RATIO)
  basem.position = pos
  basem.run_to_abs_pos(speed_sp = 450, position_sp = 0)
  while "holding" not in basem.state:
    pass

  sound.speak("Ready!")


def move(direction):
  pos = int(basem.count_per_rot * (0.25 + EXTRA) / RATIO)
  base_motor.run_to_abs_pos(position_sp = direction * pos)
  while "holding" not in basem.state:
    pass

  pos = int(liftm.count_per_rot * 280.0 / 360.0)
  liftm.run_to_rel_pos(speed_sp = 180, position_sp = -pos)
  while "holding" not in liftm.state:
    pass

  grabm.run_forever(speed_sp = 360)
  time.sleep(1)
  grabm.stop()

  liftm.run_forever(speed_sp = 500)
  while color.value(0) < LIMIT:
    pass
  liftm.stop()

  basem.run_to_abs_pos(position_sp = 0)
  while "holding" not in basem.state:
    pass

  pos = int(liftm.count_per_rot * 280.0 / 360.0)
  liftm.run_to_rel_pos(speed_sp = 180, position_sp = -pos)
  while "holding" not in liftm.state:
    pass

  pos = int(grabm.count_per_rot * 0.25)
  grabm.run_to_rel_pos(speed_sp = 360, position_sp = -pos)
  while "holding" not in grabm.state:
    pass

  liftm.run_forever(speed_sp = 500)
  while color.value(0) < LIMIT:
    pass
  liftm.stop()


def stop():
  color.mode = "COL-AMBIENT"
  grabm.reset()
  liftm.reset()
  basem.reset()


if __name__ == "__main__":
  init()
  try:
    while "backspace" not in button.buttons_pressed:
      if button.up:
        sound.speak("Right!")
        move(1)
      if button.down:
        sound.speak("Left!")
        move(-1)
      time.sleep(0.1)
  except KeyboardInterrupt:
    pass
  stop()
  sound.speak("Goodbye!").wait()
