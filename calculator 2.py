from tkinter import *
root=Tk()
m=["red","yellow","blue","navy","green","purple","cyan","black","white","orange"]
n=m[8]

root.config(bg=n)
root.title("ماشین حساب")
equation=StringVar()
h=Label(root, textvariable=equation, font=("Tohoma",20),bg=n, pady=10,padx=10)

h.grid(columnspan=6)

def colortheme():
    global n
    l=m.index(n)        
    n=m[l-1]
    global h
    h.config=Label(root, textvariable=equation, font=("Tohoma",30),bg=n, pady=10,padx=10)
    root.config(bg=n)
equation.set(" ")
    
def set_number(num):
        
    if equation.get()=="":
        equation.set(" ")
        equation.set(equation.get()+num)
        
    elif  equation.get()[-1] in "*/+-" and num in "*/+-" or  len(equation.get())>25 :
        t=len(equation.get())
        l=equation.get()[:(t-1):1]
        equation.set(l+num)
        
    else:   
        equation.set(equation.get()+num)
    
def back_space():
    t=len(equation.get())
    l=equation.get()[:(t-1):1]
    equation.set(l)
    
def squareroot():
    equation.set(eval(equation.get())**0.5)

def calculate_equation():
    if equation.get()[-1]=="0" and equation.get()[-2]=="/":
        equation.set("ERORR")    
    # eq=equation.get()
    # result=eval(eq)
    # equation.set(result)
    else: 
        equation.set(eval(equation.get()))


btn1=Button(root,text="1",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('1'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn1.grid(row=1, column=0)

btn2=Button(root,text="2",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('2'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn2.grid(row=1, column=1)
btn3=Button(root,text="3",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('3'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn3.grid(row=1, column=2)
btn4=Button(root,text="4",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('4'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn4.grid(row=2, column=0)
btn5=Button(root,text="5",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('5'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn5.grid(row=2, column=1)
btn6=Button(root,text="6",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('6'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn6.grid(row=2, column=2)
btn7=Button(root,text="7",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('7'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn7.grid(row=3, column=0)
btn8=Button(root,text="8",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('8'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn8.grid(row=3, column=1)
btn9=Button(root,text="9",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('9'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn9.grid(row=3, column=2)
btn0=Button(root,text="0",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('0'),activebackground="navy",activeforeground="cyan",bg="cornflowerblue")
btn0.grid(row=4, column=1)

btnclear=Button(root,text="c",width=5,height=2, font=("Tohoma",20 ),bg='khaki',command=lambda:equation.set(''))
btnclear.grid(row=4, column=0)
btnequal=Button(root,text="=",width=5,height=2, font=("Tohoma",20),command=calculate_equation,bg="aquamarine")
btnequal.grid(row=4, column=5)
btnplus=Button(root,text="+",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('+'),activebackground="navy",activeforeground="cyan",bg="orange")
btnplus.grid(row=1, column=3)
btnsub=Button(root,text="*",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('*'),bg="lime")
btnsub.grid(row=2, column=3)
btnmul=Button(root,text="-",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('-'),bg="mediumslateblue")
btnmul.grid(row=3, column=3)
btndivid=Button(root,text="/",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('/'),bg="darkgrey")
btndivid.grid(row=4, column=3)

btnbackspace=Button(root,text="←",width=5,height=2, font=("Tohoma",20),bg="yellow" ,command=back_space)
btnbackspace.grid(row=1, column=5)

btnsqureroot=Button(root,text="√",width=5,height=2, font=("Tohoma",20),bg="pink", command=squareroot)
btnsqureroot.grid(row=2, column=5)

btndot=Button(root,text=".",width=5,height=2, font=("Tohoma",20),command=lambda:set_number('.'),bg="tomato")
btndot.grid(row=4, column=2)

btncolor=Button(root,text="theme",width=5,height=2, font=("Tohoma",20),command=colortheme,bg="red")
btncolor.grid(row=3, column=5)
mainloop()