def encrypt_it(text):
    words = text.split()
    # implement step 1
    for i in range(len(words)):
        if words[i] == 'I':
            words[i] = 'i'
    # implement step 2
    last_ind = (len(words)//2)*2
    words[0:last_ind:2], words[1:last_ind:2] = words[1:last_ind:2], words[0:last_ind:2] 
    # implement step 3 nad 4 
    new_words = []
    for i in range(len(words)):
        new_words.append(words[i-1][0]+words[i][-1:0:-1])
        
    return ' '.join(new_words)
    
def decrypt_it(text):
    words = text.split()
    # reverse step 3 nad 4 
    orig_words = []
    for i in reversed(range(len(words))):
        i_plus1 = (i+1) % len(words)
        orig_words.insert(0,words[i_plus1][0]+words[i][-1:0:-1])   
    # reverse step 2 (which is exactly the same as implementing step 2)
    last_ind = (len(orig_words)//2)*2
    orig_words[0:last_ind:2], orig_words[1:last_ind:2] = orig_words[1:last_ind:2], orig_words[0:last_ind:2]  
    # reverse step 1
    for i in range(len(orig_words)):
        if orig_words[i] == 'i':
            orig_words[i] = 'I'
    return ' '.join(orig_words)
