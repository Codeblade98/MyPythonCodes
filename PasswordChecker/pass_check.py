import requests
import hashlib

'''
PURPOSE AND METHOD
We need to check if our password is secure or not
To do so we hash our password with SHA1 encoding
Then we take the first five characters of our SHA1 encoded password and request all passwords
from the pwned API and then check the whole password with the requested list and verify
'''

def request_api(password_encoded):

    '''
    Requests the pwned API for the data by giving the first 5 letters of the SHA1 encoded password as 
    parameter. Returns a Response object
    '''
    print(password_encoded)
    pass_str = password_encoded[:5]
    url = 'https://api.pwnedpasswords.com/range/'+ pass_str
    res = requests.get(url) #.get helps us to get the information from the site/API
    print(f'The res status is {res.status_code}')
    print(pass_str)
    
    if res.status_code != 200:
        raise RuntimeError('Error, not fetching 200')
    
    return res

def read_response(response):

    '''
    Accepts Response object as a parameter and returns a list(not of list data type) of responses.
    Returns the text of the Response object
    '''
    # What we want to do here is we accept the response
    # Then we get a collection of all responses from the API with same first 5 characters
    
    return(response.text)

def sha1_encode(password):

    '''
    Encodes the password with SHA1 encoding. Accepts the password as parameter. Returns a SHA1 encoded 
    all uppercase string
    '''

    encoded_pass = password.encode('utf-8') # as unicode objects must be encoded before hashing
    sha1_pass = hashlib.sha1(encoded_pass)
    sha1_hexa = (sha1_pass.hexdigest()).upper()
    return sha1_hexa

def get_leaks_count(response_text, to_check):
    '''
    Takes the response text and the encoded password as parameters
    Checks the tail of the encoded password
    Prints the number of times the password has been leaked and returns the number
    '''
    hash_list = (line.split(':') for line in response_text.splitlines())
    tail = to_check[5:]
    
    # we get a tuple of lists containing the hash code and count of leaks
    for h, count in hash_list:
        if tail == h:
            print(f'Your password has been leaked {count} times')
            return count
        
    print('Your password is secure')

def main(password):
    a = sha1_encode(password)
    b = request_api(a)
    c = read_response(b)
    d = get_leaks_count(c,a)

if __name__ == '__main__':
    p = input('Enter password ')
    main(p)
    

    




