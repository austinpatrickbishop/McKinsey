#!/usr/bin/env python
# Austin Bishop 03/04/2013
import random
import numpy.random as nprnd
import timeit
import collections

num = [random.randint(0,20) for r in xrange(10000)]
# Count instances 
ct = collections.Counter(num) 
# Sort by number of instances
num = sorted(ct.items(), key=lambda item: item[1], reverse=True)
print [x[0] for x in num]
#print "Value:",["%02d" % x[0] for x in num]
#print "Freq :",["%02d" % x[1] for x in num]
#print "\n".join(str(x) for x in num)
