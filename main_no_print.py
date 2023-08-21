import hashlib
num = xxx             #数字开始位置
Path = open("MD5_Start-End.txt","w")
while num <= 50000:     #数字结束位置
    numstr = str(num)
    pw = hashlib.md5()
    pw.update(numstr.encode(encoding='utf8'))
    pw = pw.hexdigest()
    Path.write("name:" + numstr +"\t" + "MD5:" + str.upper(pw) + "\n")
    num = num + 1
Path.close()
