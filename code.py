import adafruit_display_text.label
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio
import time

displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(
    width=64, height=64, bit_depth=1,
    rgb_pins=[board.MTX_R1, board.MTX_G1, board.MTX_B1, board.MTX_R2, board.MTX_G2, board.MTX_B2],
    addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC, board.MTX_ADDRD, board.MTX_ADDRE],
    clock_pin=board.MTX_CLK, latch_pin=board.MTX_LAT, output_enable_pin=board.MTX_OE)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

line1 = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0xff0000,
    text="Hello World")
line1.x = display.width
line1.y = 8

line2 = adafruit_display_text.label.Label(
    terminalio.FONT,
    color=0x0080ff,
    text="Hello to all CircuitPython contributors worldwide <3")
line2.x = display.width
line2.y = 40

g = displayio.Group()
g.append(line1)
g.append(line2)
display.root_group = g

def scroll(line):
    line.x = line.x - 1
    line_width = line.bounding_box[2]
    if line.x < -line_width:
        line.x = display.width

def reverse_scroll(line):
    line.x = line.x + 1
    line_width = line.bounding_box[2]
    if line.x >= display.width:
        line.x = -line_width

while True:
    scroll(line1)
    scroll(line2)
    display.refresh(minimum_frames_per_second=0)
    time.sleep(0.1)
