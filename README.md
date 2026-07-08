# 🥫 Food Inventory Tracking System

A simple Streamlit web application that helps users manage household food inventory, monitor expiry dates, and reduce food waste.

---

## Features

- 📦 View all food items in inventory
- ➕ Add new food items
- 📷 Barcode scanner support (USB barcode scanners)
- 🔍 Search inventory by food name
- ⚠ View food items expiring within 7 days
- ❌ View expired food items
- 🗑 Delete food items
- 📊 Dashboard displaying:
  - Total inventory items
  - Expiring soon
  - Expired items

---

## Technologies Used

- Python 3
- Streamlit
- Pandas

---

## Project Structure

```
Food-inventory-tracking-system/
│
├── app.py
├── requirements.txt
├── food_inventory.csv
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/weixianglim073-wq/Food-inventory-tracking-system.git
```

### Navigate into the project

```bash
cd Food-inventory-tracking-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## Barcode Scanner Support

This application supports USB barcode scanners.

Most barcode scanners work like a keyboard.

Steps:

1. Open the **Add Food** page.
2. Click inside the Barcode textbox.
3. Scan the barcode.
4. If the barcode is recognised, the food name will be filled automatically.
5. Otherwise, manually enter the food name.

### Built-in Products

| Barcode | Product |
|---------|---------|
|9556001123456|Gardenia Bread|
|9556041600018|Farmhouse Fresh Milk|
|9555678901234|Chicken Eggs|
|9556880900012|Coca-Cola|
|9557210001000|Milo UHT|
|8888196400017|Fresh Milk|

---

## Dashboard

The dashboard provides an overview of your inventory, including:

- Total number of food items
- Items expiring within the next 7 days
- Expired food items
- Complete inventory sorted by expiry date

---

## Purpose

Food waste is a growing concern in Singapore.

This project demonstrates how a simple digital inventory system can help households:

- Keep track of food quantities
- Monitor expiry dates
- Reduce unnecessary food waste
- Encourage better food management

The application was developed as a student project using Streamlit and Python.

---

## Future Improvements

Some planned enhancements include:

- Camera barcode scanning using a phone
- QR code support
- Product lookup using Open Food Facts API
- Edit inventory items
- Food category filtering
- Email expiry reminders
- Export inventory to Excel
- Cloud database
- User accounts
- Better dashboard visualisations
- Mobile responsive interface

---

## Repository

GitHub Repository:

https://github.com/weixianglim073-wq/Food-inventory-tracking-system

---

## Author

Developed by **Wei Xiang Lim**

Student project created using Python, Streamlit and Pandas.
