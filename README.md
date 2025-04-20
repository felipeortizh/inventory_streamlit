# Inventory Forecasting & EOQ Optimization Web App

Forecast future product demand with **Facebook Prophet** and compute optimal **Economic Order Quantity (EOQ)** parameters – all from an interactive [Streamlit](https://streamlit.io/) dashboard.

---

## 📚 What this project does
* **Time‑series forecasting** – fits a Prophet model on historical monthly demand (sample data provided).
* **Interactive sliders** – pick fixed order cost (*k*), annual holding cost per unit (*h*), and supplier lead‑time (*L*).
* **EOQ & Re‑order point** – instantly calculates how much and when you should order.
* **Downloadable results** – export the full forecast to CSV at the click of a button.
* **Beautiful visuals** – embedded Plotly charts and a custom Streamlit colour theme.

---

## ⚡ Quick‑start

```bash
# 1. Clone the repo
git clone https://github.com/felipeortizh/inventory_streamlit.git
cd inventory_streamlit

# 2. (Optional) create a virtualenv
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run inventario_prophet.py
```

Open the URL shown in the console (default <http://localhost:8501>) and start experimenting 🎉.

---

## 🗂️ Repository layout

```
├── inventario_prophet.py  # Streamlit application
├── milk_production.csv    # Example data set (monthly milk demand)
├── requirements.txt       # Python package list
└── .streamlit/
    └── config.toml        # Custom UI theme
```

---

## 🔬 Behind the scenes

| Component | Details |
|-----------|---------|
| **Model** | Prophet additive model with yearly & monthly seasonality |
| **Forecast horizon** | 12 months (adjustable by changing test size) |
| **EOQ inputs** | *k*, *h*, *L* provided via sidebar sliders |
| **Data** | Sample milk demand data from the USDA (Jan 1962 → Dec 1975) |
| **Caching** | Downloadable CSV is cached with `@st.cache_data` |

---

## ☁️ Deploy in 3 steps (Streamlit Community Cloud)

1. Push the repo to GitHub (already done).  
2. Create a **new app** on <https://share.streamlit.io>.  
3. Point it to `inventario_prophet.py` on the `main` branch and click **Deploy** – that’s it!

---

## 🤝 Contributing

Issues and PRs are welcome! Feel free to:

* add new forecasting models (ARIMA, LSTM…)
* upload different demand datasets
* improve UX or visual design

---

## 📜 License

Licensed under the **MIT License**.

---

## 🙋 Author

**Felipe Ortiz** – [@felipeortizh](https://github.com/felipeortizh)  
Made with ☕, 🐍 and ❤️
