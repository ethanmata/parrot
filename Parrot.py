import FrequencyFinder
import WaveFileGenerator
import MarkovModel
from gooey import Gooey,GooeyParser

@Gooey()
def main():
   
   parser = GooeyParser(description="A Clever Musical Machine")
   parser.add_argument(dest='ifname',metavar="Input File", widget="FileChooser",action="store")
   parser.add_argument(dest='chainlength',metavar="Chain Length",default=1,help="Markov analysis chain length",action="store")
   parser.add_argument(dest='islices',metavar="Input Slices",default=8,help="Slices per second for input music",action="store")
   parser.add_argument(dest='ofname',metavar="Output File", default="output.wav", action="store")
   parser.add_argument(dest='oslices',metavar="Output Slices",default=8,help="Slices per second for output music",action="store")
   parser.add_argument(dest='sequence_length',metavar="Sequence Length",default=100,help="Number of notes in generated song",action="store")
   args = parser.parse_args()


   # TODO: Add cleaner error handling
   ifname = args.ifname
   ofname = args.ofname
   chainlength = int(args.chainlength)
   islices = int(args.islices)
   oslices = int(args.oslices)
   sequence_length = int(args.sequence_length)

   mm = MarkovModel.ComplexMarkovModel(chainlength)

   print("Reading file...")
   data = FrequencyFinder.analyze_song(ifname,islices,snapmode="hard")
   print("Done. ({} samples recorded.)".format(len(data)))

   print("Generating Markov Model...")
   mm.parseTokens(data)

   print("Creating sequence...")
   sequence = mm.createSequence(sequence_length)
   print("Done. ({} notes created)".format(len(sequence)))


   print("Generating file...")
   WaveFileGenerator.writeSongFile(ofname, sequence, oslices)
   print("Done.")


if __name__ == '__main__':
  main()
