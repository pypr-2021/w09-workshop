def encrypt_it(text):
    '''
    Encrypts the string text using the algorithm described in the brief.
    
    Input: text (str): the string to encrypt
    Output: encrypted_text (str): the string encrypted
    '''
    # Split the sentence into words
    words = text.split()
    
    # Step 1: change "I" to "i"
    words = ['i' if word == 'I' else word for word in words]
    
    # Step 2: swap the words in consecutive pairs,
    # ignore last word if there's an odd number of words
    words[:-1:2], words[1::2] = words[1::2], words[:-1:2]
    
    # Steps 3 and 4: shift the first letters, reverse the other letters
    new_words = [words[i-1][0] + words[i][:0:-1] for i in range(len(words))]
    
    # Join all the new words into one string, separated by spaces
    return ' '.join(new_words)


def decrypt_it(text):
    '''
    Decrypts the string text using the reverse algorithm as for encrypt_it().
    
    Input: text (str): the string to decrypt
    Output: encrypted_text (str): the string decrypted
    '''
    # Split the sentence into words
    words = text.split()
    
    # Now, we do the steps backwards
    # Step 4: revert all letters except the first, and    
    # step 3: move the first letters back up one word
    new_words = [words[i+1][0] + words[i][:0:-1] for i in range(len(words)-1)]
    new_words.append(words[0][0] + words[-1][:0:-1])    # Do the last word separately

    # Step 2: swap back pairs of words
    new_words[:-1:2], new_words[1::2] = new_words[1::2], new_words[:-1:2]
    
    # Step 1: change words 'i' back to 'I'
    new_words = ['I' if word == 'i' else word for word in new_words]
    
    # Join all the new words into one string, separated by spaces
    return ' '.join(new_words)
