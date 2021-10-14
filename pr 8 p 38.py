s='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
s1=s2=s3=s
for l in range(0, len(s1)-2,2):
    print(chr(ord(s1[l])+1))
while (s2.find('Z')>=0):
    s2[s2.find('Z')+1]='A'
print(s2)
while (s3.find(' ')>=0):
    s3[s3.find(' ')+1]='-'
print(s3)