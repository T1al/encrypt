try:
    import hashlib
    from sys import argv
    hash = argv[1]
    ss = argv[2]
    if ss == "blake2b":
        crypt = hashlib.blake2b()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
    if ss == "sha224":
        crypt = hashlib.sha224()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
    if ss == "sha1":
        crypt = hashlib.md5()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
    if ss == "md5":
        crypt = hashlib.md5()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
    if ss == "blake2s":
        crypt = hashlib.blake2s()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
    if ss == "sha512":
        crypt = hashlib.sha512()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
    if ss == "sha384":
        crypt = hashlib.sha384()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
    if ss == "sha256":
        crypt = hashlib.sha256()
        crypt.update(b"\hash")
        print(crypt.hexdigest())
except IndexError:
    print("usege : python3 encrypt.py {text} {hash md5,md4,else} ")
