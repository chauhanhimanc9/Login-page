from tkinter import*
from tkinter import messagebox
import ast

root=Tk()
root.title('LOGIN')
root.state('zoomed')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=pwd.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        text=Label(screen,text='Hello Everyone...',fg='black',bg='white',font=('Microsoft YaHei UI Light',50,'bold'))
        text.pack(expand=True)

        screen.mainloop()
        
    else:
        message.showerror('Invalid','Invalid Username or Password')

        
#signup------------------------------------
def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.state('zoomed')
    window.configure(bg='#fff')
    window.resizable(False,False)

    def sign_up():
        username=user.get()
        password=pwd.get()
        confirm_password=confirm_pwd.get()

        if password==confirm_password:
        
                try:
                    file= open('datasheet.txt','r+')  #if file is available then it will read the file and write the data
                    d=file.read()
                    r= ast.literal_eval(d)

                    dict2={username:password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file= open('datasheet.txt','w')
                    w=file.write(str(r))

                    messagebox.showinfo('SignUp','Sucessfully Sign Up')
                    window.destroy()

                except:    #what if file is not available then it will create the file
                    file= open('datasheet.txt','w')
                    pp=str({'username':'password'})
                    file.write(pp)
                    file.close()

        else:
                messagebox.showerror('Invalid','Both Password should match')
            
    def sign():
        window.destroy()
    
    img= PhotoImage(file="C:/Users/user/Downloads/login (1).png")
    Label(window,image=img,border=0,bg='white').place(relx=.2,rely=.3)

    frame=Frame(window,width=500,height=450,bg='white')
    frame.place(relx=.5,rely=.2)

    heading=Label(frame,text='Sign Up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(relx=.3,rely=.1)

#username ------------------------------------

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')
        
        


    user=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(relx=.1,rely=.3)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)


    Frame(frame,width=350,height=2,bg='black').place(relx=.1,rely=.35)

# passwrd-------------------------
    def on_enter(e):
        pwd.delete(0,'end')
    def on_leave(e):
        if pwd.get()=='':
          pwd.insert(0,'password')
        
        


    pwd=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    pwd.place(relx=.1,rely=.4)
    pwd.insert(0,'Password')
    pwd.bind("<FocusIn>",on_enter)
    pwd.bind("<FocusOut>",on_leave)


    Frame(frame,width=350,height=2,bg='black').place(relx=.1,rely=.45)

#confirm passwrd-------------------------
    def on_enter(e):
        confirm_pwd.delete(0,'end')
    def on_leave(e):
        if confirm_pwd.get()=='':
           confirm-pwd.insert(0,'Confirm Password')
        
        


    confirm_pwd=Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    confirm_pwd.place(relx=.1,rely=.5)
    confirm_pwd.insert(0,'Confirm Password')
    confirm_pwd.bind("<FocusIn>",on_enter)
    confirm_pwd.bind("<FocusOut>",on_leave)


    Frame(frame,width=350,height=2,bg='black').place(relx=.1,rely=.55)

#Button--------------------------

    Button(frame,width=40,pady=7,text='Sign Up',bg="#57a1f8",fg='white',border=0,command=sign_up).place(relx=.15,rely=.65)

    label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(relx=.3,rely=.75)


    sign_in=Button(frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    sign_in.place(relx=.5,rely=.75)

    window.mainloop()


#----------------sign in login-----------------


    
img=PhotoImage(file="C:/Users/user/Downloads/login.png")
Label(root,image=img,bg='white').place(relx=.2,rely=.3)

frame=Frame(root,width=500,height=450,bg='white')
frame.place(relx=.5,rely=.3)

heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(relx=.3,rely=.1)


#-----------------------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')



user = Entry(frame,width=40,fg='black',bd=0,bg='white',font=('Microsoft YaHei UI Light',12))
user.place(relx=.1,rely=.3)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=350,height=2,bg='black').place(relx=.1,rely=.35)

#----------------------------

def on_enter(e):
    pwd.delete(0,'end')

def on_leave(e):
    name=pwd.get()
    if name=='':
        pwd.insert(0,'password')

pwd = Entry(frame,width=35,fg='black',bd=0,bg='white',font=('Microsoft YaHei UI Light',12))
pwd.place(relx=.1,rely=.4)
pwd.insert(0,'password')
pwd.bind('<FocusIn>',on_enter)
pwd.bind('<FocusOut>',on_leave)



Frame(frame,width=350,height=2,bg='black').place(relx=.1,rely=.45)

#sign in---------------------------------------------
sign_in=Button(frame,width=40,pady=9,text='Sign In',bg='#57a1f8',fg='white',bd=0,command=signin)
sign_in.place(relx=.15,rely=.55)

label=Label(frame,text="Don't Have an Account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',12)) 
label.place(relx=.17,rely=.7)

#sign up--------------------------

sign_up=Button(frame,width=6,text="Sign Up",bd=0,fg='#57a1f8',bg='white',cursor='hand2',command=signup_command,font=('Microsoft YaHei UI Light',11,'bold'))
sign_up.place(relx=.55,rely=.7)















             
root.mainloop()
