# Import necessary libraries
import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Define the main class for the food ordering app
class FoodOrderingApp:
    # Constructor - sets up menu and initializes session variables
    def __init__(self):
        # Menu items categorized
        self.menu = {
            "Main Course": {
                "Pizza": {"price": 600, "image": "🍕", "prep_time": 15, "popular": True},
                "Burger": {"price": 200, "image": "🍔", "prep_time": 10, "popular": False},
                "Biryani": {"price": 500, "image": "🍛", "prep_time": 20, "popular": True},
            },
            "Snacks": {
                "Chaat": {"price": 250, "image": "🥙", "prep_time": 10, "popular": False},
            },
            "Desserts": {
                "Gulab Jamun": {"price": 200, "image": "🍡", "prep_time": 5, "popular": True},
                "Rabri": {"price": 1200, "image": "🥣", "prep_time": 8, "popular": False},
            },
            "Beverages": {
                "Lassi": {"price": 100, "image": "🥛", "prep_time": 3, "popular": True},
                "Doodh Patti Chai": {"price": 300, "image": "🍵", "prep_time": 7, "popular": True},
            }
        }

        # Set up session state and order variables
        self.init_session_state()
        self.customer_name = ""
        self.table_number = ""
        self.total_items = 0
        self.total_amount = 0
        self.max_prep_time = 0

    # Initialize session state variables to keep track of the order
    def init_session_state(self):
        if 'order_items' not in st.session_state:
            st.session_state['order_items'] = {}
        if 'order_confirmed' not in st.session_state:
            st.session_state['order_confirmed'] = False

    # Show the app title and header
    def show_header(self):
        st.markdown('<div class="header">🍽️ Flaming Python Grill</div>', unsafe_allow_html=True)
        st.markdown("---")

    # Input form for customer name and table number
    def customer_details_form(self):
        with st.expander("👤 Customer Details", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                self.customer_name = st.text_input("Full Name*", placeholder="Enter your name", key="name")
            with col2:
                self.table_number = st.text_input("Table Number", placeholder="Leave blank for takeaway", key="table")
            st.caption("*Required fields")

    # Display all items under a selected category
    def display_category(self, category_name):
        for item, details in self.menu[category_name].items():
            with st.container():
                cols = st.columns([1, 3, 2, 2])
                with cols[0]:
                    st.markdown(f"<h2>{details['image']}</h2>", unsafe_allow_html=True)
                with cols[1]:
                    st.subheader(item)
                    if details['popular']:
                        st.markdown("🔥 **Popular Item!**")
                    st.caption(f"⏱️ {details['prep_time']} mins preparation")
                with cols[2]:
                    st.markdown(f"**RS. {details['price']}**")
                with cols[3]:
                    # User selects quantity for the item
                    quantity = st.number_input(
                        f"Quantity for {item}",
                        min_value=0,
                        max_value=10,
                        value=st.session_state['order_items'].get(item, 0),
                        key=f"qty_{item}"
                    )
                    # Save or remove item from session state
                    if quantity > 0:
                        st.session_state['order_items'][item] = quantity
                    elif item in st.session_state['order_items']:
                        del st.session_state['order_items'][item]

    # Show menu in tab format for each category
    def display_menu_tabs(self):
        st.subheader("📜 Menu")
        tabs = st.tabs(list(self.menu.keys()))
        for i, category in enumerate(self.menu):
            with tabs[i]:
                self.display_category(category)

    # Generate and show the order summary
    def generate_order_summary(self):
        if not st.session_state['order_items']:
            st.info("Your order is currently empty. Select items from the menu above.")
            return

        # Reset totals
        self.total_items, self.total_amount, self.max_prep_time = 0, 0, 0
        order_df = pd.DataFrame(columns=["Item", "Quantity", "Price", "Subtotal"])

        # Calculate totals and fill the dataframe
        for item, qty in st.session_state['order_items'].items():
            category = next((cat for cat in self.menu if item in self.menu[cat]), None)
            price = self.menu[category][item]["price"]
            subtotal = qty * price
            self.total_items += qty
            self.total_amount += subtotal
            self.max_prep_time = max(self.max_prep_time, self.menu[category][item]["prep_time"])
            order_df.loc[len(order_df)] = [item, qty, f"RS. {price}", f"RS. {subtotal}"]

        # Show summary
        st.dataframe(order_df, use_container_width=True, hide_index=True)
        st.markdown(f"**Total Items:** {self.total_items}")
        st.markdown(f"**Total Amount:** RS. {self.total_amount}")
        est_time = datetime.now() + timedelta(minutes=self.max_prep_time)
        st.markdown(f"**⏳ Estimated Ready By:** {est_time.strftime('%I:%M %p')}")

        # Buttons for clearing and confirming order
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Clear Order", use_container_width=True):
                st.session_state['order_items'] = {}
                st.session_state['order_confirmed'] = False
                st.rerun()
        with col2:
            if st.button("✅ Confirm Order", type="primary", use_container_width=True, disabled=not self.customer_name):
                st.session_state['order_confirmed'] = True
                st.rerun()
            elif not self.customer_name:
                st.warning("Please enter your name to confirm order")

    # Show receipt and download button after order is confirmed
    def display_receipt(self):
        if not st.session_state['order_confirmed'] or not st.session_state['order_items']:
            return

        st.markdown("---")
        st.success("🎉 Your order has been confirmed!")

        est_time = datetime.now() + timedelta(minutes=self.max_prep_time)
        receipt = f"{' FLAMING PYTHON GRILL '.center(40, '=')}\n\n"
        receipt += f"Customer: {self.customer_name or 'Not specified'}\n"
        receipt += f"Table: {self.table_number or 'Takeaway'}\n"
        receipt += f"Order Time: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}\n"
        receipt += "-"*40 + "\n"

        # Add order items to the receipt
        for item, qty in st.session_state['order_items'].items():
            category = next((cat for cat in self.menu if item in self.menu[cat]), None)
            price = self.menu[category][item]["price"]
            subtotal = qty * price
            receipt += f"{item[:15]:<15} {qty:>2} x RS. {price:>4} = RS. {subtotal:>5}\n"

        # Add totals
        receipt += "-"*40 + "\n"
        receipt += f"{'Total Items:':<20} {self.total_items:>10}\n"
        receipt += f"{'Total Amount:':<20} RS. {self.total_amount:>8}\n"
        receipt += "-"*40 + "\n"
        receipt += f"{'Estimated Ready By:':<20} {est_time.strftime('%I:%M %p'):>10}\n"
        receipt += "-"*40 + "\n"
        receipt += f"{'Thank you for your order!'.center(40)}\n"

        # Show and download receipt
        st.subheader("📄 Order Receipt")
        st.code(receipt)
        st.download_button(
            label="📥 Download Receipt",
            data=receipt,
            file_name=f"FlamingPythonGrill_Receipt_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
            mime="text/plain"
        )

        # Option to place new order
        if st.button("🆕 Place New Order"):
            st.session_state['order_items'] = {}
            st.session_state['order_confirmed'] = False
            st.rerun()

    # Main function to run all parts of the app
    def run(self):
        self.show_header()
        self.customer_details_form()
        self.display_menu_tabs()
        st.markdown("---")
        st.subheader("🛒 Your Order")
        self.generate_order_summary()
        self.display_receipt()
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.9em;">
            Thank you for dining with us at Flaming Python Grill!<br>
            📍 Code City | 📞 +92 3110000001
        </div>
        """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app = FoodOrderingApp()
    app.run()
