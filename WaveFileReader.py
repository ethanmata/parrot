import array
import wave


class WaveFileReader:


   def __init__(self, filename):
      self.wavefile = None
      try:
         self.wavefile = wave.open(filename)
         
      except FileNotFoundError as fnfe:
         print("Error in WaveFileReader: No file with the name '{}' was found.".format(filename))
      
   def getAllSamples(self):
      return [int.from_bytes(self.wavefile.readframes(1), byteorder='little', signed=True) for i in range(self.wavefile.getnframes())]
   
   def getNextSamples(self, num_samples):
      return [int.from_bytes(self.wavefile.readframes(1), byteorder='little', signed=True) for i in range(num_samples)]
   
   def getFrameCount(self):
      return self.wavefile.getnframes()
   
   def getFrameRate(self):
      return self.wavefile.getframerate()
   
      
