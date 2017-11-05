#!/usr/bin/env python3

import hashlib

if __name__ == '__main__':
    m = hashlib.sha256()
    print(m.update(b'Nobody inspects the spam repetition'))
    print(m.digest())
    print(m.hexdigest())
    print(m.digest_size)
    print(m.block_size)

    test1 = 'Nobody inspects the spam repetition'
    print(test1)
    encoded_test1 = test1.encode('utf-8')
    print(encoded_test1)
    decoded_test1 = encoded_test1.decode("utf-8")
    print(decoded_test1)


    """
        b before string = string.encode('utf-8')
        in order to hash a string, need to encode it first
    """