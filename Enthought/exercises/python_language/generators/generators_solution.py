"""
Generators
----------

Generators are created by function definitions which contain one or
more yield expressions in their body.  They are a much easier way to
create iterators than by creating a class and implementing the
__iter__ and next methods manually.

In this exercise you will write generator functions that create
various iterators by using the yield expression inside a function
body.

Create generators to

1. Iterate through a file by reading N bytes at a time; i.e.::

        N = 10000
        for data in chunk_reader(file, N):
            print len(data), type(data)

   should print::

        10000 <type 'str'>
        10000 <type 'str'>
        ...
        10000 <type 'str'>
        X <type 'str'>

   where X is the last number of bytes.

2. Iterate through a sequence N-items at a time; i.e.::

        for i, j, k in grouped([1,2,3,4,5,6,7], 3):
            print i, j, k
            print "="*10

   should print (note the last number is missing)::

        1, 2, 3
        ==========
        4, 5, 6
        ==========


3. Implement "izip" based on a several input sequences; i.e.::

        list(izip(x,y,z))

   should produce the same as zip(x,y,z) so that in a for loop izip and zip
   work identically, but izip does not create an intermediate list.

"""


def chunk_reader(obj, N):
    while True:
        data = obj.read(N)
        if data == '':
            break
        else:
            yield data


def grouped(seq, N):
    for i in range(0, len(seq)-N, N):
        yield seq[i:i+N]


def izip(*args):
    iters = [iter(x) for x in args]
    # StopIteration from arg.next will terminate loop.
    while True:
        res = []
        for arg in iters:
            res.append(arg.next())
        yield tuple(res)

if __name__ == "__main__":
    from cStringIO import StringIO
    val = StringIO("3"*1000)
    N = 100
    for data in chunk_reader(val, N):
        print len(data), type(data)

    print
    print "*" * 10
    print

    seq = [1, 2, 3, 4, 5, 6, 7]
    for i, j, k in grouped(seq, 3):
        print i, j, k
        print "="*10

    print
    print "*" * 10
    print

    for i, j in izip([1, 2, 3], [4, 5]):
        print i, j
