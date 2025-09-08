import sqlite3
import pandas as pd


def connect_to_db():
    try:
        conn = sqlite3.connect('sales.db')
        print("Połączono z bazą danych successfully!")
        return conn
    except sqlite3.Error as e:
        print(f"Błąd połączenia z bazą danych: {e}")
        return None


# Wyświetl tylko sprzedaż produktu „Laptop”
def query_laptop_sales(conn):
    query = "SELECT * FROM sales WHERE product = 'Laptop'"
    df = pd.read_sql_query(query, conn)
    return df


# Wyświetl dane tylko z dni 2025-05-07 i 2025-05-08
def query_date_range(conn):
    query = "SELECT * FROM sales WHERE date IN ('2025-05-07', '2025-05-08')"
    df = pd.read_sql_query(query, conn)
    return df


# Wyświetl tylko transakcje, w których cena jednostkowa przekracza 200 zł
def query_high_price(conn):
    query = "SELECT * FROM sales WHERE price > 200"
    df = pd.read_sql_query(query, conn)
    return df


# Oblicz łączną wartość sprzedaży dla każdego produktu
def query_total_sales(conn):
    query = """
    SELECT 
        product, 
        SUM(quantity * price) as total_sales_value
    FROM sales
    GROUP BY product
    """
    df = pd.read_sql_query(query, conn)
    return df


# Znajdź dzień z największą liczbą sprzedanych sztuk
def query_most_sold_day(conn):
    query = """
    SELECT 
        date,
        SUM(quantity) as total_quantity
    FROM sales
    GROUP BY date
    ORDER BY total_quantity DESC
    LIMIT 1
    """
    df = pd.read_sql_query(query, conn)
    return df



def main():
    conn = connect_to_db()
    if conn is None:
        return

    try:
        print("\n=== a) Sprzedaż produktu 'Laptop' ===")
        laptop_sales = query_laptop_sales(conn)
        print(laptop_sales)

        print("\n=== b) Dane z dni 2025-05-07 i 2025-05-08 ===")
        date_sales = query_date_range(conn)
        print(date_sales)

        print("\n=== c) Transakcje z ceną powyżej 200 zł ===")
        high_price_sales = query_high_price(conn)
        print(high_price_sales)

        print("\n=== d) Łączna wartość sprzedaży dla każdego produktu ===")
        total_sales = query_total_sales(conn)
        print(total_sales)

        print("\n=== e) Dzień z największą liczbą sprzedanych sztuk ===")
        most_sold_day = query_most_sold_day(conn)
        print(most_sold_day)

    except Exception as e:
        print(f"Wystąpił błąd podczas wykonywania zapytań: {e}")
    finally:
        if conn:
            conn.close()
            print("\nPołączenie z bazą danych zamknięte.")


if __name__ == "__main__":
    main()