#python3 hello.py -n 5
import argparse
parser = argparse.ArgumentParser(description= "Hello kitty")
parser.add_argument("-n" , default= 1 , help= "No of times to Hello" , type= int)
args = parser.parse_args()

for _ in range(args.n):
    print("Hello")