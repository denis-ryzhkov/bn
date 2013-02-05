bn
==

Lightweight profiling tool to detect performance BottleNecks in Python code.

Hence the name: bn - BottleNeck.  
And you know keys B and N are very comfortable to type quickly in a row.

Usage:

    bn('iteration')

    for item in generator:

        bn('step 1')
        # code of step 1

        bn('step 2')
        # code of step 2

        bn('iteration')

    bn() # Stop tracking.

    if bn.total > 1.0:
        logging.info(bn)

Result:

    22.2632    TOTAL
    20.6403    step 2
     1.6209    step 1
     0.0020    iteration

Scope:

    pip install bn
    from bn import bn

    # OR:

    from bn import Bn
    def action():
        bn = Bn()

Config:

    bn.total_key = 'TOTAL'
    bn.format = '{seconds:>10.4f}    {key}'

See also: [bn.py:test()](https://github.com/denis-ryzhkov/bn/blob/master/bn.py#L58).

bn version 0.1.4  
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
