


password = 'monero'

'''
for i in range(1, 100):
    a = file.readlines(i)
    print(a)'''
with open('passwords.txt', 'r') as f:
    nums = f.read().splitlines()
with open('passwords2.txt', 'r') as f:
    nums2 = f.read().splitlines()

#print(nums)

try:
    for  i in range(1000000000):
        a = nums[i]
        if password == a:
            print(nums[i])
            exit()
        else:
            a = nums[i]
    for  i in range(1000000000):
        a = nums2[i]
        if password == a:
            print(nums2[i])
            exit()
        else:
            a = nums2[i]
except:    
    print("Password val succses")
