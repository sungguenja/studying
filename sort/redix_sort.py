def countingsort(arr,digit):
    n = len(arr)

    # 배열의 크기에 맞게 result 생성 자릿수에 이용하는 10길이짜리 배열
    result = [0]*n
    count = [0]*10

    for i in range(n):
        count[(int(arr[i]/digit))%10] += 1
    
    # count 배열을 수정해 digit으로 잡은 포지션을 설정
    for i in range(1,10):
        count[i] += count[i-1]
        print(i,count[i])
    
    i = n-1
    print(count)
    print(result)
    while i>=0:
        index = int(arr[i]/digit)
        result[count[index%10]-1] = arr[i]
        count[index%10] -= 1
        i -= 1
        print(count)
        print(result)
    
    for i in range(n):
        arr[i] = result[i]
    print(arr)

def radixsort(arr):
    maximum = max(arr)
    digit = 1
    while int(maximum/digit) > 0:
        countingsort(arr,digit)
        digit *= 10

arr = [180,7513,54,1,9754,123,446,10]
radixsort(arr)
print(arr)