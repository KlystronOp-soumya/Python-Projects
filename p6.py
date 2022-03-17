from contextlib import contextmanager

@contextmanager
def context():
    print('Entering Context')
    yield 
    print("Exiting Context")

with context():
    print('In Context')