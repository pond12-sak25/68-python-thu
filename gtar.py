def shell_sort(arr):
    
    n = len(arr)
    gap = n // 2   # ระยะห่างเริ่มต้น

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i

            # เปรียบเทียบแบบ insertion sort
            #ข้าม gap
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = temp

        gap //= 2   # ลด gap ลง