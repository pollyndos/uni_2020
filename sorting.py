from collections import defaultdict, Counter

a = 'qwertyuiopasdfghjklzxcvbnmMNBVCXZLKJHGFDSAPOIUYTRREWQ10255120'
sorted_ch = sorted(a)
sorted_str = ''.join(sorted_ch)
print(sorted_str)

count = Counter()
alpha = ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for char in alpha:
    count[char] = 0
for char in a:
    count[char] += 1 
counter_str = ''.join(count.elements())
print(counter_str)
print(sorted_str == counter_str)
    
defaultdict = defaultdict()
for char in alpha:
    defaultdict[char] = 0
for char in a:
    defaultdict[char] += 1
dict_str = ''.join([k * v for k, v in defaultdict.items()])   
print(dict_str)
print(sorted_str == dict_str)
