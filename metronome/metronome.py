import pika
import time
import playsound
# Let's do this simple at first

time_grid = [None] * 64 # Breaking down the metronome into small units of time
for i in range(0, len(time_grid), 1):
    if (i%8) == 0:
        time_grid[i] = 2
    if (i%32) == 0:
        time_grid[i] = 1
# Fuck it, I'm going to do this in go.
index = 0
print(time_grid)
while True:
    if time_grid[index%len(time_grid)] == 1:
        playsound.playsound("./samples/metronome.mp3", False)
    elif time_grid[index%len(time_grid)] == 2:
        playsound.playsound("./samples/metronome_soft.mp3", False)
    index+=1
    time.sleep(0.125/4)
    

