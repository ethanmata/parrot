import random

"""
The MarkovModel class provides an encapsulated method of recreating
music based on the statistical pattern of frequencies, using Markov chains.

The class provides methods for parsing input dynamically, as well as creating
sequences of a given length. In order to avoid storing the entire source
sequence, the length of the Markov chains must be set when instantiating the
object.
"""

class ComplexMarkovModel:

    def __init__(self, length):


        # The data for the sequences. Each key represents a sequence, and the result
        # is a dict of the options and their count in the source sequence.
        self.mapping = {}


        # This contains the set chain length to use in the model.
        self.length = length

        # Dict for number of 'out paths' for a given key
        # This reduces the overhead for creating sequences.
        self.mappingOccurences = {};

    def parseTokens(self, token_arr):

        for index in range(len(token_arr) - self.length):

            key = str(token_arr[index:index+self.length])
            token = token_arr[index+self.length]
            if key in self.mapping.keys():  # If we've seen this key before...
                if token in self.mapping[key].keys(): # And this next token...
                    self.mapping[key][token] += 1  # Increment the two counts
                    self.mappingOccurences[key] += 1
                else:                                   # If this is a new option:
                    self.mapping[key][token] = 1   # Set the count for this options
                    self.mappingOccurences[key] += 1    # Increment the out path count
            else:                                       # If we've never seen this key before...
                self.mapping[key] = {token : 1}    # Set the intiial values.
                self.mappingOccurences[key] = 1


    def createSequence(self, seq_length):
        newSequence = []
        current = random.choice(list(self.mapping.keys()))

        for i in range(seq_length):
            if current not in self.mapping.keys():
                current = random.choice(list(self.mapping.keys()))

            selection = random.randint(0,self.mappingOccurences[current]-1)

            for option in self.mapping[current].keys():
                if selection <= 0:
                    newSequence.append(option)
                    current = str(eval(current)[1:] + [option])
                    break

                selection -= self.mapping[current][option]

        return newSequence
