from tkinter import *
import qrcode
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



# MySQL connection setup
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akash@123",
    database="form_data"
)
cursor = conn.cursor()

root=Tk()
root.title("Akash kumar ")
root.geometry("600x480")
root.minsize(600,480)
root.maxsize(600,480)
root.configure(bg="#2E8B57")
ti=Label(text="AK Travel Agency",font="Calibri 22 bold ", border=4,relief=SUNKEN,bg="teal")
ti.grid(row=0,column=3 ,pady=15)

Name=Label(text="Name :" ,bg="#2E8B57" ,font="Calibri 18 bold ")
Name.grid(row=1,column=2)

Email=Label(text="Email ID :", bg="#2E8B57" ,font="Calibri 18 bold ")
Email.grid(row=2,column=2)

sor=Label(text="Source :",bg="#2E8B57" ,font="Calibri 18 bold ")
sor.grid(row=3,column=2)

dis=Label(text="Travel Destination :",bg="#2E8B57" ,font="Calibri 18 bold ")
dis.grid(row=4,column=2)

num=Label(text="Contect Number :",bg="#2E8B57" ,font="Calibri 18 bold ")
num.grid(row=5,column=2)

Name_value=StringVar()
Email_value=StringVar()
sor_value=StringVar()
dis_value=StringVar()
num_value=StringVar()



Name_entry=Entry(root,textvariable=Name_value)
Email_entry=Entry(root,textvariable=Email_value)
sor_entry=Entry(root,textvariable=sor_value)
dis_entry=Entry(root,textvariable=dis_value)
num_entry=Entry(root,textvariable=num_value)

Name_entry.grid(row=1,column=3)
Email_entry.grid(row=2,column=3)
sor_entry.grid(row=3,column=3)
dis_entry.grid(row=4,column=3)
num_entry.grid(row=5,column=3)

Label(text="Cast :" ,bg="#2E8B57", font="Calibri 18 bold").grid(row=7,column=2)
combo = ttk.Combobox(root, values=["OBC", "SC", "ST", "General"])
combo.current(0)  
combo.grid(row=7,column=3)

Label(text="Travel Purpose:" ,bg="#2E8B57", font="Calibri 18 bold").grid(row=8,column=2)
combo2 = ttk.Combobox(root, values=["Tourism", "Business", "Honeymoon", "etc."])
combo2.current(0)  
combo2.grid(row=8,column=3)

def pay():
    upi_id = "9198241778@ybl"
    name = "Akash kumar"
    amount = "29" 
    currency = "INR"
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
    qr = qrcode.make(upi_link)
    qr.show()

# Function to insert form data into MySQL
def akash_office():
    name = Name_value.get()
    email = Email_value.get()
    source = sor_value.get()
    destination = dis_value.get()
    contact = num_value.get()
    category = combo.get()
    Travel_Purpose = combo2.get() 
    if (name =="" or email =="" or source =="" or destination =="" or contact ==""):
        messagebox.showinfo("error", "Data not inserted..!")
        return

    query = """
    INSERT INTO submissions (name, email, source, destination, contact, category,Travel_Purpose)
    VALUES (%s, %s, %s, %s, %s, %s,%s)
    """
    values = (name, email, source, destination, contact, category,Travel_Purpose)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)
    messagebox.showinfo("Success", "Data inserted successfully!")
 

Button(text="submit", command=akash_office).grid(row=9,column=3,pady=23)
Button(text="Pay Now ", bg="Coral", command=pay ,font="aria 18 bold").grid(row=10,column=3,pady=5)


root.mainloop()

# Close MySQL connection when done (optional)
cursor.close()
conn.close()
