coins = 0
while coins < 50:
    coin = int(input("Insert Coin: ").strip())
    if coin == 25 or coin == 10 or coin == 5:
        coins += coin
        if coins < 50:
            t_coins = 50 - coins
            print(f"Amount Due: {t_coins}")
        else:
            t_coins = coins - 50
            print(f"Change Owed: {abs(t_coins)}")
            break
    else :
        print("Amount Due:",50)