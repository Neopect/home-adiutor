def query():
    conver = True
    firstState = True

    while conver == True:
        print()
        if firstState == True:
            print("What can I help you with?")
            firstState = False
        else:
            print("What else can I help you with?")

        x = input()
        print("Processing request for \"" +x+ "\" now")

        # if x == goodby:
        #     conver = False
        

def langIntrep(query):
    # Trys to translate pseudo statements to key word meaning
    testList = []
    for x in testList:
        if x.contains(query):
            print()