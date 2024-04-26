f=open("1.txt",'w')
f.write('Hello')
f.close()

f=open("1.txt", 'a')
f.write('World')
f.close()

f=open('1.txt','r')
text=f.read()
print(text)
f.close()

f = open("one.txt","w")
lines=["Hello","World","Hi","Cool"]
for line in lines:
    f.writelines(line+'\n')
f.close()

f=open('one.txt','r')
while True:
    line=f.readlines()
    if not line:
        break
    print(line)
    
with open('one.txt','r') as f:
    print(type(f))
    f.seek(3)
    data = f.read(3)
    print(data)