az=oz=[]
di={}
import re

file = "file2.txt"
#NOW, MAKE IT SOCKET RATHER THAN FILE, AND CREATE SOLUTION TO CAPTCHA PROBLEM

ez = open(file)

for lines in ez.readlines():
    az = re.findall(r'\?ci\D*(\d*)\S*.{4}(\d*)',lines)
    print('1')
    print(az)

for c_code,n_cites in az:
    print('1.5')
    c_code,n_cites = str(c_code),str(n_cites)
    ez = open(file)
    print('2')
    for lines in ez.readlines():
        print('2')
        yz = None
        #f - literal string was makign the \d{4} fail. replaced with double curly bracket.
        yz = re.findall(rf"d={c_code}(?!.*d={c_code}).*?>([^-]*?)</a.+?\">(.+?)(\d{{4}}).+?gs_rs\">(.+?)</div",lines)
        if yz is not None:
            for tup in yz:
                a,b,c,d=tup[0],tup[1],tup[2],tup[3]
                title,author_journal,year,desc = re.sub('<.*?>', '', a),re.sub('<.*?>', '', b),re.sub('<.*?>', '', c),re.sub('<.*?>', '', d)
                iz = (title,author_journal,year,desc,"https://scholar.google.com/scholar?cluster="+c_code)
                di[int(n_cites)]=iz

#get others
#sort total
for a,b in sorted(di.items(), key=lambda x: x[0], reverse=True):
    print('=======================================\n')
    print(a)
    for n in range(0,5):
        print('\n')
        print(b[n])
