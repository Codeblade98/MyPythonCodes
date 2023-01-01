import requests

url = 'https://api.pwnedpasswords.com/range/'+'password123'
res = requests.get(url)
print(res) #prints <Response[400]>

# we do not just simply save passwords, we hash it first before saving
# But now K Aninomity is used to help servers receive information about us but not know who we are


