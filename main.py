from tkinter import *

root = Tk()

input_var = StringVar()
rem_var = StringVar()

input_var.set("0")

root.resizable(False,False)
root.title("Python Calculator")
root.geometry("400x300")
root["bg"]="#454545"

input_label = Label(root, textvariable=input_var, font=20, anchor="w", justify=LEFT, height=2, width=35)
input_label.place(x=5,y=10)
input_label["bg"]="grey"

rem_label = Label(root, textvariable=rem_var, font=20, height=2, width=6)
rem_label.place(x=332,y=10)
rem_label["bg"]="grey"

one_btn = Button(root, text="1", font=20, height=2, width=10)
one_btn.place(x=5,y=60)
one_btn["bg"]="grey"

two_btn = Button(root, text="2", font=20, height=2, width=10)
two_btn.place(x=115,y=60)
two_btn["bg"]="grey"

three_btn = Button(root, text="3", font=20, height=2, width=10)
three_btn.place(x=225,y=60)
three_btn["bg"]="grey"

four_btn = Button(root, text="4", font=20, height=2, width=10)
four_btn.place(x=5,y=120)
four_btn["bg"]="grey"

five_btn = Button(root, text="5", font=20, height=2, width=10)
five_btn.place(x=115,y=120)
five_btn["bg"]="grey"

six_btn = Button(root, text="6", font=20, height=2, width=10)
six_btn.place(x=225,y=120)
six_btn["bg"]="grey"

seven_btn = Button(root, text="7", font=20, height=2, width=10)
seven_btn.place(x=5,y=180)
seven_btn["bg"]="grey"

eight_btn = Button(root, text="5", font=20, height=2, width=10)
eight_btn.place(x=115,y=180)
eight_btn["bg"]="grey"

nine_btn = Button(root, text="6", font=20, height=2, width=10)
nine_btn.place(x=225,y=180)
nine_btn["bg"]="grey"

zero_btn = Button(root, text="0", font=20, height=2, width=10)
zero_btn.place(x=5,y=240)
zero_btn["bg"]="grey"

clr_btn = Button(root, text="C", font=20, height=2, width=5)
clr_btn.place(x=335,y=60)
clr_btn["bg"]="grey"

sum_btn = Button(root, text="+", font=20, height=2, width=5)
sum_btn.place(x=335,y=120)
sum_btn["bg"]="grey"

sub_btn = Button(root, text="-", font=20, height=2, width=5)
sub_btn.place(x=335,y=180)
sub_btn["bg"]="grey"

multi_btn = Button(root, text="*", font=20, height=2, width=5)
multi_btn.place(x=335,y=240)
multi_btn["bg"]="grey"

div_btn = Button(root, text="/", font=20, height=2, width=10)
div_btn.place(x=225,y=240)
div_btn["bg"]="grey"

dot_btn = Button(root, text=".", font=20, height=2, width=10)
dot_btn.place(x=115,y=240)
dot_btn["bg"]="grey"

root.mainloop()