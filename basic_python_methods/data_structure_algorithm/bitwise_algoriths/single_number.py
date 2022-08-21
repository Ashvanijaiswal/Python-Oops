def singleNumber(A):
    result=0
    st=set()
    array_sum=0
    for i in A:
        st.add(i)
        array_sum+=i
    max_sum=sum(st)*3
    print(max_sum)

    return (max_sum-array_sum)//2

print(singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))
