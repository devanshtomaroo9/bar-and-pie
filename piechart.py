import matplotlib.pyplot as plt
def graph():
    con=["United States","Great britain","China       ","Russia      ","Germany     "]
    gold=[46,27,26,19,17]
    colors=['r','y','g','c','b']
    plt.pie(gold,labels=con,colors=colors,shadow=True,startangle=90,explode=[0.1,0,0,0,0],autopct='%1.1f%%')
    plt.legend()
    print("\t","*"*45)
    plt.title("Gold Medal of Olympics 2016")
    print("\t          SUMMER OF OLYMPICS 2016 RECORDS")
    print("\t","*"*45)
    print("\t\tCOUNTRY \tGOLD MEDALS")
    print("\t","*"*45)
    for i in range(0,5):
        print("\t\t",con[i],"\t   ",gold[i])
    print("\t","*"*45)
    plt.show()
    
  
graph()
