import os

while True:
    f = os.popen('./lmao.sh')
    print(f.read())

