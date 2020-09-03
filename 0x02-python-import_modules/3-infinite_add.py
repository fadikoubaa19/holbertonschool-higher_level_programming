#!/usr/bin/python3
if __name__ == "__main__":
    import sys
if len(sys.argv) > 1:
    if len(sys.argv) == 2:
        print("{:s}".format(sys.argv[1]))
    else:
        k = 0
        for i in range(1, len(sys.argv)):
            k += int(sys.argv[i])
        print(k)
else:
    print("0")
