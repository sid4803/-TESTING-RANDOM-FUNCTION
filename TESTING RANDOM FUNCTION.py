from tkinter import *
import random
root=Tk()
root.title("TESTING RANDOM FUNCTION")
root.geometry("300x400")
root.configure(bg="#e65a09")
lable=Label(root)
array_3d=[[[1,2,3,4,5,6],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][1][0])
def newpassword():
    r1=random.randint(0,5)
    r2=random.randint(0,1)
    r3=random.randint(0,7)
    l1=str(array_3d[0][0][r1])
    l2=array_3d[0][1][r2]
    l3=array_3d[0][2][r3]
    lable["text"]=l1+" "+l2+" "+l3
btn=Button(root,text="NEW Password",command=newpassword)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
lable.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()