import array
import math
import wave

# TODO: Merge duplicate consecutive notes. Instead of [A, B, B, B, C], should be [A, B*3, C] to mitigate "popping" sound
# Or make sure that we end each note on a sample that's pretty much "at zero".
# that happens N times per second where N is the frequency if tge current note = I can just wait for the next full cyckle== and keep appending data untul then, shoukd be negib=gake

def writeSongFile(filename, sequence, notes_per_sec = 1):

   f = wave.open(filename, 'wb')

   NUM_CHANNELS = 1
   SAMPLE_WIDTH = 2
   FRAME_RATE = 40000

   MAX_POS_VALUE = (2 ** ((SAMPLE_WIDTH * 8)-1)) -1
   
   duration = 1/notes_per_sec
   
  
   
   f.setnchannels(NUM_CHANNELS)
   #Set the number of channels.
   f.setsampwidth(SAMPLE_WIDTH)
   #Set the sample width to n bytes.
   f.setframerate(FRAME_RATE)
   #Set the frame rate to n.
   #f.setnframes(DURATION * FRAME_RATE * len(sequence))
   #Set the number of frames to n. This will be changed later if more frames are written.
   #f.setcomptype(type, name)
   #Set the compression type and description. At the moment, only compression type NONE is supported, meaning no compression.

   for frequency in sequence:
      num_frames = int(duration * FRAME_RATE)
      modulo = int((1/frequency) * FRAME_RATE)
      extra = num_frames % modulo
      num_frames -= extra
   
      samples = [int(MAX_POS_VALUE * math.sin(2 * math.pi * frequency * sample_num/FRAME_RATE)) for sample_num in range(num_frames)]
      data = array.array('h')
      for sample in samples:
         data.append(sample)  
      f.writeframes(data.tostring())
   #Write audio frames and make sure nframes is correct.
   f.close()
