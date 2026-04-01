# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(page_title="Market Trend Analysis", layout="wide")

# st.title("📊 Market Trend Analysis Dashboard")

# # Load Data
# df = pd.read_csv("ecommerce_sales_data.csv")
# df["Order Date"] = pd.to_datetime(df["Order Date"])

# # Sidebar
# st.sidebar.header("Filters")

# region = st.sidebar.selectbox("Select Region", df["Region"].unique())
# category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# filtered_df = df[(df["Region"] == region) & (df["Category"] == category)]

# # Show Data
# st.subheader("Filtered Data")
# st.dataframe(filtered_df)

# # Sales Trend
# st.subheader("📈 Sales Trend")

# fig = px.line(filtered_df, x="Order Date", y="Sales", title="Sales Over Time")
# st.plotly_chart(fig, use_container_width=True)

# # Insights
# st.subheader("📌 Insights")

# st.write("Sales trends show variation across regions and categories.")

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # ================= PAGE CONFIG =================
# st.set_page_config(page_title="Market Trend Analysis", layout="wide")

# # ================= CUSTOM UI =================
# st.markdown("""
# <style>
# .main {
#     background-color: #0e1117;
# }
# h1, h2, h3 {
#     color: #ffffff;
# }
# .stMetric {
#     background-color: #1c1f26;
#     padding: 15px;
#     border-radius: 10px;
#     text-align: center;
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# # 📊 Market Trend Analysis Dashboard
# ### Real-time Business Insights & Visualization
# """)

# # ================= LOAD DATA =================
# df = pd.read_csv("ecommerce_sales_data.csv")

# # Convert date
# df["Order Date"] = pd.to_datetime(df["Order Date"])

# # Create Month column
# df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# # ================= SIDEBAR =================
# st.sidebar.header("🔍 Filters")

# region = st.sidebar.multiselect("Select Region", df["Region"].unique())
# category = st.sidebar.multiselect("Select Category", df["Category"].unique())

# date_range = st.sidebar.date_input("Select Date Range", [])

# filtered_df = df.copy()

# if region:
#     filtered_df = filtered_df[filtered_df["Region"].isin(region)]

# if category:
#     filtered_df = filtered_df[filtered_df["Category"].isin(category)]

# if len(date_range) == 2:
#     start, end = date_range
#     filtered_df = filtered_df[
#         (filtered_df["Order Date"] >= pd.to_datetime(start)) &
#         (filtered_df["Order Date"] <= pd.to_datetime(end))
#     ]

# # ================= METRICS =================
# st.subheader("📌 Key Metrics")

# col1, col2, col3 = st.columns(3)

# col1.metric("Total Sales", f"{filtered_df['Sales'].sum():,.0f}")
# col2.metric("Total Profit", f"{filtered_df['Profit'].sum():,.0f}")
# col3.metric("Total Orders", len(filtered_df))

# st.markdown("---")

# # ================= TABS =================
# tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 Analysis", "📌 Insights"])

# # ================= DASHBOARD =================
# with tab1:
#     st.subheader("Filtered Data")
#     st.dataframe(filtered_df)

# # ================= ANALYSIS =================
# with tab2:

#     # Monthly Trend
#     st.subheader("📅 Monthly Sales Trend")
#     monthly_sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()

#     fig1 = px.line(monthly_sales, x="Month", y="Sales", markers=True)
#     fig1.update_layout(template="plotly_dark")
#     st.plotly_chart(fig1, use_container_width=True)

#     # Sales Trend
#     st.subheader("📈 Sales Over Time")
#     fig2 = px.line(filtered_df, x="Order Date", y="Sales")
#     fig2.update_layout(template="plotly_dark")
#     st.plotly_chart(fig2, use_container_width=True)

#     # Layout (side-by-side)
#     col1, col2 = st.columns(2)

#     with col1:
#         fig3 = px.bar(filtered_df, x="Category", y="Sales", color="Category")
#         fig3.update_layout(template="plotly_dark")
#         st.plotly_chart(fig3, use_container_width=True)

#     with col2:
#         fig4 = px.pie(filtered_df, names="Region", values="Profit", hole=0.5)
#         fig4.update_layout(template="plotly_dark")
#         st.plotly_chart(fig4)

#     # Scatter
#     st.subheader("📊 Profit vs Sales")
#     fig5 = px.scatter(filtered_df, x="Sales", y="Profit", color="Category")
#     fig5.update_layout(template="plotly_dark")
#     st.plotly_chart(fig5, use_container_width=True)

#     # Top Products
#     st.subheader("🏆 Top 10 Products")
#     top_products = filtered_df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()

#     fig6 = px.bar(top_products, x="Sales", y="Product Name", orientation='h')
#     fig6.update_layout(template="plotly_dark")
#     st.plotly_chart(fig6, use_container_width=True)

# # ================= INSIGHTS =================
# with tab3:
#     st.subheader("📌 Smart Insights")

#     if not filtered_df.empty:
#         top_region = filtered_df.groupby("Region")["Sales"].sum().idxmax()
#         top_category = filtered_df.groupby("Category")["Sales"].sum().idxmax()

#         st.write(f"🔥 Highest sales come from **{top_region}** region.")
#         st.write(f"📦 **{top_category}** category generates the most revenue.")
#     else:
#         st.write("No data available for selected filters.")

# # ================= DOWNLOAD =================
# st.sidebar.download_button(
#     label="⬇ Download Filtered Data",
#     data=filtered_df.to_csv(index=False),
#     file_name="filtered_data.csv",
#     mime="text/csv"
# )

import streamlit as st
import pandas as pd
import plotly.express as px

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Market Trend Analysis", layout="wide")

# ================= TITLE =================
st.title("📊 Market Trend Analysis Dashboard")
st.markdown("### Real-time Business Insights & Performance Overview")
st.markdown("---")

# ================= LOAD DATA =================
df = pd.read_csv("ecommerce_sales_data.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
df["Days"] = (df["Order Date"] - df["Order Date"].min()).dt.days

from sklearn.linear_model import LinearRegression

X = df[["Days"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

# ================= SIDEBAR =================
st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect("Region", df["Region"].unique())
category = st.sidebar.multiselect("Category", df["Category"].unique())

date_range = st.sidebar.date_input("Date Range", [])

filtered_df = df.copy()

if region:
    filtered_df = filtered_df[filtered_df["Region"].isin(region)]

if category:
    filtered_df = filtered_df[filtered_df["Category"].isin(category)]

if len(date_range) == 2:
    start, end = date_range
    filtered_df = filtered_df[
        (filtered_df["Order Date"] >= pd.to_datetime(start)) &
        (filtered_df["Order Date"] <= pd.to_datetime(end))
    ]

# ================= METRICS =================
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"{filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"{filtered_df['Profit'].sum():,.0f}")
col3.metric("Total Orders", len(filtered_df))

st.markdown("---")

# ================= TABS =================
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 Analysis", "📌 Insights"])

# ================= DASHBOARD =================
with tab1:
    st.subheader("Filtered Data")
    st.dataframe(filtered_df, use_container_width=True)

# ================= ANALYSIS =================
with tab2:

    # Monthly Trend
    st.subheader("📅 Monthly Sales Trend")
    monthly_sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()

    fig1 = px.line(monthly_sales, x="Month", y="Sales", markers=True, template="plotly_white")
    st.plotly_chart(fig1, use_container_width=True)

    # Sales Over Time
    st.subheader("📈 Sales Over Time")
    fig2 = px.line(filtered_df, x="Order Date", y="Sales", template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)

    # Side-by-side charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Sales by Category")
        fig3 = px.bar(filtered_df, x="Category", y="Sales", color="Category", template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.subheader("🌍 Profit by Region")
        fig4 = px.pie(filtered_df, names="Region", values="Profit", hole=0.4)
        st.plotly_chart(fig4)

    # Scatter
    st.subheader("📉 Profit vs Sales")
    fig5 = px.scatter(filtered_df, x="Sales", y="Profit", color="Category", template="plotly_white")
    st.plotly_chart(fig5, use_container_width=True)

    # Top Products
    st.subheader("🏆 Top 10 Products")
    top_products = filtered_df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()

    fig6 = px.bar(top_products, x="Sales", y="Product Name", orientation='h', template="plotly_white")
    st.plotly_chart(fig6, use_container_width=True)

    # 🔮 Sales Prediction
st.subheader("🔮 Sales Prediction (Next 30 Days)")

import numpy as np

future_days = np.arange(df["Days"].max(), df["Days"].max() + 30).reshape(-1, 1)
predictions = model.predict(future_days)

future_dates = pd.date_range(start=df["Order Date"].max(), periods=30)

pred_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted Sales": predictions
})

fig_pred = px.line(pred_df, x="Date", y="Predicted Sales")
st.plotly_chart(fig_pred, use_container_width=True)

# ================= INSIGHTS =================
with tab3:
    st.subheader("📌 Smart Insights")

    if not filtered_df.empty:
        top_region = filtered_df.groupby("Region")["Sales"].sum().idxmax()
        top_category = filtered_df.groupby("Category")["Sales"].sum().idxmax()

        st.success(f"Highest sales come from **{top_region}** region.")
        st.info(f"Top performing category is **{top_category}**.")

    else:
        st.warning("No data available for selected filters.")

# ================= DOWNLOAD =================
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="⬇ Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv"
)