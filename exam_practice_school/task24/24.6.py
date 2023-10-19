# with open('24.6.txt') as f:
#     f=f.readline()
# c=0
# mx=0
# vovels='AO'
# consonants='CDF'
# for i in range(len(f)-3):
#     if f[i] in vovels and f[i+1] in vovels and f[i+2] in consonants:
#         c+=1
#         mx=max(c, mx)
#     else:
#         c=0
# print(mx)

# f=open('24.6.txt')
# s=f.read()
# maxi=0
# c=0
# i=0
# while i < len(s)-2:
#     if s[i] in "AO" and s[i+1] in 'AO' and s[i+2] in 'CDF':
#         c+=1
#         maxi=max(maxi,c)
#         i+=2
#     else:
#         c=0
#         i+=1
# print(maxi)