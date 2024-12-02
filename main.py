import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='Rahul@*123456',database="BANK_MANAGEMENT")

def openacc():
    n=input('enter the name:')
    an=input('enter the account number:')
    db=input('enter the date of birth:')
    ad=input('enter the address:')
    cn=input('enter the contact number:')
    ob=int(input('enter the opning balance:'))
    data1=(n,an,db,ad,cn,ob)
    data2=(n,an,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values (%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print('entered successfully')
    main()

def DepositeAM():
    amount=int(input("enter the amount:"))
    acc=input("enter the acc number:")
    b="select opning_bal from amount where Account_Number=%s"
    dta=(acc,)
    x=mydb.cursor()
    x.execute(b,dta)
    result=x.fetchone()
    r=result[0]+ amount
    sql=("UPDATE amount SET opning_bal = %s WHERE Account_Number = %s")
    d=(r,acc)
    x.execute(sql,d)
    mydb.commit()
    main()


def WithdrawAm():
    amount=input("enter the amount you want to withdraw:")
    acc=input("enter the acc number:")
    try:
        amount = int(amount)
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return 

    b="select opning_bal from amount where Account_Number=%s"
    dta=(acc,)
    x=mydb.cursor()
    x.execute(b,dta)
    result=x.fetchone()
    r=int(result[0])-int(amount)
    sql=("UPDATE amount SET opning_bal = %s WHERE Account_Number = %s")
    d=(r,acc)
    x.execute(sql,d)
    mydb.commit()
    main()

def  BalanceEnq():
    ac=input('enter the account number:')
    w="select * from amount where Account_Number=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(w,data)
    result=x.fetchone()
    print("balance amount:",result[-1])
    main()


def DsplayCustomerDet():
    ac=input('enter the account number:')
    a="select * from account where Account_Number=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    ad=input("enter the account number:")
    sql1="select * from amount where Account_Number=%s"
    sql2='select * from account where Account_Number=%s'
    data=(ad,)
    x=mydb.cursor()
    x.execute(sql1,data)
    result1=x.fetchall()
    if not result1:
        print("Account not found in amount table.")
        return

    x.execute(sql2,data)
    result2=x.fetchall()
    if not result2:
        print("Account not found in amount table.")
        return
    mydb.commit()
    main()



def main():
    print('''
        1.Open New Account
        2.deposite Amount
        3.withdraw Amount
        4.Balance enquiry
        5.Display Customer Details
        6.Close an Account           
          ''')
    
    choice=input("Enter the task you want to perform:")
    if choice=="1":
        openacc()
    elif choice=="2":
        DepositeAM()
    elif choice=='3':
        WithdrawAm()
    elif choice=="4":
        BalanceEnq()
    elif choice=="5":
        DsplayCustomerDet()
    elif choice=="6":
        CloseAcc()
    else:
        print("Unable open the Account")
        main()
main()



