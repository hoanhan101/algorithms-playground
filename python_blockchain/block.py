import hashlib

class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def __str__(self):
        return 'Index: {0}, Timestamp: {1}, Data: {2}, Previous Hash: {3}, Hash: {4}'.format(self.index,
                                                                                             self.timestamp,
                                                                                             self.data,
                                                                                             self.previous_hash,
                                                                                             self.hash)

    def calculate_hash(self):
        hash_string = hashlib.sha256()
        hash_string.update(self.covert_to_unicode(str(self.index)) +
                           self.covert_to_unicode(str(self.timestamp)) +
                           self.covert_to_unicode(str(self.data)) +
                           self.covert_to_unicode(str(self.previous_hash)))
        return hash_string.hexdigest()

    def covert_to_unicode(self, string):
        return string.encode('utf-8')

    def has_valid_index(self, previous_block):
        return self.index == previous_block.index + 1

    def has_valid_previous_hash(self, previous_block):
        return self.previous_hash == previous_block.hash

    def has_valid_hash(self):
        return self.calculate_hash() == self.hash