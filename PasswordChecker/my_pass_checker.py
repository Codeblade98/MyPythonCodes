import hashlib
import requests

class PassChecker:
    '''
    To check the security of the passwords by checking the number of times it has been leaked
    '''
    
    encoded_sha1 = ''
    response = ''

    def __init__(self, password):
        self.password = password
    
    def hash_encoder(self):
        '''
        Encodes the password with SHA1 encoding. Accepts the password as parameter. Returns a SHA1 encoded 
        all uppercase string
        '''

        encoded_pass = self.password.encode('utf-8') # as unicode objects must be encoded before hashing
        sha1_pass = hashlib.sha1(encoded_pass)
        self.encoded_sha1 = (sha1_pass.hexdigest()).upper()
    
    def request_api(self):
        '''
        Requests the pwned API for the data by giving the first 5 letters of the SHA1 encoded password
        '''
        pass_str = self.encoded_sha1[:5]
        url = 'https://api.pwnedpasswords.com/range/'+ pass_str
        self.response = requests.get(url)
        if self.response.status_code != 200:
            raise RuntimeError('Error, not fetching 200')
    

    def check_leaks(self):
        '''
        Takes the response text and the encoded password
        Checks the tail of the encoded password
        Prints the number of times the password has been leaked and returns the number
        '''
        tail = self.encoded_sha1[5:]
        response_text = self.response.text
        hash_list = (line.split(':') for line in response_text.splitlines())

        for item, count in hash_list:
            if item == tail:
                print(f'The password has been leaked {count} times')
                return None
        
        print('Your password is secure')
    
    def check_safety(self):
        '''
        Executes all the functions and does the job of Encapsulation
        '''
        self.hash_encoder()
        self.request_api()
        self.check_leaks()
    

if __name__ == '__main__':
    pw = input('Enter password ')
    p1 = PassChecker(pw)
    p1.check_safety()

