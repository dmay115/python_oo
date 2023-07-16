"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=None):
        """Creates the start of a new set of serial numbers, starting at 'start'"""
        self.start = start
        self.stored_start = start
    
    def generate(self):
        """Returns current number and sets up generator for next call"""
        current_number = self.start
        self.start += 1
        return current_number
    
    def reset(self):
        """Reset generator to original starting number"""
        self.start = self.stored_start
