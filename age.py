#!/usr/bin/env python
# Years till 100
import sys

name = sys.argv[0]
age = int(sys.argv[1])
diff = 100 - age

print 'Hello', name + ', you will be 100 in', diff, 'years!'
