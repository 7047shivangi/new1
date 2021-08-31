if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_list = list(arr)
my_list.sort()
l1=my_list
l1.reverse()
l2=l1

for i in range(n):
    if l2[i]>l2[i+1]:
        print(l2[i+1])
        break
