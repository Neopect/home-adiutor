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
    #TODO Refractor and Simplify
    #FIXME Computer can't read multiword phrases if word is used in a singlar context
    qlst = query.split()
    # print("query "+ query)
    # print(qlst)
    extWords= []
    tranState= []
    for state_org in qlst:
        # For each word in query try to match with a phrase
        # If not, add it to extWords[] and try again until possible
        # If nonthing is found, error out a not understanding quote
        print("Starting analysis for " + state_org)
        print("starting extWords = to vv")
        print(extWords)
        state_new = ""
        if extWords != []:
            for e in extWords:
                state_new = e + " " 
            state_new = state_new + state_org
        else:
            state_new = state_org
        print("Starting full analysis for " + state_new)

        jr = open("adiutor\Main\lang.json")
        jrdata = json.load(jr)
        jr.close()

        solved = False
        # while solved == False:
        for x in jrdata:
            for y in jrdata[x]:
                if y.lower() == state_new.lower():
                    solved = True
                    print("True")
                    tranState.append(x)
                    extWords.clear()
                    break

            if solved == True:
                break
            #     pass

        if solved == False:
            extWords.append(state_org)

        print("final extWords = to vv")
        print(extWords)
        print("\n=====================================================================================\n")

    print(tranState)

        

        




# Hey Computer,| what is  | the Time
#  Wake word   |query into| Question
