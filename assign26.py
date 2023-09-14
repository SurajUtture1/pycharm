def histogram(st):
    for i in st:
        print(i * '*')


st = []
lin = int(input("Enter the list length :- "))
print("Enter integer = ", lin)
for i in lin:
    data = int(input())
    st.append(data)
histogram(st)
