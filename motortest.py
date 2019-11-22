#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

m = LargeMotor(OUTPUT_A)
m.on_for_rotations(SpeedPercent(75), 5)
