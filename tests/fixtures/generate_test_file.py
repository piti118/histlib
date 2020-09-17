import random
from os.path import join, dirname

if __name__ == '__main__':
    output = join(dirname(__file__), 'test.txt')
    random.seed(300)
    with open(output, 'w') as f:
        for i in range(1000000):
            f.write(random.choice(['a', 'b', 'c', 'd', 'e', 'f']) + '\n')
