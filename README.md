# [Take-Home Pay Calculator](https://github.com/Dev-0S/Take-Home-Pay-Calculator)

- 🧮 A Django-based **Take-Home Pay Calculator** for UK PAYE tax rates.
- 💰 Calculates **gross income, taxable income, tax paid, NI contributions, and take-home pay**.
- 🌍 View results in **annual, monthly, weekly, daily, and hourly formats**.

---

## 🚀 Features
- ✅ **UK PAYE Tax Calculation** (Basic, Higher, Additional Rates).
- ✅ **National Insurance Contributions** based on income.
- ✅ **Currency Formatted Output** (`£xx,xxx.xx`).
- ✅ **User-Friendly Django Web Interface**.

---

## 🛠️ Installation and Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Dev-0S/Take-Home-Pay-Calculator.git
cd Take-Home-Pay-Calculator
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run Database Migrations**
```bash
python manage.py migrate
```

### 5️⃣ **Start the Django Server**
```bash
python manage.py runserver
```

Now, visit **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

---

## 📌 How to Use
1. **Enter Your Annual Income**.
2. **Click "Calculate"**.
3. **View Detailed Breakdown**:
   - Gross Income (Yearly, Monthly, Weekly, Daily, Hourly).
   - Taxable Income after allowances.
   - Tax Paid and NI Contributions.
   - Final Take-Home Pay.

---

## 📖 UK PAYE Tax Calculation
| Tax Band | Annual Income Range | Tax Rate |
|----------|--------------------|----------|
| **Personal Allowance** | Up to £12,570 | 0% |
| **Basic Rate** | £12,571 - £37,700 | 20% |
| **Higher Rate** | £37,701 - £125,140 | 40% |
| **Additional Rate** | Above £125,140 | 45% |

### **National Insurance (NI) Contributions**
| Monthly Salary | NI Rate |
|---------------|--------|
| Below £1,048 | 0% |
| £1,048 - £4,189 | 8% |
| Above £4,189 | 2% |

### **SFE (Student Finance England) Repayments**
| Annual Income | SFE Rate |
|---------------|----------|
| Below £27,295 | 0% |
| Above £27,295 | 9% |

---

## 📜 License
This project is under the **MIT License**.