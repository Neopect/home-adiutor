import json

def query():
    conver = True
    firstState = True

    while conver == True:
        # Convert to remove need of if statement
        print()
        if firstState == True:
            print("What can I help you with?")
            firstState = False
        else:
            print("What else can I help you with?")

        x = input()
        print("Processing request for \"" +x+ "\" now")

        langIntrep(x)
        # if x == goodby:
        #     conver = False
        

def langIntrep(query):
    """
    - Try's to translate pseudo statements to key word meaning -

    Going to go through a evaluation algorthim that seeks 
    to solve and break down the sentence into key parts by 
    going through each word, trying to ref link it to the 
    lang.json index.
    """
    
    qlst = query.split()
    extWords= []
    for x in qlst:
        # For each word in query try to match with a phrase
        # If not, add it to extWords[] and try again until possible
        # If nonthing is found, error out a not understanding quote
        if x.contains(query):
            print()




# def 


# Hey Computer,| what is  | the Time
#  Wake word   |query into| Question