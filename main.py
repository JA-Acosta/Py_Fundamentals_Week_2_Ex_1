'''
>>> JAAR
>>> 07/16/2023
>>> Practicing Fundamentals Program 7
>>> Version 1
'''

'''
>>> Creates a program that'll check if two sentences are palindrome and then counts the frequency of each word in both sentences.
'''

def palindrome_test(phrase_1 : str, phrase_2 : str)-> bool :
    '''
    >>> Checks if the two strings are palindromes.

    >>> Param: (str) phrase_1, (str) phrase_2
    >>> Return: bool
    '''
    if sorted(phrase_2.replace(' ', '')) == sorted(phrase_1.replace(' ', '')) :
        return True
    return False

def unique_words(word_list : list)-> list :
    '''
    >>> Creates a list containing each unique word contained in both phrases maintaining the order of the phrases (phrase_1 + phrase_ 2).

    >>> Param (str) phrase_1, (str) phrase_2
    >>> Return: (list) u_word_list
    '''
    u_word_list = []
    for word in word_list :
        if word not in u_word_list :
            u_word_list.append(word)
    return u_word_list

def word_count(word_list : list,  ) :
    '''
    >>> Takes a list and counts the unique words in the list then returns the count for each word.

    >>> Param: (list) word_list
    >>> Return: (dict) unique_word_count
        key : 'word'
        value : int
    '''
    unique_word_count = {}
    for word in word_list :
        if word in unique_word_count :
            unique_word_count[word] +=1
        else :
            unique_word_count[word] = 1
    return unique_word_count

def main() :
    remove_special_char = lambda phrase : ''.join(char for char in phrase if char.isalnum() or char == ' ')
    phrase = input('Enter a phrase: ').lower()
    phrases = [remove_special_char(phrase)]
    phrase = input('Enter another phrase: ').lower()
    phrases.append(remove_special_char(phrase))
    palindrome = palindrome_test(phrases[0], phrases[1])
    print('\n\t', end= '')
    print('The phrases are palindrome.') if palindrome else print('The phrases are not palindrome.')
    word_list = (f'{phrases[0]} {phrases[1]}').split()
    unique_word_count = word_count(word_list)
    print(f'''
I've ordered the list by unique words based on their occurrence from the start of the first phrase to the end of the second:

        \t'{"', '".join(unique_words(word_list)) }'

I've also counted the occurrence of each word in the combined sentences:
        ''')
    for key, value in unique_word_count.items() :
        print(f'\t{key} : {value}')

if __name__ == '__main__' :
    main()