def classify_char(char):
  if len(char)==1 and char.isalpha():
    if char in 'aeiou':
      print('Vowel')
    else:
      print('consonant')
  else:
    print('neither')
char=input("Enter a char:").lower()
classify_char(char)
