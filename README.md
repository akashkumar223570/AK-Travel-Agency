ravel Agency - Tkinter Booking App

A desktop application built using **Python Tkinter** that allows users to book travel services, store booking data in **MySQL**, and generate **UPI QR codes** for payment.

---

## 📸 Screenshot
![App Screenshot](<img width="632" height="634" alt="Screenshot 2025-05-11 134800" src="https://github.com/user-attachments/assets/98587e41-327e-4bff-a4dc-af74a3820026" />
)

---

## ✨ Features
- **User-Friendly Form** for travel bookings
- **Dropdown Selection** for caste and travel purpose
- **MySQL Database Integration** to store booking details
- **UPI Payment QR Code** generation using `qrcode` library
- **Form Validation** before submission
- Clean and colorful Tkinter GUI

---

## 🛠️ Tech Stack
- **Python 3**
- **Tkinter** (GUI)
- **MySQL** (Database)
- **qrcode** (Payment QR generation)
- **Pillow** (Image handling for QR)

---

## 📦 Installation
1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/travel-agency-tkinter.git
   cd travel-agency-tkinter
Install dependencies:

bash
Copy
Edit
pip install mysql-connector-python qrcode[pil]
Set up MySQL Database:

sql
Copy
Edit
CREATE DATABASE form_data;
USE form_data;
CREATE TABLE submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    source VARCHAR(100),
    destination VARCHAR(100),
    contact VARCHAR(15),
    category VARCHAR(20),
    Travel_Purpose VARCHAR(50)
);
Run the app:

bash
Copy
Edit
python main.py
📄 How It Works
User fills in name, email, travel source & destination, contact number, caste, and travel purpose.

On Submit, data is stored in the MySQL database.

On Pay Now, a UPI QR code is generated for payment.

Shows success/error messages via Tkinter message boxes.

📬 Author
Akash Kumar
📧 Email: your-email@example.com
🌐 GitHub: yourusername
