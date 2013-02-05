# -*- coding: utf-8 -*-

'''
Lightweight profiling tool to detect performance BottleNecks in Python code.

Please see full description here:
https://github.com/denis-ryzhkov/bn/blob/master/README.md

bn version 0.1.4
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### import

from collections import defaultdict
from time import time

#### Bn

class Bn(object):

    def __init__(self):
        self.stats = defaultdict(int)
        self.time = 0
        self.key = None
        self.total_key = 'TOTAL'
        self.format = '{seconds:>10.4f}    {key}'

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
        return self.stats[self.total_key]

    def __str__(self):
        self() # Save last seconds.
        return '\n'.join(
            self.format.format(seconds=seconds, key=key)
            for key, seconds in
            sorted(self.stats.iteritems(), key=lambda (key, seconds): -seconds)
        )

    def reset(self):
        self.__init__()

bn = Bn()

#### test

def test():

    import re
    from time import sleep

    bn('iteration')

    for item in xrange(10):

        bn('step 1')
        sleep(0.1)

        bn('step 2')
        sleep(0.2)

        bn('iteration')

    bn() # Stop tracking.

    if bn.total > 1.0:
        # logging.info(bn)
        print(bn)

    '''
    3.0053    TOTAL
    2.0030    step 2
    1.0019    step 1
    0.0004    iteration
    '''

    assert 2 < bn.total < 4

    result = re.sub(r'\.\d{4}', '.0123', str(bn))

    assert result.strip() == '''
    3.0123    TOTAL
    2.0123    step 2
    1.0123    step 1
    0.0123    iteration
    '''.strip()

    print('OK')

if __name__ == '__main__':
    test()
