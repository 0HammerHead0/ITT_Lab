# s = "this is hello world hello is this a world"

# map = {}
# for i in s.split(' '):
#     # map[i]+=1
#     if(i in map.keys()):
#         map[i]+=1
#     else:
#         map[i]=1
# map2 = {'a': 1, 'b': 10, 'c': 2}
# val_map2 = list(map2.values())
# key_map2 =list(map2.keys())
# for i in range(len(val_map2)):
#     for j in range(i,len(val_map2)-1):
#         if(val_map2[j]>val_map2[j+1]):
#             key_map2[j],key_map2[j+1] = key_map2[j+1],key_map2[j]
#             val_map2[j],val_map2[j+1] = val_map2[j+1],val_map2[j]
# # print(key_map2)
# sorted_keys = sorted(map2, key=lambda k: map2[k])
# # print(sorted_keys)
# s = "Mississippi Alabama Texas Massachusetts Kansas"
# statesList = ['']*5
# print(statesList)
# for i in s.split():
#     if(i.endswith('xas')):
#         statesList[0] = i
#     if(i.startswith('k') and i.endswith('s')):
#         statesList[1] = i
#     if(i.startswith('M') and i.endswith('s')):
#         statesList[2] = i
#     if(i.endswith('a')):
#         statesList[3] = i
#     if(i.startswith('M')):
#         statesList[4] = i
# print(statesList)

# import re

# pattern = re.compile(r'^k.{4}s$', re.I)

# statesList = ['Kansas', 'California', 'Texas', 'New York']

# for i in statesList:
#     if pattern.match(i):
#         print(f"Match: {i}")

# m = 2
# n = 10
# def isPrime(n):
#     for i in range(2,n):
#         if(n%i==0):
#             return True
#     return False
# for i in range(m,n+1):
#     if(not isPrime(i)):
#         print(i)

lis = [1, 3, 1, 5, 3, 7]
# for i in lis:
#     if(lis.count(i)>1):
#         lis.remove(i)
# print(lis)

# for i in range(len(lis)-1,-1, -1):
#     print(lis[i], end=' ')


s = 'this is a random string with a repeating word a'
words = {}
for i in s.split():
    if(i not in words.keys()):
        words[i]=1
    else:
        words[i]+=1
chars={}
for i in s:
    if(i not in chars.keys() ):
        chars[i]=1
    else:
        chars[i]+=1
print(chars)
print(words)