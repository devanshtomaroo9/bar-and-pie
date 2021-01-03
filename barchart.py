import matplotlib.pyplot as plt
import numpy as np
def graph():
    x=["Kavi","Roni","Ethan","Mani","Jaz"]
    y=[94,85,25,50,54]
    y1=[78,100,67,89,90]
    y2=[78,100,67,89,90]      
    i=np.arange(1,10,2)
    print("VALUES=",i)
    plt.xticks(i,x)
    plt.bar(i+0.5,y,width=0.5,color="black",label="CHEMISTRY MARKS")
    plt.bar(i,y1,width=0.5,label="CS MARKS")
    plt.legend()
    plt.xlabel("Student Name")
    plt.ylabel("Student'S Marks")
    plt.title("STUDENT'S DATA")
    plt.grid()
    plt.show()
graph()    
    
