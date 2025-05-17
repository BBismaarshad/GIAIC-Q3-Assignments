import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import io
from auth import auth_section  # Login system

# --- Phone Price Data Class ---
class PhonePriceChecker:
    def __init__(self):
        self.phone_data = {
            "iPhone 14": {
                "price": 2000000,
                "buy_link": "https://www.apple.com/iphone-14/",
                "image_url": "https://images.priceoye.pk/apple-iphone-14-pakistan-priceoye-4q8o2-500x500.webp",
                "popularity": 9.5,
                "units_sold": 5000000,
                "rating": 4.8,
                "price_trend": [1199, 1149, 1099, 1049],
                "storage_options": ["128GB", "256GB", "512GB"],
                "colors": ["Midnight", "Starlight", "Blue", "Purple", "Red"],
                "release_year": 2022
            },
            "Samsung Galaxy S23": {
                "price": 20999,
                "buy_link": "https://www.samsung.com/global/galaxy/galaxy-s23/",
                "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq8BpSIbfzW4N9qI_-VjIyJ1qIPEtY7SEdeA&s",
                "popularity": 9.2,
                "units_sold": 4300000,
                "rating": 4.6,
                "price_trend": [1099, 1049, 999, 949],
                "storage_options": ["128GB", "256GB"],
                "colors": ["Phantom Black", "Green", "Lavender", "Cream"],
                "release_year": 2023
            },
            "Google Pixel 7": {
                "price": 70999,
                "buy_link": "https://store.google.com/product/pixel_7",
                "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZp1feJTMQbhA5XhnCoQantR3vmc0AywlZPw&s",
                "popularity": 8.7,
                "units_sold": 3100000,
                "rating": 4.5,
                "price_trend": [899, 849, 799, 749],
                "storage_options": ["128GB", "256GB"],
                "colors": ["Snow", "Obsidian", "Lemongrass"],
                "release_year": 2022
            },
            "OnePlus 11": {
                "price": 21999,
                "buy_link": "https://www.oneplus.com/oneplus-11",
                "image_url": "https://media.wisemarket.com.pk/web-app/detail/product/oneplus-11-79.webp",
                "popularity": 5.6,
                "units_sold": 2800000,
                "rating": 4.4,
                "price_trend": [849, 799, 749, 699],
                "storage_options": ["128GB", "256GB"],
                "colors": ["Titan Black", "Eternal Green"],
                "release_year": 2023
            },
            "Xiaomi 13 Pro": {
                "price": 60999,
                "buy_link": "https://www.mi.com/global/product/xiaomi-13-pro/",
                "image_url": "https://images.priceoye.pk/xiaomi-13-pro-pakistan-priceoye-n2dfh-500x500.webp",
                "popularity": 8.3,
                "units_sold": 2500000,
                "rating": 4.3,
                "price_trend": [799, 749, 699, 649],
                "storage_options": ["128GB", "256GB", "512GB"],
                "colors": ["Ceramic Black", "Ceramic White", "Sky Blue"],
                "release_year": 2022
            },
            "Realme C75x": {
                "price": 41999,
                "buy_link": "https://www.mi.com/global/product/xiaomi-13-pro/",
                "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8GiGSx8vWPcu0PCZTd7WYMwRqBMrAzmhy56I0P5yc4ErJJrHQnUeKFuoYDVfHfcrAWHg&usqp=CAU",
                "popularity": 4.3,
                "units_sold": 2500000,
                "rating": 3.3,
                "price_trend": [799, 749, 699, 649],
                "storage_options": ["64GB", "128GB"],
                "colors": ["Black", "Blue"],
                "release_year": 2021
            }
        }

    def get_all_models(self):
        return list(self.phone_data.keys())

    def get_details(self, model_name):
        return self.phone_data.get(model_name, {})

# --- PDF Generation ---
def generate_pdf_report(phone_data, comparison_data=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Phone Price Report", ln=1, align='C')
    pdf.ln(10)
    
    # Phone Details
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=f"Phone: {phone_data['model']}", ln=1)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Price: Rs.{phone_data['price']}", ln=1)
    pdf.cell(200, 10, txt=f"Rating: {phone_data['rating']}/5", ln=1)
    pdf.cell(200, 10, txt=f"Popularity: {phone_data['popularity']}/10", ln=1)
    pdf.cell(200, 10, txt=f"Units Sold: {phone_data['units_sold']:,}", ln=1)
    pdf.ln(5)
    
    if comparison_data:
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="Comparison Summary", ln=1)
        pdf.set_font("Arial", size=12)
        
        # Comparison table
        pdf.cell(95, 10, txt=phone_data['model'], border=1)
        pdf.cell(95, 10, txt=comparison_data['model'], border=1, ln=1)
        
        pdf.cell(95, 10, txt=f"Rs.{phone_data['price']}", border=1)
        pdf.cell(95, 10, txt=f"Rs.{comparison_data['price']}", border=1, ln=1)
        
        pdf.cell(95, 10, txt=f"{phone_data['rating']}/5", border=1)
        pdf.cell(95, 10, txt=f"{comparison_data['rating']}/5", border=1, ln=1)
        
        pdf.cell(95, 10, txt=f"{phone_data['popularity']}/10", border=1)
        pdf.cell(95, 10, txt=f"{comparison_data['popularity']}/10", border=1, ln=1)
        
        pdf.cell(95, 10, txt=f"{phone_data['units_sold']:,}", border=1)
        pdf.cell(95, 10, txt=f"{comparison_data['units_sold']:,}", border=1, ln=1)
    
    return pdf.output(dest='S').encode('latin1')

# --- Main App ---
def main():
    st.set_page_config(
        page_title="Phone Price Checker", 
        page_icon="📱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
        .main {background-color: #f9f9f9;}
        .stSelectbox, .stTextInput, .stNumberInput
        .stButton>button { color: white;}
        .stAlert {border-left: 5px solid #4CAF50;}
        .footer {position: fixed; bottom: 0; width: 100%;}
        .phone-card {border-radius: 10px; padding: 15px; background-color: white; 
                    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1); margin-bottom: 20px;}
    </style>
    """, unsafe_allow_html=True)
    
    auth_section()

    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50; font-size: 48px; font-weight: bold;'>BuyNCompare</h1>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <p style='font-size: 16px; color: #555;'>Compare prices, features, and market trends for popular smartphones</p>
    </div>
    """, unsafe_allow_html=True)

    if "auth_user" not in st.session_state:
        st.warning("Please log in to access the app.")
        return

    st.success(f"Welcome back, {st.session_state['auth_user']}! 👋")

    checker = PhonePriceChecker()
    models = checker.get_all_models()
    
    # Main columns layout
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### 🔍 Search Phones")
        selected_model = st.selectbox("Select a phone model:", models, key="main_select")
        
        # Quick filters
        st.markdown("### 🎯 Quick Filters")
        min_price, max_price = st.slider(
            "Price Range (Rs.)",
            0, 3000000,
            (0, 3000000),
            step=10000
        )
        
        min_rating = st.slider("Minimum Rating", 1.0, 5.0, 3.0, 0.1)
        
        filtered_models = [
            model for model in models 
            if (min_price <= checker.get_details(model)["price"] <= max_price) and 
            (checker.get_details(model)["rating"] >= min_rating)
        ]
        
        if filtered_models != models:
            selected_model = st.selectbox("Filtered models:", filtered_models, key="filtered_select")
    
    with col2:
        if selected_model:
            data = checker.get_details(selected_model)
            
            # Phone details card
            with st.container():
                st.markdown(f"<div class='phone-card'>", unsafe_allow_html=True)
                
                col_img, col_info = st.columns([1, 2])
                with col_img:
                    st.image(data["image_url"], width=200, use_container_width=False)
                
                with col_info:
                    st.markdown(f"### {selected_model}")
                    st.markdown(f"**💰 Price:** Rs.{data['price']:,}")
                    st.markdown(f"**⭐ Rating:** {data['rating']}/5 ({'★' * int(data['rating'])}{'☆' * (5 - int(data['rating']))})")
                    st.markdown(f"**📅 Release Year:** {data.get('release_year', 'N/A')}")
                    
                    # Storage and colors
                    st.markdown(f"**💾 Storage Options:** {', '.join(data['storage_options'])}")
                    st.markdown(f"**🎨 Colors:** {', '.join(data['colors'])}")
                    
                    # Buy Now button
                    if st.button("🛒 Buy Now", key=f"buy_{selected_model}"):
                        st.session_state['show_payment'] = True
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Payment form (shown only when Buy Now is clicked)
                if st.session_state.get('show_payment', False):
                    with st.form("payment_form"):
                        st.markdown("### 💳 Payment Details")
                        cols = st.columns(2)
                        with cols[0]:
                            name = st.text_input("Full Name")
                            email = st.text_input("Email Address")
                        with cols[1]:
                            card_number = st.text_input("Card Number", placeholder="1234 5678 9012 3456")
                            cvv = st.text_input("CVV", type="password")
                        
                        cols = st.columns(2)
                        with cols[0]:
                            expiry = st.text_input("Expiry Date (MM/YY)", placeholder="MM/YY")
                        with cols[1]:
                            address = st.text_area("Shipping Address")
                        
                        submitted = st.form_submit_button("Confirm Payment")
                        
                        if submitted:
                            if all([name, email, card_number, cvv, expiry, address]):
                                st.success("✅ Payment Successful!")
                                st.balloons()
                                st.info(f"📦 Order Confirmed for **{selected_model}**")
                                st.markdown(f"**Thank you, {name}!** Your order will be shipped to:")
                                st.markdown(f"`{address}`")
                                st.markdown(f"🔗 [Track your order here]({data['buy_link']})")
                                st.session_state['show_payment'] = False
                            else:
                                st.error("Please fill in all payment details.")
                
                # Market analysis section
                st.markdown("### 📊 Market Analysis")
                
                cols = st.columns(3)
                with cols[0]:
                    st.metric("🔥 Popularity Score", f"{data['popularity']}/10")
                with cols[1]:
                    st.metric("📦 Units Sold", f"{data['units_sold']:,}")
                with cols[2]:
                    st.metric("🏆 Market Position", f"#{models.index(selected_model)+1} of {len(models)}")
                
                # Price trend chart
                st.markdown("#### 📈 Price Trend Over Time")
                trend_df = pd.DataFrame({
                    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
                    "Price (Rs.)": data["price_trend"],
                    "Model": [selected_model] * 4
                })
                
                fig = px.line(
                    trend_df, 
                    x="Quarter", 
                    y="Price (Rs.)", 
                    color="Model",
                    title=f"Price Trend for {selected_model}",
                    markers=True
                )
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis_title="Quarter",
                    yaxis_title="Price (Rs.)"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Download report button
                if st.button("📄 Download Report (PDF)"):
                    pdf_data = generate_pdf_report({
                        "model": selected_model,
                        "price": data["price"],
                        "rating": data["rating"],
                        "popularity": data["popularity"],
                        "units_sold": data["units_sold"]
                    })
                    
                    st.download_button(
                        label="⬇️ Download PDF Report",
                        data=pdf_data,
                        file_name=f"{selected_model}_report.pdf",
                        mime="application/pdf"
                    )
    
    # Comparison section
    st.markdown("---")
    st.markdown("## 🔄 Compare Phones")
    
    cols = st.columns(2)
    with cols[0]:
        model1 = st.selectbox("Select Phone 1", models, key="comp1")
    with cols[1]:
        model2 = st.selectbox("Select Phone 2", models, key="comp2")
    
    if model1 and model2 and model1 != model2:
        data1 = checker.get_details(model1)
        data2 = checker.get_details(model2)
        
        # Comparison metrics
        st.markdown("### 📋 Comparison Summary")
        
        # Create comparison table
        comparison_df = pd.DataFrame({
            "Feature": ["Price", "Rating", "Popularity", "Units Sold", "Release Year"],
            model1: [
                f"Rs.{data1['price']:,}",
                f"{data1['rating']}/5",
                f"{data1['popularity']}/10",
                f"{data1['units_sold']:,}",
                data1.get('release_year', 'N/A')
            ],
            model2: [
                f"Rs.{data2['price']:,}",
                f"{data2['rating']}/5",
                f"{data2['popularity']}/10",
                f"{data2['units_sold']:,}",
                data2.get('release_year', 'N/A')
            ]
        })
        
        # Display comparison table with alternating row colors
        st.markdown("""
        <style>
            .comparison-table {width: 100%; border-collapse: collapse;}
            .comparison-table th {background-color: #4CAF50; color: white; padding: 10px; text-align: left;}
            .comparison-table td {padding: 10px; border-bottom: 1px solid #ddd;}
            .comparison-table tr:nth-child(even) {background-color: #f2f2f2;}
        </style>
        """, unsafe_allow_html=True)
        
        st.table(comparison_df.set_index("Feature"))
        
        # Visual comparison
        st.markdown("### 📊 Visual Comparison")
        
        cols = st.columns(2)
        with cols[0]:
            st.image(data1["image_url"], width=200, use_container_width=False)
        with cols[1]:
            st.image(data2["image_url"], width=200, use_container_width=False)
        
        # Price trend comparison
        st.markdown("#### 📈 Price Trend Comparison")
        trend_df = pd.DataFrame({
            "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
            "Price (Rs.)": data1["price_trend"] + data2["price_trend"],
            "Model": [model1] * 4 + [model2] * 4
        })
        
        fig = px.line(
            trend_df, 
            x="Quarter", 
            y="Price (Rs.)", 
            color="Model",
            title="Price Trend Comparison",
            markers=True,
            line_shape="linear"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis_title="Quarter",
            yaxis_title="Price (Rs.)",
            legend_title="Phone Model"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Download comparison report
        if st.button("📄 Download Comparison Report (PDF)"):
            pdf_data = generate_pdf_report(
                {
                    "model": model1,
                    "price": data1["price"],
                    "rating": data1["rating"],
                    "popularity": data1["popularity"],
                    "units_sold": data1["units_sold"]
                },
                {
                    "model": model2,
                    "price": data2["price"],
                    "rating": data2["rating"],
                    "popularity": data2["popularity"],
                    "units_sold": data2["units_sold"]
                }
            )
            
            st.download_button(
                label="⬇️ Download Comparison PDF",
                data=pdf_data,
                file_name=f"{model1}_vs_{model2}_comparison.pdf",
                mime="application/pdf"
            )
    
    elif model1 == model2:
        st.warning("Please select two different phones for comparison.")
    
if __name__ == "__main__":
    main()