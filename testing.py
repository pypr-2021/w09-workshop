# Import the functions from the other script to test them
from model1 import encrypt_it, decrypt_it
#  from model2 import encrypt_it, decrypt_it
#  from model3 import encrypt_it, decrypt_it
#  from model4 import encrypt_it, decrypt_it
#  from week09_code import encrypt_it, decrypt_it

# You can run this script to perform the tests directly -- just put the .py file with the
# function definitions in the same folder, and change the import above to import the
# functions from the file.
# If you prefer, you could also just copy this code at the end of the script to assess,
# and run that directly.
# Of course you can also run your own tests!

# You can also add code here to time the different model solutions,
# using e.g. timeit() or a profiler.
# To compare the performance of different functions, you can import all of them
# as a different namespace -- for example:
# import model1 as m1
# import model2 as m2
# Then, you can compare e.g. encrypt_it in both files using
# m1.encrypt_it() and m2.encrypt_it().

# Test encryption
my_text = 'This course is fun, but I am tired of programming in Python!'
encrypted = 'iesruo csih T,nu fs i itu bderi tm agnimmargor pf o!nohty Pn'
print(encrypt_it(my_text))

# "assert x" does nothing if x is True, and gives an error if x is False
assert encrypt_it(my_text) == encrypted, 'Encrypted string incorrect!'

# Test decryption
my_text = 'pcimedna peh Te blli w!noo srev omla cpee Kyojn edn an ignimmargor p!nohty'
print(decrypt_it(my_text))

print(decrypt_it('tesua cemo Srevereh wssenippa h;o gyeh treveneh wemo s.o gyeh'))
print(decrypt_it('mevo l ihti wuo yy mll a i!ylle bo tdetna wtrae hya sy mtu bs iylle b.reggi bhcu'))

def test_encrypt_decrypt(my_text, display=False):
    '''
    Test encrypt/decrypt functions by comparing
    original string to encrypted, then decrypted string.
    '''
    # Encrypt then decrypt the string
    decrypted = decrypt_it(encrypt_it(my_text))
    
    if display:
        # Optionally display both strings to compare them
        print('\n', my_text, decrypted, sep='\n')
    
    # This returns an error if the decrypted string is different from the original
    assert decrypted == my_text, 'Original string different from decrypted string!'


def make_random_string():
    '''
    Randomly generated a string of characters.
    '''
    import random
    import string
    # Make a random string of random length with random words
    my_text = []
    for i in range(random.randint(5, 20)):
        my_text.append(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase,
                                              k=random.randint(3, 15))))
    return ' '.join(my_text)
    

# Test our functions
test_encrypt_decrypt('This course is fun, but I am tired of programming in Python!', display=True)
test_encrypt_decrypt('I\'ve had toast for breakfast today, and I enjoyed it.', display=True)

for i in range(10):
    # If nothing happens here, that's a good sign!
    my_text = make_random_string()
    test_encrypt_decrypt(my_text, display=False)
