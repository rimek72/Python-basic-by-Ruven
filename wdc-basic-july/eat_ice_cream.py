from icecream import Scoop, Bowl

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

print(s1.flavor)  # chocolate

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)   # chocolate, vanilla, coffee

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)
b.add_scoops(s6)
print(len(b.scoops))  # 3
print(b.flavors())   # ['chocolate', 'vanilla', 'coffee']


print(s1)
print(s2)
print(s3)

print('****   Below here is "print b"  *****')
print(b)

print(len(b))

b2 = Bowl()
b2.add_scoops(s1, s3, s2)
print(b == b2)
