import pika
import time
import playsound
# Let's do this simple at first

time_grid = [None] * 64 # Breaking down the metronome into small units of time
for i in range(0, len(time_grid), 1):
    if (i%8) == 0:
        time_grid[i] = 1

index = 0
while True:
    index+=1
    if time_grid[index%len(time_grid)]:
        playsound.playsound("./samples/metronome.mp3")
    time.sleep(0.125)

