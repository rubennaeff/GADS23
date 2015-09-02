#!/usr/local/bin/python
from mrjob.job import MRJob
import itertools

# ex1 - word count
class MRWC(MRJob):

    def mapper(self, _, line):

        # print mapper input
        # print line

        for word in line.split():
            # print mapper output
            # print word, 1
            yield word, 1

    def reducer(self, word, counts):

        # print reducer input
        # note - counts is a generator object, so we need to do some fancy
        #        stuff to copy it (otherwise it's only good for a single use)
        # tmp1, tmp2 = itertools.tee(counts)
        # print word, [k for k in tmp1]
        # yield word, sum(tmp2)

        yield word, sum(counts)

# ex 2 - inverted index
# note - applying this twice gives the identity transformation
class MRInvIdx(MRJob):

    def mapper(self, _, line):
        usr, locs = line.split()
        for loc in locs.split(','):

            # print mapper output
            # print loc, usr

            # reverse & flatten key-value relationship
            yield loc, usr

    def reducer(self, loc, usrs):

        # print reducer input
        # tmp1, tmp2 = itertools.tee(usrs)
        # print loc, [k for k in tmp1]
        # yield loc, [k for k in tmp2]

        yield loc, [k for k in usrs]

# ex 3 - chained wc job
class MRWC2(MRJob):

    # same as above
    def mapper1(self, _, line):
        for word in line.split():
            yield word, 1

    # same as above
    def reducer(self, word, counts):
        yield word, sum(counts)

    # extra step
    def mapper2(self, word, count_sum):
        if count_sum > 3:
            yield word, count_sum

    # instructions to framework on how to run chained job
    def steps(self):
        return [self.mr(mapper=self.mapper1,
                        reducer=self.reducer),
                self.mr(mapper=self.mapper2)]

if __name__ == '__main__':
    MRWC.run()
    # MRInvIdx.run()
    # MRWC2.run()
