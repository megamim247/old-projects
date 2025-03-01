import hashlib
from cryptography.fernet import Fernet
import base64

username_trial = b"GOUGH"
bUsername_trial = b"GOUGH"
key="picoCTF{1n_7h3_|<3y_of_f911a486}"
print(hashlib.sha256(username_trial).hexdigest()[4])
print(hashlib.sha256(username_trial).hexdigest()[5])
print(hashlib.sha256(username_trial).hexdigest()[3])
print(hashlib.sha256(username_trial).hexdigest()[6])
print(hashlib.sha256(username_trial).hexdigest()[2])
print(hashlib.sha256(username_trial).hexdigest()[7])
print(hashlib.sha256(username_trial).hexdigest()[1])
print(hashlib.sha256(username_trial).hexdigest()[8])