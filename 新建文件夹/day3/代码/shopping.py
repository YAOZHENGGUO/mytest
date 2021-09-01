# author:Iron Qi
product_list = [('Iphone', 5800),
                ('Mac Pro', 9800),
                ('Play Game', 1000),
                ('Watch', 4300),
                ('Basketball', 260),
                ('cloth', 1314)
               ]
shopping_list = []    # 商品购物车是空表
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):    # 取列表的下标和实际属性
            print(index, item)
        user_choice = input("Please select the item you want to buy:")     # 选择的是商品编号
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_price = product_list[user_choice]
                if p_price[1] <= salary:  # can buy
                    shopping_list.append(p_price)
                    salary -= p_price[1]
                    print("Added %s into shopping cart,your balance is \033[31;1m%s\033[0m" % (p_price, salary))
                else:
                    print("\033[32;1myour balance only is[%s]，No longer available\033[0m" % salary)
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print("---------shopping list---------")
            for p in shopping_list:
                print(p)
            print("your current balance:", salary)
            exit()
        else:
            print("invalid option")
else:
    print("\033[33;1mYour input is not valid\033[0m")