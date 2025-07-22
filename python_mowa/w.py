def market(file):
    with open(file,'r') as f:
        read=f.read()
        lst=read.split()
        dic={}
        for i in range(0,len(lst),2):
            if lst[i+1].isnumeric():
                dic[lst[i]]=int(lst[i+1])
            else:
                dic[lst[i]]=lst[i+1]
        total=0
        for key in dic:
            if key != 'Discount' or key != 'discount':
                if isinstance(dic[key], int):
                    total += dic[key]
        print(f'Items purchased: {len(dic)}')
        print(f'Total Amount purchased: {total}')
        free_items = sum(1 for value in dic.values() if isinstance(value, str) and value.lower() == 'free')
        print(f'Free items: {free_items}')
        discount = dic.get('Discount', 0)
        print(f'Discount: {discount}')
        print(f'Final Amount: {total - discount}')
        print(f'Items purchased: {", ".join(dic.keys())}')
market(input("Enter the file name: "))