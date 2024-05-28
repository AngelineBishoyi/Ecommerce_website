import streamlit as st
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce"
)

def main():
    st.title("Ecommerce Website")
    menu=["Home","Products","Add Cart","Search"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Welcome to Our Ecommerce Website!")
        st.image()
    elif choice == "Products":
        st.subheader("Product Details")
        product_id = st.text_input("Enter Product ID:")
        if st.button("Display Product"):
            product = fetch_product_by_id(product_id)
            if product:
                st.image(product[4], caption=product[1], use_column_width=True)
                st.write(f"Price: ${product[2]}")
                st.write(f"Description: {product[3]}")
            else:
                st.write("Product not found.")
    elif choice=="Products":
        st.subheader("Products")
    elif choice=="Search":
        st.subheader("search Products")
    elif choice=="Add Cart":
        st.subheader("AddCart wishlist")
def fetch_product_by_id(product_id):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, description, image_url FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    return product

   




if __name__ == "__main__":
        main()