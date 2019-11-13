import string
class caesar:
  def __init__(self,text):
    self.has=text
    
  def encrypt(self,rot):
    for i in self:
      if i in string.punctuation or ord(i)==32:
            new_let=ord(i)
            print(chr(new_let))
      if i in string.ascii_lowercase:
        new_let=(ord(i)+ rot)
        if new_let>122:
          new_let=(new_let%122)+96
        print(chr(new_let))
      if i in string.ascii_uppercase:
        
        new_let=(ord(i)+ rot)
        if new_let>90:
          new_let=(new_let%90)+64
        print (chr(new_let))
    
def main(self,rot):
    caesar.encrypt(self,rot) 
    



if __name__ == "__main__":
    main()