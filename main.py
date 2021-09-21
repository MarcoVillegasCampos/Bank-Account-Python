from Account import Account



michaelAccount= Account(0.1)
alvaroAccount= Account(0.2)


michaelAccount.deposit(5000).deposit(1000).deposit(1000).withdraw(500).yield_interest().displayAccountInfo()


alvaroAccount.deposit(10000).deposit(1000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().displayAccountInfo()

Account.printAllAccountInfo()













