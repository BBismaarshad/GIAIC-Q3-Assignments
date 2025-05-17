# 📱 BuyNCompare

BuyNCompare is an interactive Streamlit web application that helps users compare smartphone prices, features, and trends. It includes a login system, price filtering, market analysis, and even lets users simulate a phone purchase with a mock payment system and PDF bill generation.

---

## 🚀 Features

- 🔐 **Login System** (via `auth.py`)
- 📊 **Compare Phone Prices & Features**
- 🔍 **Price & Rating**
- 🧾 **PDF Report Generation for Phones**
- 📈 **Interactive Price Trend Graphs using Plotly**
- 💳 **Simulated Payment Checkout**
- 🎉 **Confirmation with Animation & Tracking Info**
- 📦 **Market Stats (Popularity, Units Sold, Ratings)**

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – UI framework
- **Pandas** – Data handling
- **Plotly Express** – Interactive charts
- **FPDF** – Generate PDF reports
- **Custom Auth Module** – User login system

---

## 🏗️ Project Structure

BuyNCompare/
│
├── app.py # Main Streamlit app logic
├── auth.py # User authentication logic
├── requirements.txt # Python dependencies
└── README.md # Project overview (you’re here!)



---

## 📋 Example Phones in Dataset

- iPhone 14
- Samsung Galaxy S23
- Google Pixel 7
- OnePlus 11
- Xiaomi 13 Pro
- Realme C75x

Each phone includes:
- Price
- Ratings
- Units Sold
- Popularity Score
- Buy Link & Image
- Color & Storage Options
- Price Trends Over Time

---

## 📄 PDF Report Sample

The app can generate a downloadable PDF comparing two smartphones, containing:

- Name
- Price
- Rating
- Popularity
- Units Sold
- Visual Table Comparison (if two phones are selected)

---

## 🛒 Simulated Payment Flow

Once a user selects a phone:
- They can click **"Buy Now"**
- Enter mock payment + shipping info
- Receive a visual confirmation and tracking link

---

## 🛠️ Installation

1. **Clone the repo**

```
git clone https://github.com/yourusername/.git
cd
```


Install dependencies
```
pip install -r requirements.txt
```

Run the app

```
streamlit run main.py
```

📦 Dependencies

```
streamlit
pandas
plotly
fpdf
```

Install all via:
```
pip install -r requirements.txt
```

✨ Demo
Live Streamlit sharing link:
📍( https://giaic-q3-assignments-9nt4vw9fkkzp3amstzwsvb.streamlit.app/ )

