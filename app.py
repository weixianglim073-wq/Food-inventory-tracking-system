import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Food Inventory Tracker",
    page_icon="🥫",
    layout="wide"
)

FILE_NAME = "food_inventory.csv"

PRODUCTS = {
    "9556001123456": "Gardenia Bread",
    "9556041600018": "Farmhouse Fresh Milk",
    "9555678901234": "Chicken Eggs",
    "9556880900012": "Coca-Cola",
    "9557210001000": "Milo UHT",
    "8888196400017": "Fresh Milk"
}

# Create inventory file if it doesn't exist
if not os.path.exists(FILE_NAME):
    pd.DataFrame(
        columns=["Barcode", "Food Item", "Quantity", "Expiry Date"]
    ).to_csv(FILE_NAME, index=False)


def load():
    return pd.read_csv(FILE_NAME)


def save(df):
    df.to_csv(FILE_NAME, index=False)


inv = load()

menu = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Add Food",
        "View Inventory",
        "Expiring Soon",
        "Expired Items",
        "Delete Item"
    ]
)

# ---------------- Dashboard ---------------- #

if menu == "Dashboard":

    st.title("🥫 Food Inventory Dashboard")

    if inv.empty:
        st.info("No inventory.")

    else:
        inv["Expiry Date"] = pd.to_datetime(
            inv["Expiry Date"],
            errors="coerce"
        )

        today = pd.Timestamp.today().normalize()

        c1, c2, c3 = st.columns(3)

        c1.metric("Total Items", len(inv))

        c2.metric(
            "Expiring Soon",
            len(
                inv[
                    (inv["Expiry Date"] >= today)
                    &
                    (inv["Expiry Date"] <= today + pd.Timedelta(days=7))
                ]
            )
        )

        c3.metric(
            "Expired",
            len(inv[inv["Expiry Date"] < today])
        )

        st.dataframe(
            inv.sort_values("Expiry Date"),
            use_container_width=True
        )

# ---------------- Add Food ---------------- #

elif menu == "Add Food":

    st.title("➕ Add Food")

    st.write(
        "USB barcode scanners work like keyboards. "
        "Click the box below and scan."
    )

    barcode = st.text_input("📷 Barcode")

    name = PRODUCTS.get(barcode, "")

    if barcode:

        if name:
            st.success("✅ Product recognised.")

        else:
            st.warning("Unknown barcode. Enter product name manually.")

    food = st.text_input(
        "Food Name",
        value=name
    )

    qty = st.number_input(
        "Quantity",
        min_value=1,
        max_value=1000,
        value=1
    )

    exp = st.date_input("Expiry Date")

    if st.button("Add Item"):

        if not food.strip():
            st.error("Please enter a food name.")

        else:

            new = pd.DataFrame([{
                "Barcode": barcode,
                "Food Item": food,
                "Quantity": qty,
                "Expiry Date": exp
            }])

            inv = pd.concat(
                [inv, new],
                ignore_index=True
            )

            save(inv)

            st.success("✅ Item added successfully!")

# ---------------- Inventory ---------------- #

elif menu == "View Inventory":

    st.title("📦 Inventory")

    if inv.empty:
        st.info("Inventory is empty.")

    else:

        search = st.text_input("Search by Food Name")

        show = inv.copy()

        if search:
            show = show[
                show["Food Item"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        st.dataframe(
            show,
            use_container_width=True
        )

# ---------------- Expiring Soon ---------------- #

elif menu == "Expiring Soon":

    st.title("⚠ Expiring Within 7 Days")

    if inv.empty:
        st.info("Inventory is empty.")

    else:

        inv["Expiry Date"] = pd.to_datetime(inv["Expiry Date"])

        today = pd.Timestamp.today().normalize()

        expiring = inv[
            (inv["Expiry Date"] >= today)
            &
            (inv["Expiry Date"] <= today + pd.Timedelta(days=7))
        ]

        st.dataframe(
            expiring,
            use_container_width=True
        )

# ---------------- Expired ---------------- #

elif menu == "Expired Items":

    st.title("❌ Expired Items")

    if inv.empty:
        st.info("Inventory is empty.")

    else:

        inv["Expiry Date"] = pd.to_datetime(inv["Expiry Date"])

        today = pd.Timestamp.today().normalize()

        expired = inv[
            inv["Expiry Date"] < today
        ]

        st.dataframe(
            expired,
            use_container_width=True
        )

# ---------------- Delete ---------------- #

elif menu == "Delete Item":

    st.title("🗑 Delete Item")

    if inv.empty:
        st.info("Inventory is empty.")

    else:

        choice = st.selectbox(
            "Select Food",
            inv["Food Item"]
        )

        if st.button("Delete"):

            inv = inv[
                inv["Food Item"] != choice
            ]

            save(inv)

            st.success("✅ Item deleted.")
