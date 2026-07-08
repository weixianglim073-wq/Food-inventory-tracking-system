# 🥫 Food Inventory Tracker

A simple Streamlit web application that helps users manage household food inventory, monitor expiry dates, and reduce food waste.

---

## Features

- 📦 View all food items in inventory
- ➕ Add new food items
- 📷 Barcode scanner support (USB barcode scanners)
- 🔍 Search inventory by food name
- ⚠ View food expiring within 7 days
- ❌ View expired food items
- 🗑 Delete food items
- 📊 Dashboard showing:
  - Total items
  - Expiring soon
  - Expired items

---

## Technologies Used

- Python
- Streamlit
- Pandas

---

## Project Structure

```
FoodInventoryTracker/
│
├── app.py
├── requirements.txt
├── food_inventory.csv
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/FoodInventoryTracker.git
cd FoodInventoryTracker
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

---

## Barcode Support

This application supports USB barcode scanners.

USB barcode scanners function like a keyboard.

Simply:

1. Click inside the Barcode input box.
2. Scan the product barcode.
3. The barcode number will automatically appear.
4. If the barcode exists in the built-in product database, the food name will be filled in automatically.

Current supported products include:

| Barcode | Product |
|----------|---------|
|9556001123456|Gardenia Bread|
|9556041600018|Farmhouse Fresh Milk|
|9555678901234|Chicken Eggs|
|9556880900012|Coca-Cola|
|9557210001000|Milo UHT|
|8888196400017|Fresh Milk|

Unknown barcodes can still be entered manually.

---

## Dashboard

The dashboard displays:

- Total number of inventory items
- Number of items expiring within 7 days
- Number of expired items
- Complete inventory table sorted by expiry date

---

## Purpose

This project was developed as a simple student project to demonstrate how technology can help households reduce food waste and improve food inventory management.

The system allows users to monitor food expiry dates and encourages better food consumption planning.

---

## Future Improvements

Possible future enhancements include:

- Barcode lookup using an online database
- QR code support
- Camera barcode scanning using a mobile phone
- Edit existing inventory items
- Email expiry reminders
- Food category filtering
- Export inventory to Excel
- User login system
- Cloud database support
- Mobile-friendly interface

---

## Author

Developed as a student Streamlit project for learning Python, data management, and food inventory tracking.
