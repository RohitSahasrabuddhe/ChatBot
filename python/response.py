import sys

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return lines[0]

def main():
    #get our data as an array from read_in()
    lines = read_in()
    lines = 'ABC' + lines
    #return the sum to the output stream
    print (lines)

# Start process
if __name__ == '__main__':
    main()