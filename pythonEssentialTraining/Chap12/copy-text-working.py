#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('pythonEssentialTraining/Chap12/lines.txt', 'rt')
    outfile = open('pythonEssentialTraining/Chap12/lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        # outfile.writelines(line)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
