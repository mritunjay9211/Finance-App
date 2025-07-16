# 💵 Personal Finance Tracker App

A smart and user-friendly **personal finance dashboard** built with **Python** and **Streamlit**, tailored for Indian users. It allows you to upload your bank CSV statement, automatically categorizes your transactions, and visualizes your expenses in real-time — all from a browser.

---

## 🔧 Features

✨ Highlights of this app:

- 📁 Upload CSV bank statements
- ⚙️ Auto-categorization of expenses based on keywords
- 🧠 Custom category and keyword management
- 📝 Interactive editing of categories in the UI
- 📊 Visual summaries (pie charts, tables) of your expenses
- 💾 Persistent category data stored in `categories.json`
- 🪄 Designed for Indian-style statements (e.g., Flipkart, Zomato)

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3** | Core language |
| **Streamlit** | Front-end web UI |
| **Pandas** | Data analysis & manipulation |
| **Plotly Express** | Interactive visualizations |
| **JSON** | Category mapping and persistence |

---

## 📁 Project Structure

## 📦 Finance-App/
├── app.py # Main Streamlit app

├── categories.json # Stores user-defined category mappings

├── sample.csv # Sample bank statement

├── README.md # Project documentation

└── requirements.txt # Python dependencies (optional)



---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```
git clone https://github.com/mritunjay9211/Finance-App.git
cd Finance-App 
```

### 2️⃣ Create a virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
## 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

## 4️⃣ Run the Streamlit app
```
streamlit run app.py
```
## 🧪 Sample CSV Format
Ensure your CSV has the following format:
```
Date,Details,Amount,Currency,Debit/Credit,Status,category
04 Jan 2025,FLIPKART,1500.00,INR,Debit,SETTLED
12 Jan 2025,Salary,50000.00,INR,Credit,SETTLED
```
📌 Date format should be: DD Mon YYYY (e.g., 04 Jan 2025)

## 🗂 Managing Categories
When transactions are uploaded, the app auto-assigns categories using keyword matching.

You can add new categories and assign keywords in the app interface.

All category mappings are stored in a file called categories.json for persistence.


## 📊 Expense Visualization
After uploading your transactions:

View/Edit categorized expenses in an editable table

Summarized totals shown per category

Pie chart visualization of where your money goes



## 🤝 Contribution
Found a bug? Want to add a feature?
Fork the repo and submit a pull request! All contributions are welcome 🙌

## 🔒 License
This project is licensed under the MIT License.
Feel free to use, modify, and share.

## 👨‍💻 Author
Built with ❤️ by Mritunjay Thakur
