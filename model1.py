def encrypt_it(text):
    # Make a list of words
    words = []
    word = ''
    for char in text:
        if char != ' ':
            word += char
        else:
            words.append(word)
            word = ''
    # Add the last word
    words.append(word)
    
    # Step 1: change "I" to "i"
    for i in range(len(words)):
        if words[i] == 'I':
            words[i] = words[i].lower()
        else:
            words[i] = words[i]
    
    # Step 2: swap the words in consecutive pairs,
    # ignore last word if there's an odd number of words
    new_words = [0] * len(words)
    for i in range(len(words)):
        if i % 2 == 0 and i+1 < len(words):
            new_words[i] = words[i+1]
            new_words[i+1] = words[i]
        else:
            pass
    if new_words[-1] == 0:
        new_words[-1] = words[-1]
    
    # Step 3: shift the initials
    initials = [new_words[-1][0]]
    for i in range(len(words)-1):
        initials.append(new_words[i][0])
    
    new_new_words = []
    for i in range(len(words)):
        rest_of_word = new_words[i][1:]
        new_new_words.append(initials[i] + rest_of_word)
    
    # Step 4: reverse the other letters
    reversed_words = []
    for i in range(len(words)):
        word_backwards = ''
        for j in range(len(new_new_words[i])-1, 0, -1):
            word_backwards += new_new_words[i][j]
        reversed_words.append(new_new_words[i][0] + word_backwards)
    
    # Join all the words in one string
    encrypted_text = ''
    for i in range(len(words)):
        encrypted_text += reversed_words[i]
        encrypted_text += ' '
    
    return encrypted_text[0:-1]
    
    
def decrypt_it(text):
    # Make a list of words
    words = []
    word = ''
    for char in text:
        if char != ' ':
            word += char
        else:
            words.append(word)
            word = ''
    # Add the last word
    words.append(word)
    
    # Step 4: reverse the other letters
    reversed_words = []
    for i in range(len(words)):
        word_ordered = ''
        for j in range(len(words[i])-1, 0, -1):
            word_ordered += words[i][j]
        reversed_words.append(words[i][0] + word_ordered)
    
    # Step 3: shift the initials
    initials = []
    for i in range(1, len(reversed_words)):
        initials.append(reversed_words[i][0])
    initials.append(reversed_words[0][0])
    
    new_words = []
    for i in range(len(words)):
        rest_of_word = reversed_words[i][1:]
        new_words.append(initials[i] + rest_of_word)
        
    # Step 2: swap the words in consecutive pairs,
    # ignore last word if there's an odd number of words
    new_new_words = [0] * len(words)
    for i in range(len(words)):
        if i % 2 == 0 and i+1 < len(words):
            new_new_words[i] = new_words[i+1]
            new_new_words[i+1] = new_words[i]
        else:
            pass
    if new_new_words[-1] == 0:
        new_new_words[-1] = new_words[-1]
    
    # Step 1: change "i" to "I"
    for i in range(len(words)):
        if new_new_words[i] == 'i':
            new_new_words[i] = new_new_words[i].upper()
        else:
            new_new_words[i] = new_new_words[i]
    
    # Join all the words in one string
    decrypted_text = ''
    for i in range(len(words)):
        decrypted_text += new_new_words[i]
        decrypted_text += ' '
    
    return decrypted_text[0:-1]
