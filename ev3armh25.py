from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C 
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
import time

BASE_GEAR_RATIO = 12.0 / 36.0  
LIFT_ARM_LIMIT = 25 
BASE_EXTRA = 0.03


def init():
  global button
  global sound
  global grab_motor
  global lift_motor
  global base_motor
  global base_limit_sensor
  global lift_limit_sensor

  button = Button()
  sound = Sound()

  grab_motor = MediumMotor(OUTPUT_A)
  lift_motor = LargeMotor(OUTPUT_B)
  base_motor = LargeMotor(OUTPUT_C)

  base_limit_sensor = TouchSensor()
  lift_limit_sensor = ColorSensor()

  lift_limit_sensor.mode = "COL-REFLECT"
  lift_motor.reset()
  lift_motor.stop_action = "hold"
  lift_motor.polarity = "inversed"
  lift_motor.run_forever(speed_sp=450)
  while lift_limit_sensor.value(0) < LIFT_ARM_LIMIT:
    pass
  lift_motor.stop()

  grab_motor.reset()
  grab_motor.stop_action = "hold"
  grab_motor.run_forever(speed_sp=400)
  time.sleep(1)
  pos = int(grab_motor.count_per_rot * -0.25)  # 90 degrees
  grab_motor.run_to_rel_pos(speed_sp=600, position_sp=pos)
  
  base_motor.reset()
  base_motor.stop_action = "hold"
  base_motor.run_forever(speed_sp=450)
  while not base_limit_sensor.value(0):
    pass
  base_motor.stop()
  pos = int(base_motor.count_per_rot * (0.25 + BASE_EXTRA) / BASE_GEAR_RATIO)
  base_motor.position = pos
  base_motor.run_to_abs_pos(speed_sp=450, position_sp=0)
  while "holding" not in base_motor.state:
    pass

  sound.speak("Ready!")


def move(direction):
  global grab_motor
  global lift_motor
  global base_motor
  global lift_limit_sensor

  pos = int(base_motor.count_per_rot * (0.25 + BASE_EXTRA) / BASE_GEAR_RATIO)
  base_motor.run_to_abs_pos(position_sp=direction * pos)
  while "holding" not in base_motor.state:
    pass

  pos = int(lift_motor.count_per_rot * 280.0 / 360.0)
  lift_motor.run_to_rel_pos(speed_sp=180, position_sp=-pos)
  while "holding" not in lift_motor.state:
    pass

  grab_motor.run_forever(speed_sp=360)
  time.sleep(1)
  grab_motor.stop()

  lift_motor.run_forever(speed_sp=500)
  while lift_limit_sensor.value(0) < LIFT_ARM_LIMIT:
    pass
  lift_motor.stop()

  base_motor.run_to_abs_pos(position_sp=0)
  while "holding" not in base_motor.state:
    pass

  pos = int(lift_motor.count_per_rot * 280.0 / 360.0)
  lift_motor.run_to_rel_pos(speed_sp=180, position_sp=-pos)
  while "holding" not in lift_motor.state:
    pass

  pos = int(grab_motor.count_per_rot * 0.25)
  grab_motor.run_to_rel_pos(speed_sp=360, position_sp=-pos)
  while "holding" not in grab_motor.state:
    pass

  lift_motor.run_forever(speed_sp=500)
  while lift_limit_sensor.value(0) < LIFT_ARM_LIMIT:
    pass
  lift_motor.stop()


def stop():
  global lift_limit_sensor
  global grab_motor
  global lift_motor
  global base_motor

  lift_limit_sensor.mode = "COL-AMBIENT"
  grab_motor.reset()
  lift_motor.reset()
  base_motor.reset()


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
