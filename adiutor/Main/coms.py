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
    #TODO Remove punctuation to avoid errors
    
    qlst = query.split()
    
    extWords= []
    tranState= []
    
    solved_fut = False

    for ct, state_org in enumerate(qlst):
        print('iter of ' + str(ct))

        if solved_fut == True:
            solved_fut = False
            continue
        
        extWords.append(state_org)

        # Combines any unsolved words from previous loop to current loop
        # state_new = str()
        # if extWords != []:
        #     for e in extWords:
        #         state_new = e + " " 
        #     state_new = state_new + state_org
        # else:
        #     state_new = state_org

        state_new = ''.join(extWords)
        # if extWords != []:
        #     for e in extWords:
        #         state_new = e + " " 
        #     state_new = state_new + state_org
        # else:
        #     state_new = state_org
        
        # Creates possible query for multiword phrases and reduce iterations
        state_fut = str()
        try:
            state_fut = state_new + " " + qlst[ct + 1]
        except:
            print("EOP")
        

        jr = open("adiutor\Main\lang.json")
        jrdata = json.load(jr)
        jr.close()

        solved = False
        
        print(extWords)

        print('state_new = ' + state_new)
        print('state_fut = ' + state_fut)

        # Checks lib for synonyms of dic words
        for x in jrdata:
            for y in jrdata[x]:
                # Doesn't account for which one to check first, just checks what comes first in lib
                if y.lower() == state_fut.lower():
                    solved = True
                    solved_fut = True
                    print("True fut")
                    tranState.append(x)
                    extWords.clear()
                    break
                elif y.lower() == state_new.lower():
                    solved = True
                    print("True new")
                    tranState.append(x)
                    extWords.clear()
                    break

            if solved == True:
                break
           

        # if solved == False:
        #     extWords.append(state_org)

        # if solved == False:
        #     extWords.append(state_org)
        
        print(extWords)

    print(tranState)

        

        




# Hey Computer,| what is  | the Time
#  Wake word   |query into| Question
