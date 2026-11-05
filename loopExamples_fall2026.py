# ***************************************************************************************************
#   Fall 2026 - Example for Intro to Git In-class Assignment
#   Created by Maggie Vanderberg on Nov. 4th 2026
#   This file contains examples from the loops lecture given during Week 6 of the Fall term.
# ***************************************************************************************************

def loop_through_it(data_structure):
    ''' prints each item in structure that was passed in. None is returned.'''
    if type(data_structure) is dict: # Learned that type() and "is" is possible from Gemini. type() determines the type of input recieved, "is" just means ==.
        for item in data_structure:
            print(f"{item}:{data_structure[item]}", end="\t")
    else:    
        for item in data_structure:
            print(item, end="\t")

def num_vowels(input_text):
    ''' count and return the number of vowels in the input text'''
    count = 0
    for character in input_text:
        # check if character should be counted
        # assumes y is not a vowel
        if character.lower() in ['a','e','i','o','u']:
            count += 1
    return count

def num_non_vowels(input_text):
    ''' count and return the number of non-vowels in the input text'''
    count = 0
    for character in input_text:
        # checks if a character should be counted
        # assumes y is a non vowel
        if character.lower() in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            count += 1
    return count

def nested_loops(i,j):
    ''' prints a grid of X's with i rows and j columns. Nothing is returned.'''
    for row in range(i):
        for col in range(j):
            print("X", end="\t")
        print()  # print a new line after each row
    print()

def test_loop_through_it():
    ''' This function doesn't take any input or return any values. Instead it executes the loop_through_it function
    with various types of input (i.e.., a list, a typle, a string, a set, a dictionary) '''
    print("Looping through structures")
    print("List... ")
    loop_through_it([1,2,3,4,5])    # list
    print("\nTuple... ")
    loop_through_it(('a','b','c'))  # tuple
    print("\nString... ")
    loop_through_it("hello")        # string
    print("\nSet... ")
    loop_through_it({2,10,3,20})    # set (order is not guarenteed)
    print("\nDictionary... ")
    studentGradeDictionary = {'discussion':10, 'attendance':5, 'zybook':30}
    loop_through_it(studentGradeDictionary) #dictionary



def test_count_vowels():
    ''' This function doesn't take any input or return any values. It tests the count_vowels function with two 
    different strings.'''
    print("\n\nExecuting count vowel function... ")
    print("And, printing value(s) returned for first execution with 'Hello! My name is Maggie V.' :")
    print(num_vowels("Hello! My name is Maggie V."))
    text = "How many vowels?"
    print("And, printing value(s) returned for second execution: ", text)
    print(num_vowels(text))
    print()
    # what if we wanted to count non_vowels?

def test_num_non_vowels():
    ''' This function doesn't take any input or return any values. It tests the num_non_vowels function with two 
    different strings.'''
    print("\n\nTesting the count of non vowels...")
    print("Printing the values returned for the first execution with 'Hello! My name is Maggie V.' :")
    print(f"Total: {num_non_vowels("Hello! My name is Maggie V.")}. Looking for 12.")
    text = "How many non-vowels?"
    print(f"And printing value(s) returned for second execution: '{text}'")
    print(f"Total: {num_non_vowels(text)}. Looking for 11.")

def test_nested_loops():
    ''' This function doesn't take any input or return any values. It tests the nested_loops function with two 
    different sets of parameters.'''
    print("\nExecuting nested loops function... ")
    print("And, printing value(s) returned for first execution with parameters 3 and 5 :")
    nested_loops(3,5)
    print("And, printing value(s) returned for second execution with parameters 4 and 2 :")
    nested_loops(4,2)
    print()

def main():
    ''' This function is called when this file is executed directly.
    It does not take in any parameters and it will return None '''
    # test loop through structures
    test_loop_through_it()
    # testing count vowels
    test_count_vowels()
    # testing new function counting non-vowels
    test_num_non_vowels()
    # test nested loops
    test_nested_loops()

if __name__ == "__main__":
    # execute the main function
    main()