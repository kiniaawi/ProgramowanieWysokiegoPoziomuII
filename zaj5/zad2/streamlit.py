import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import datetime


# Połączenie z bazą danych
def get_connection():
    conn = sqlite3.connect('sales.db')
    return conn


# Utworzenie tabeli jeśli nie istnieje
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Dodanie nowego rekordu
def add_sale(product, quantity, price, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
        (product, quantity, price, date)
    )
    conn.commit()
    conn.close()


# Pobranie wszystkich danych
def get_all_sales():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df


# Pobranie unikalnych produktów
def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT product FROM sales")
    products = [row[0] for row in cursor.fetchall()]
    conn.close()
    return products


# Główna aplikacja
def main():
    st.set_page_config(page_title="System Sprzedaży", page_icon="📊", layout="wide")

    # Inicjalizacja bazy danych
    init_db()

    st.title("📊 System Analizy Sprzedaży")
    st.markdown("---")

    # Sekcja dodawania nowej sprzedaży
    st.header("Dodaj nową transakcję")

    with st.form("add_sale_form"):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            product = st.text_input("Produkt", placeholder="Nazwa produktu")
        with col2:
            quantity = st.number_input("Ilość", min_value=1, value=1)
        with col3:
            price = st.number_input("Cena", min_value=0.0, value=0.0, step=0.1)
        with col4:
            date = st.date_input("Data", value=datetime.now())

        submitted = st.form_submit_button("Dodaj transakcję")

        if submitted:
            if product and quantity and price:
                add_sale(product, quantity, price, date.strftime("%Y-%m-%d"))
                st.success("Transakcja dodana pomyślnie!")
                st.balloons()
            else:
                st.error("Wypełnij wszystkie pola!")

    st.markdown("---")

    # Pobranie danych
    sales_data = get_all_sales()

    if sales_data.empty:
        st.info("Brak danych sprzedaży. Dodaj pierwszą transakcję.")
        return

    # Filtrowanie danych
    st.header("Filtruj dane sprzedaży")

    col1, col2 = st.columns(2)

    with col1:
        show_all = st.checkbox("Pokaż wszystkie produkty", value=True)

    with col2:
        if not show_all:
            products = get_products()
            selected_product = st.selectbox("Wybierz produkt", products)
            filtered_data = sales_data[sales_data['product'] == selected_product]
        else:
            filtered_data = sales_data

    # Wyświetlenie danych
    st.header("Dane sprzedaży")
    st.dataframe(filtered_data, use_container_width=True)

    st.markdown("---")

    # Przygotowanie danych do wykresów
    sales_data['total_value'] = sales_data['quantity'] * sales_data['price']
    daily_sales = sales_data.groupby('date')['total_value'].sum().reset_index()
    product_sales = sales_data.groupby('product')['total_value'].sum().reset_index()

    # Wykresy
    st.header("Wizualizacja danych")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sprzedaż dzienna")
        if not daily_sales.empty:
            fig_daily = px.line(daily_sales, x='date', y='total_value',
                                labels={'date': 'Data', 'total_value': 'Wartość sprzedaży'},
                                title='Dzienna wartość sprzedaży')
            st.plotly_chart(fig_daily, use_container_width=True)
        else:
            st.info("Brak danych do wyświetlenia wykresu dziennego")

    with col2:
        st.subheader("Sprzedaż wg produktów")
        if not product_sales.empty:
            fig_products = px.bar(product_sales, x='product', y='total_value',
                                  labels={'product': 'Produkt', 'total_value': 'Wartość sprzedaży'},
                                  title='Sprzedaż wg produktów')
            st.plotly_chart(fig_products, use_container_width=True)
        else:
            st.info("Brak danych do wyświetlenia wykresu produktów")

    # Statystyki
    st.markdown("---")
    st.header("Statystyki sprzedaży")

    total_sales = sales_data['total_value'].sum()
    avg_sale = sales_data['total_value'].mean()
    total_quantity = sales_data['quantity'].sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Całkowita wartość sprzedaży", f"{total_sales:,.2f} zł")
    with col2:
        st.metric("Średnia wartość transakcji", f"{avg_sale:,.2f} zł")
    with col3:
        st.metric("Łączna liczba sprzedanych sztuk", f"{total_quantity}")


if __name__ == "__main__":
    main()