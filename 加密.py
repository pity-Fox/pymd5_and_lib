import hashlib
while True:
    Userin = input("输入加密算法(MD5_SHA1_SHA256_SHA512):")
    Txt = input("请输入加密文本:")
    Userin = Userin.upper()
    if Userin =="MD5":
        hl=hashlib.md5()
        hl.update(Txt.encode(encoding='utf8'))
        md5=hl.hexdigest()
        print("加密结果："+str.upper(md5)+"\n")
    #MD5
    elif Userin =="SHA1":
        hl=hashlib.sha1()
        hl.update(Txt.encode(encoding='utf8'))
        sha1=hl.hexdigest()
        print("加密结果："+str.upper(sha1)+"\n")
    #SHA1
    elif Userin =="SHA384":
        hl=hashlib.sha384()
        hl.update(Txt.encode(encoding='utf8'))
        sha384=hl.hexdigest()
        print("加密结果："+str.upper(sha384)+"\n")
    #SHA384
    elif Userin =="SHA256":
        hl=hashlib.sha256()
        hl.update(Txt.encode(encoding='utf8'))
        sha256=hl.hexdigest()
        print("加密结果："+str.upper(sha256)+"\n")
    #SHA256
    elif Userin=="SHA512":
        hl=hashlib.sha512()
        hl.update(Txt.encode(encoding='utf8'))
        sha512=hl.hexdigest()
        print("加密结果："+str.upper(sha512)+"\n")
    #SHA512
    else:
        print("输入有误")
