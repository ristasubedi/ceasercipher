import sys
no_of_shift = int(sys.argv[1])
message = sys.stdin.read()
msg = ''
for letter in message:
  if letter.isalpha():
    msg += letter
# print()
final = ""
# print(no_of_shift)
upperCased_messsage =msg.upper()
# print(upperCased_messsage)
for letter in upperCased_messsage:
  if ord(letter) + no_of_shift > 90:
    num = ord(letter) - 26 + no_of_shift
    i = chr(num)
    final += i
  else:
    num = ord(letter) + no_of_shift
    i = chr(num)
    final += i
lst = []
count = ""
curr_len = 0
for let in final:
  count += let
  curr_len += 1
  if len(count) % 5 == 0:
    lst.append(count)

    count = ""
  
  elif len(final) == curr_len:
    lst.append(count) 
total = 0
last = 0
lst2 = []
again = []
for item in lst:
  last += 1
  total += 1
  lst2.append(item)
  if total % 10 == 0:
    again.append(" ".join(lst2))
    lst2 = []
  elif len(lst) == last:
    again.append(" ".join(lst2))
for line in again:
  print(line)

  



