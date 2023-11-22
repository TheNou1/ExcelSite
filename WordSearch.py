
FORWARD = 1
BACKWARDS = -1

def is_outside_list(letter_list,index):
    """
    checks if index is within bounds or not 
    and returns the corresponding boolean 

    inputs: 
    letter_list(list)
    index(integer)

    outputs:
    boolean

    Examples: 

    testList = [1, 2, 2, 3, 14, 341, 35, 135, 13, 5]

    print(is_outside_list(testList, 9)) # False
    --------------------------------------------------------------------------
    large_list = list(range(1, 1000001))

    print(is_outside_list(large_list, -1)) # True
    ----------------------------------------------------------------------------
    null_list = []

    print(is_outside_list(null_list,111)) # True

     """
    if index in range(len(letter_list)) and index >= 0:
        return False 

    else:
        return True



def letter_positions(letter_list,character):
    """ 
     Counts which indexes within a list a character can be found

     inputs: 
     letter_list(list)
     character(string)

     outputs:
     found_count(list)

print(letter_positions([],'e')) #[]
-------------------------------------------
print(letter_positions(['r','w','e','e','t','g','e'],'e'))#[2, 3, 6]
-------------------------------------------
print(letter_positions(['r','w','e','e','t','g','e','e','e','e','e','e','e'
,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',
'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'
,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e'
,'e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e',
'e','e','e','e','e','e','e','e','e','e','e','e','e'],'e'))

#[2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 
        """    
    """#2 Do not use the in keyword to test for membership (you can use the in keyword
    in the for loop but not to check if a letter exist in a list) Is the way i used it okay?""" 
    found_count = []

    for index in range(len(letter_list)):
        if letter_list[index] == character:
            found_count.append(index)
    return found_count

def valid_word_pos_direction(letter_list,word,index,direction):
    """ 
    Finds a word within a list of letter

    inputs:
    letter_list(list)
    word(string)
    direction(integer)

    outputs:
    boolean

    examples:
    l = ["r","a","d","a","r"]
    print(valid_word_pos_direction(l, "rad mj8ar",0,1))#True
    ---------------------------------------------------
    print(valid_word_pos_direction(l, "radar",5,-1))#False
    ------------------------------------------------------
    print(valid_word_pos_direction(l, "radar",4,-1))#True
    """ 
    if not is_outside_list(letter_list,index):

        for count in range(len(word)):

            if (not is_outside_list(letter_list,index)) and letter_list[index] == word[count]:

                index += direction

            else:
                return False

        return True
    return False

def direction_word_given_position(letter_list,word,index):
    """ calls valid_word_pos_direction to check which direction
     a word can be found. if the word isn't found return an empty list

    inputs:
    letter_list(list)
    word(string)
    index(integer)

    outputs:
    success(list)
    
    letter_list= ['A','B','C','D','C','M'] 
    word =' ' 
    index = 3
    print(direction_word_given_position(letter_list,word,index))
    #[]
    -------------------------------------------------------------  
    letter_list= ['A','B','C','D','C','M'] 
    word ='CBA' 
    index = 2
    print(direction_word_given_position(letter_list,word,index))
    #[-1]
    -------------------------------------------------------------------
    letter_list= ['A','B','C','D','C','M'] 
    word ='CDC' 
    index = 2
    print(direction_word_given_position(letter_list,word,index))
    #[1]
    """
    success = []


    if valid_word_pos_direction(letter_list,word,index,-1):

        success.append(BACKWARDS)

    if valid_word_pos_direction(letter_list,word,index,1):

        success.append(FORWARD)

    return success
 
def position_direction_word(letter_list,word):
    """ combines the results of direction_word_given_position and letter_positions 
    and returns a list of the correct indices and directions

    inputs:
    letter_list(list)
    word(string)

    outputs:
    total(list)
    examples:

     letter_list= ["A","B","C","D","C","M"]
word = "DC"
print(position_direction_word(letter_list,word))
[[3, -1], [3, 1]]

    letter_list= []
word = " "
print(position_direction_word(letter_list,word))
[] 

    letter_list = ['t', 'o', 'b', 'o', 'n', 'r','a','c', 
    'w', 'x', 'y', 'z', 'd']
word = 'car'
print(position_direction_word(letter_list,word))
[[7, -1]]
    """
    total = []

    if len(letter_list) == 0 and len(word) == 0:
        return total
    
    indices = letter_positions(letter_list,word[0])
    
    

    for number in indices:

        resolved = direction_word_given_position(letter_list,word,number)

        if resolved: #Check if the position in the indices is valid
            
            for direction in resolved:

                total.append(list((number,direction))) 
    return total

    
    if len(successes) == 0:
        return successes
        
    return total

def cross_word_position_direction(bool_letter_list,length_word,index,direction):
    """ simulates a crossword being crossed out at specific positions 
    by changing a list of booleans

    inputs:

    bool_letter_list(list)
    length_word(inter)
    index(integer)
    direction(integer)

    outputs:
    None

    examples: 

boolList = [False, False, False, False, False]
length_word = 8
index = 2
direction = 1
cross_word_position_direction(boolList,length_word,index,direction)
print(boolList)
[False, False, False, False, False]

boolList = [False, False, False, False, False]
length_word = 0
index = 2
direction = 1
cross_word_position_direction(boolList, length_word, index, direction)
print(boolList)
[False, False, False, False, False]
    
boolList= [False, False, False, False, False, False] 
length_word = 2
index = 4  
direction = 1
cross_word_position_direction(boolList, length_word, index, direction)
print(boolList)
[False, False, False, False, True, True]
    """
    pos = index

    if not is_outside_list(bool_letter_list,(index + (length_word-1)*direction)):       
    #makes sure the word is within the index
    
        for count in range(length_word):

            bool_letter_list[pos] = True
            pos += direction


def cross_word_all_position_direction(bool_letter_list,length_word,list_position_direction):
    """calls cross_word_position_direction but for multiple position-direction pairs
     
    inputs: 
    bool_letter_list(list)
    length_word(integer)
    list_position_direction(list)


    outputs:
    None

    examples: 

boolList = []
length_word = 3
list_position_direction = [(2, 1), (1, -1)]
cross_word_all_position_direction(boolList, length_word, list_position_direction)
print(boolList)

[]


boolList = [False, False, False, False, False]
length_word = 10
list_position_direction = [(2, 1), (1, -1)]
cross_word_all_position_direction(boolList, length_word, list_position_direction)
print(boolList)

[False, False, False, False, False]

boolList = [False, False, False, False, False]
length_word = 3
list_position_direction = [(2, 1), (-1, 1), (6, 1)]
cross_word_all_position_direction(boolList, length_word, list_position_direction)
print(boolList)

[True, True, True, True, True]

    """
    for pair in list_position_direction:

        cross_word_position_direction(bool_letter_list,length_word,pair[0],pair[1])

 
def find_magic_word(letter_list,bool_letter_list):
    """Makes a word out of the False elements in a list
    inputs:
    letter_list(list)
    bool_letter_list(list)

    outputs:
    word(string)

    examples:

    letter_list = ['e', 'e', 'e']
bool_letter_list = [True, False]
print(find_magic_word(letter_list, bool_letter_list))
#Value error was raised

    letterlist = []
bool_letterlist = []
print(find_magic_word(letterlist, bool_letterlist))
#no return

    letter_list = ['a', 'b', 'c']
bool_letter_list = [True, True, True]
print(find_magic_word(letter_list, bool_letter_list))
 #no return
    """

    if len(letter_list) != len(bool_letter_list):

        raise ValueError("Both lists should have the same size")
    
    magic_word = []

    for index in range(len(bool_letter_list)):

        if bool_letter_list[index] == False:

            magic_word.append(letter_list[index])

    word = ''.join(magic_word)
    return word


def word_search(letter_list,word_list):
    """ Calls previous functions to cross out a word in a list of letters
    inputs:
    letter_list(list)
    word_list(word)

    outputs:
    word(string)

    examples:
    
    letter_list = ["C","w","I","K","I","P","E","D","I","A","O","M","M","O","D","N","A","R","P"]
word_list = ["WIKIPEDJIA","FANDOM"]
print(word_search(letter_list,word_list))
CwIKIPEDIAOMMODNARP

    letter_list = ["C", "W", "I", "K", "I", "P", "E", "D", "I", "A", "O", "M", "M", "O", "D", "N", "A", "R", "P"]
word_list = ["WIKIPEDIA","RANDOM"]
result = word_search(letter_list, word_list)
print(result)
COMP

    letter_list = ["C", "w", "I", "K", "I", "P", "E", "D", "I", "A", "O", "M", "M", "O", "D", "N", "A", "R", "P"]
word_list = ["XZYZYZ", "RJASNDSDAD"]
result = word_search(letter_list, word_list)
print(result)
CwIKIPEDIAOMMODNARP
    """

    bool_list = []

    for element in letter_list:

        bool_list.append(False)

    for word in word_list:

        position_direction_list = position_direction_word(letter_list,word)
        

        cross_word_all_position_direction(bool_list,len(word),position_direction_list)

    return find_magic_word(letter_list,bool_list) 



def word_search_main(letters,words):
    """turns two string inputs into lists 
    and finds the magic word with word_search
    
    inputs:
    letters(string)
    words(string)

    outputs:
    word(string)

    examples:

    letters = "PjAVA++CJSYLQSPHPTGOHNILTOKOmatLABNTFIWSRUSTYBURTRAd"
words = "java-C++-JS-SQL-php-GO-kotlin-MATLaB-SWIFT-RUSt-ruby-DART"
print(word_search_main(letters,words))

PYTHON


    letters = "ABCDEFGHIJKLM"
words = "NOPQRSTUVWXYZ"
print(word_search_main(letters, words))

ABCDEFGHIJKLM

    letters = ""
words = ""
print(word_search_main(letters, words))
    """
    letter_list = []
    word_list = []

    for character in letters.upper():

        letter_list.append(character)

    for character in words.upper().split('-'):

        word_list.append(character)
    
    return word_search(letter_list,word_list)




