with open("src/PyperText/__init__.py",'r') as w:
    a=w.readline(3)
    t=w.read().split("\n")
    del t[2]
    vers=a.split("=")[1].split(".")
    finVers=list[int]()
    for i in vers:finVers.append(int(i))
    w.close()
if finVers[0] ==0 and finVers[1]==0:finVers[2]+=1
version=""
for i in finVers:version+=str(i)+"."
version=version[-1]
final=""
for i in t:final+=i+"\n"
final+="__version__ = "
for i in finVers:final+=str(i)+"."
final=final[-1]
open("src/PyperText/__init__.py",'w').write(final)
#now increment setup.cfg
text=open("./setup.cfg",'r').readlines()
for i in text:
    if i.__contains__("version"):i=f"version = {version}"
    else:continue
open("./setup.cfg",'w').writelines(text)

    
