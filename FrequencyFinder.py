import numpy as np

import NoteMapper
import WaveFileReader

# Many thanks to:
# https://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python

def analyze_song(filename, slices_per_sec, snapmode="none",threshold=5e9):
   wfr = WaveFileReader.WaveFileReader(filename)
   frate = wfr.getFrameRate()
   frame_count = wfr.getFrameCount()
   slice = int(frate / slices_per_sec) # Number of frames per section.
   results = []
   for i in range(0,frame_count,slice):
      data = wfr.getNextSamples(slice)


      w = np.fft.fft(data)
      freqs = np.fft.fftfreq(len(w))

      # Find the peak in the coefficientes
      idx = np.argmax(np.abs(w))
      # Get the frequency and level of the highest index
      freq = freqs[idx]

      # Convert to Hz based on sample rate
      freq_in_hertz = abs(freq * frate)

      # Check to see if we're snapping to the closest actual note
      if (snapmode == "soft"):
         freq_in_hertz = round(freq_in_hertz)
      if (snapmode == "hard"):
         freq_in_hertz = NoteMapper.snap_to_freq(freq_in_hertz)

      # Make sure we're over the threshold to pick up this sound
      if (w[idx] < threshold):
         results.append(float(freq_in_hertz))
      else:
         results.append(1) # If quiet or uncertain, choose no note.
   return results
