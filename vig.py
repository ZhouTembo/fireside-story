import string

class Vigenere:
  def __init__(self,text):
    self.has=text
  
  def encrypt(self,rot):
    but=''
    for num in range(len(string.ascii_lowercase)):
      but+=string.ascii_lowercase[num]
    
    k=0
    
    group1=''
    m=len(rot)
    print(ord('a'), ord('z'), ord('A'),ord('Z'))

    for i in self:
      if i in string.ascii_letters:
        m=k%4
        l=(ord(i)+but.index(rot[m]))
        
        if ord(i) in range(65,90):
          while l>90:
            l=(l%90)+64
        if ord(i) in range(97,122):
          while l>122:
            l=l%122+96
        if ord(i)==32 or i in string.punctuation:
          l=ord(i)
        k+=1
        print (i,rot[m],chr(l))
        group1+=chr(l)
      else:
        group1+=i
       
    print(group1)