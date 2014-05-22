# -*- coding: utf-8 -*-

'''
Lightweight profiling tool to detect performance BottleNecks in Python code.

Please see full description here:
https://github.com/denis-ryzhkov/bn/blob/master/README.md

bn version 0.1.5
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### import

from collections import defaultdict
from time import time

#### Bn

class Bn(object):

    def __init__(self, total_key='TOTAL', format='{key}={seconds:.4f}', sep=', '):
        self.stats = defaultdict(int)
        self.time = 0
        self.key = None
        self.total_key = total_key
        self.format = format
        self.sep = sep

    def __call__(self, key=None):
        now = time()
        if self.key:
            seconds = now - self.time
            for stats_key in self.key, self.total_key:
                self.stats[stats_key] += seconds
        self.time = now
        self.key = key

    @property
    def total(self):
        self() # Save last seconds.
        return self.stats[self.total_key]

    def __str__(self):
        self() # Save last seconds.
        return self.sep.join(
            self.format.format(seconds=seconds, key=key)
            for key, seconds in
            sorted(self.stats.iteritems(), key=lambda (key, seconds): -seconds)
        )

    def reset(self):
        self.__init__()

#### global bn

bn = Bn()

#### test

def test():

    import re
    from time import sleep
    bn = Bn()

    bn('loop')
    for item in xrange(10):

        bn('rabbit')
        sleep(0.1)

        bn('turtle')
        sleep(0.2)

        bn('loop')

    if bn.total > 1.0:
        print(bn) # logging.info(bn)
        # Microseconds may differ:
        # TOTAL=3.0053, turtle=2.0030, rabbit=1.0019, loop=0.0004

    # But seconds are OK to test.
    assert 2 < bn.total < 4, bn.total
    result = re.sub(r'\.\d{4}', '.0123', str(bn))
    assert result == 'TOTAL=3.0123, turtle=2.0123, rabbit=1.0123, loop=0.0123', result

    print('OK')

if __name__ == '__main__':
    test()
