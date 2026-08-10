def reverse_string(value):
   reversed_str = ""
   for char in value:
       reversed_str = char + reversed_str
   return reversed_str
# print(reverse_string("ba"))

listsn = [1,2,3,4,"a","b","c","d"]
nwln = listsn[1:2]

print(len(nwln))