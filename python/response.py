import sys
from chatterbot import ChatBot


#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return lines[0]

def main():
    #get our data as an array from read_in()
    request = read_in()

    # Create a new instance of a ChatBot
    bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./python/database.sqlite3"
    )

    response = bot.get_response(request)
    #return the sum to the output stream
    print (response)

# Start process
if __name__ == '__main__':
    main()