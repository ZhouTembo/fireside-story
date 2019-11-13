import string
def alphabet_position():
    but=''
    for num in range(len(string.ascii_lowercase)):
        but+=string.ascii_lowercase[num]
    return but[num]
def rotate_character(char,rot):
  if i in string.ascii_lowercase:
        new_let=(ord(i)+ rot)
        if new_let>122:
          new_let=(new_let%122)+96
        group+=(chr(new_let))
      if i in string.ascii_uppercase:
        
        new_let=(ord(i)+ rot)
        if new_let>90:
          new_let=(new_let%90)+64
        group+= (chr(new_let))
    return group
  