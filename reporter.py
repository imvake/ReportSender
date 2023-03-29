from tkinter import *
from tkinter import messagebox
from datetime import date
import pywhatkit
from datetime import datetime
import threading


global final_dict

final_dict = {}

root = Tk()
root.geometry('680x500')
root.title("Altarteel")


def reports():
    int(entrypatientop.get()), float(entryopthal.get()), int(entrypatientdental.get()), float(entrydental.get()), int(entrypatientgp.get()), float(entrygp.get()), float(entrysales.get()) , float(entrycash.get()), float(entryremcash.get())

    total = (float(entryopthal.get()) + float(entrydental.get()) + float(entrygp.get()) + float(entrysales.get()))
    
    float(total)

    visa = total - float(entrycash.get())

    curdate = date.today()

    dt = datetime.now()
    today = dt.strftime('%A')
    if today == "Saturday":

        today = "السبت"
    elif today == "Sunday":
        today = "الأحد"
    elif today == "Monday":
        today = "الإثنين"
    
    elif today =="Tuesday":
        today = "الثلاثاء"
        
    elif today == "Wednesday":
        today = "الأربعاء"
    
    elif today == "Thursday":

        today = "الخميس"
    
    elif today == "Friday":
        today = "الجمعة"

    
         



    report = (f" السلام عليكم ورحمة الله وبركاته -- تقرير مجمع الترتيل الطبي اليومي \n\n اليوم {today}  \n\n{curdate}\n  \nالفترة \ {shift.get()}\n\n ١- عيادة العيون عدد {entrypatientop.get()} مرضى دفع مبالغ {entryopthal.get()} ريال عماني  \n\n٢-عيادة الأسنان عدد  {entrypatientdental.get()}  مرضى دفع مبالغ  {entrydental.get()} ريال عماني   \n \n٣- عيادة الطب العام عدد {entrypatientgp.get()} مرضى دفعوا مبالغ {entrygp.get()} ريال عماني  \n \n ٤- مبيعات بقيمة {entrysales.get()} ريال عماني \n\n مجموع الإيرادات المالية لهذه الفترة هو  {total} \n\n ريالات عمانية كاش : {entrycash.get()} \nبطاقة : { visa } \n\nمبلغ الكاش الموجود {entryremcash.get()} ريال عماني  ")

    Number = number.get()
    pywhatkit.sendwhatmsg_instantly(Number, report)



def Send():
    mythreads = threading.Thread(target=reports)


    mythreads.start()


def Add():
    opthal_patients, opthal_money, dental_patients, dental_money, gp_patients, gp_money = entrypatientop.get(
    ), entryopthal.get(), entrypatientdental.get(), entrydental.get(), entrypatientgp.get(), entrygp.get()
    temp = {}
    temp['noop'] = opthal_patients
    temp['moneyop'] = opthal_money
    temp['noden'] = dental_patients
    temp['moneyden'] = dental_money
    temp['nogp'] = gp_patients
    temp['moneygp'] = gp_money
    

    all_items = final_dict.values()

    if temp in all_items:
        messagebox.showinfo("Add Dialog", "Information is already there ")
    else:
        final_dict[str(len(final_dict)+1)] = temp
        messagebox.showinfo("Add Dialog", "New Information Added Successfully")


#############################################################


def Reset():
    entrypatientop.delete(0, 999)
    entryopthal.delete(0, 999)
    entrypatientdental.delete(0, 999) 
    entrydental.delete(0, 999)
    entrypatientgp.delete(0, 999)
    entrygp.delete(0, 999)
    entrysales.delete(0,999)
    entryremcash.delete(0, 999)
    entrycash.delete(0, 999)


# lable top
Label(root, text="AlTarteel Medical Complix Reports", font=(
    "bold", 30), anchor=CENTER, background="gold", width=28, heigh=1).place(x=10, y=5)


# opthal  lable
lblpatientop = Label(root, text="eyes Patients", width=15, font=("bold", 9))
lblpatientop.place(x=10, y=60)


entrypatientop = Entry(root, width=50, font=("bold", 9))
entrypatientop.place(x=150, y=60)


# opthal money lable
lblopthal = Label(root, text="eyes Money", width=15, font=("bold", 9))
lblopthal.place(x=10, y=90)


entryopthal = Entry(root, width=50, font=("bold", 9))
entryopthal.place(x=150, y=90)


# Dental Patients
lblpatientdental = Label(
    root, text="Dental Patients", width=15, font=("bold", 9))
lblpatientdental.place(x=10, y=120)


entrypatientdental = Entry(root, width=50, font=("bold", 9))
entrypatientdental.place(x=150, y=120)


# Dental Money
lbldental = Label(root, text="Dental Money", width=15, font=("bold", 9))
lbldental.place(x=10, y=150)


entrydental = Entry(root, width=50, font=("bold", 9))
entrydental.place(x=150, y=150)


# GP Patients
lblpatientpatientgp = Label(
    root, text="GP Patients", width=15, font=("bold", 9))
lblpatientpatientgp.place(x=10, y=180)


entrypatientgp = Entry(root, width=50, font=("bold", 9))
entrypatientgp.place(x=150, y=180)


# GP Money
lblgp = Label(root, text="GP Money", width=15, font=("bold", 9))
lblgp.place(x=10, y=210)


entrygp = Entry(root, width=50, font=("bold", 9))
entrygp.place(x=150, y=210)


# Sales Money
lblsales = Label(root, text="Sales Money", width=15, font=("bold", 9))
lblsales.place(x=10, y=240)


entrysales = Entry(root, width=50, font=("bold", 9))
entrysales.place(x=150, y=240)


# Paid cash
lblcash = Label(root, text="Paid Cash", width=15, font=("bold", 9))
lblcash.place(x=10, y=270)


entrycash = Entry(root, width=50, font=("bold", 9))
entrycash.place(x=150, y=270)



# remaining cash
lblremcash = Label(root, text="Remaining Cash", width=15, font=("bold", 9))
lblremcash.place(x=10, y=300)


entryremcash = Entry(root, width=50, font=("bold", 9))
entryremcash.place(x=150, y=300)


# Number
lblnumber = Label(root, text="Enter Number", width=15,  font=("bold", 9))
lblnumber.place(x=10, y=330)


number = StringVar()
Radiobutton(root, text="", variable = number, value = "+").place(x=150, y=330)
Radiobutton(root, text="",  variable = number, value = "+").place(x=250, y=330)


# time
# label4 = Label(root, font=20, fg="white", bg="black")
# label4.grid(row=1, padx=10, pady=10)
# label4.place(x=290,
#              y=330)


# now time

# def localtime():
#     t = time.localtime()
#     current_time = time.strftime("%H:%M:%S", t)
#     label4.config(text="Localtime:"+current_time)
#     label4.after(200, localtime)


# localtime()

# # hrs
# entry3 = (Entry(root, width=20))
# entry3.insert(0, "15")
# entry3.grid(row=1, column=1, columnspan=1, padx=5, pady=13)
# entry3.place(x=150,
#              y=330)

# # mins
# entry4 = (Entry(root, width=20))
# entry4.insert(0, "20")
# entry4.grid(row=1, column=1, columnspan=1, padx=5, pady=13)
# entry4.place(x=150,
#              y=360)

shiftlbl = Label(root, text="Shift", width=15 ,font=("bold",9)).place(x=30 , y=350)
shift = StringVar()
Radiobutton(root, text="Morning", variable = shift, value = "الصباحية").place(x=150,y=350)
Radiobutton(root, text="Evening",  variable = shift, value = "المسائية").place(x=250, y=350)


#######################################################################################
# buttons
Button(root, text='Send', width=10, background='silver',
       fg='black', command=Send).place(x=180, y=470)
Button(root, text='Reset', width=10, background='silver',
       fg='black', command=Reset).place(x=300, y=470)
# Button(root, text='Display', width=10, background='silver',
#        fg='black', command=Display).place(x=420, y=420)
Button(root, text='Add', width=10, background='silver',
       fg='black', command=Add).place(x=420, y=470)


# Shahla & Alwaleed Buttons 
# Button(root, text='Shahlaa', width=7, background='white',
#        fg='black', command=Shahlaa).place(x=500, y=300)
# Button(root, text='Alwaleed', width=7, background='white',
#        fg='black', command=Alwaleed).place(x=570, y=300)



       


#####################################################################################


# displaying data
# labeldisplying_data = Label(root, text="", width=100, font=("bold", 9))
# labeldisplying_data.place(x=10, y=450)


root.mainloop()
