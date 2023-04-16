import hashlib

m = hashlib.md5(str("Hello").encode()).hexdigest()
if(hashlib.md5(str("Hello").encode()).hexdigest() == hashlib.md5(str("Hello").encode()).hexdigest()):
    print("Hello")
