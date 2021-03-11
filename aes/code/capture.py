
# Setup scope and target
########################################
# ANCHOR: setup
import chipwhisperer as cw

# Setup a connection with the CW board
# and fetch the scope for using this board.
scope = cw.scope()

# The default settings are fine for now.
scope.default_setup()

# Fetch the target from the scope
# This should be automatically connected
target = cw.target(scope)
# ANCHOR_END: setup
########################################


# Reprogram the target
########################################
# ANCHOR: program
from chipwhisperer.capture.api.programmers import STM32FProgrammer
import os

# Initiate a new STM32F Program
# STM32 being the ARM microcontroller that we are using
# https://en.wikipedia.org/wiki/STM32#STM32_F3
program = STM32FProgrammer

# Get the path to the current folder
# Adjust accordingly
aes_firmware_dir = os.path.dirname(os.path.realpath(__file__))
aes_hex_path = os.path.join(aes_firmware_dir, r"simpleserial-aes-CWLITEARM.hex")

# Apply the program to the actual target
# This allows us to run the hex code on the microcontroller
cw.program_target(scope, program, aes_hex_path)
# ANCHOR_END: program
########################################
