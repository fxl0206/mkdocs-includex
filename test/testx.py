import os
import sys

def main(argv):
    path=os.path.splitext("1.txt")[-1]
    print(path)

if __name__ == "__main__":
   main(sys.argv[1:])