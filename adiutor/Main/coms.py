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
    #TODO Remove punctuation to avoid errors
    
    qlst = query.split()
    
    extWords= []
    tranState= []
    solved_fut = False

    for ct, state_org in enumerate(qlst):
        solved = False
        if solved_fut:
            solved_fut = False
            continue

        # Combines any unsolved words from previous loop to current loop
        extWords.append(state_org)
        state_new = ''.join(extWords).lower()
        
        # Creates possible query for multiword phrases and reduce iterations
        state_fut = str()
        try: state_fut = state_new + " " + qlst[ct + 1].lower()
        except: print("EOP")
        
        # Replace with a with as statement
        jr = open("adiutor/Main/lang.json")
        jrdata = json.load(jr)
        jr.close()

        # Checks lib for synonyms of dic words
        for x in jrdata:
            for y in jrdata[x]:
                # Doesn't account for which one to check first, just checks what comes first in lib
                if y == state_fut or y == state_new:
                    solved = True
                    if y == state_fut:
                        solved_fut = True
                    tranState.append(x)
                    extWords.clear()
                    break

            if solved: break

    print(tranState)

        

        




# Hey Computer,| what is  | the Time
#  Wake word   |query into| Question
