from itertools import cycle

def encrypt_it(text):
    '''
    Encrypts the string text using the algorithm described in the brief.
    
    Input: text (str): the string to encrypt
    Output: encrypted_text (str): the string encrypted
    '''
    # Split the sentence into words
    words = text.split()
    N = len(words)
    
    # Step 1: change "I" to "i"
    for i in range(N):
        if words[i] == 'I':
            words[i] = 'i'
    
    # Step 2: swap the words in consecutive pairs,
    # ignore last word if there's an odd number of words
    i = 0
    while i < N - 1:
        current_word = words[i]
        words[i] = words[i+1]
        words[i+1] = current_word
        i += 2
    
    # Steps 3 and 4: shift the first letters, reverse the other letter
    words_cyclic = cycle(words)
    # Advance by N-1 to start at the last word
    for i in range(N-1):
        next(words_cyclic)
    
    initials = ''.join(next(words_cyclic)[0] for word in words)
    new_words = [i + ''.join(reversed(word[1:])) for i, word in zip(initials, words)]
    
    # Return the final string, remove the last space
    return ' '.join(new_words)


def decrypt_it(text):
    '''
    Decrypts the string text using the reverse algorithm as for encrypt_it().
    
    Input: text (str): the string to decrypt
    Output: encrypted_text (str): the string decrypted
    '''
    # Split the sentence into words
    words = text.split()
    N = len(words)
    
    # Now, we do the steps backwards
    # Step 4: revert all letters except the first, and    
    # step 3: move the first letters back up one word
    words_cyclic = cycle(words)
    next(words_cyclic)   # advance by 1 to start at the second word
    
    initials = ''.join(next(words_cyclic)[0] for word in words)
    new_words = [i + ''.join(reversed(word[1:])) for i, word in zip(initials, words)]
    
    # Step 2: swap back pairs of words
    i = 0
    while i < N - 1:
        current_word = new_words[i]
        new_words[i] = new_words[i+1]
        new_words[i+1] = current_word
        i += 2
    
    # Step 1: change words 'i' back to 'I'
    for i in range(N):
        if new_words[i] == 'i':
            new_words[i] = 'I'
    
    # Join all the new words into one string, separated by spaces
    return ' '.join(new_words)
