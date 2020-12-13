def method1(lst1):
    lst1.reverse()
    print(lst1)

def method2(lst2):
    n = len(lst2)
    for i in range(n//2):
        lst2[i],lst2[n-1-i] = lst[n-1-i],lst[i]
    print(lst2)

print("Enter elements.")
lst1 = lst(map(int,input().split()))
lst1 = lst.copy()
lst2 = lst.copy()

method1(lst1)
method2(lst2)