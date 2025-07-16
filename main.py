import streamlit as st 
import pandas as pd 
import plotly.express as px 
import json 
import os 

st.set_page_config(page_title="Finance App" , page_icon="💵" , layout="wide")


categories_file = "categories.json"
if "categories" not in st.session_state:
    st.session_state.categories = {
        "uncategorized" : []
    }

if os.path.exists(categories_file):
    with open(categories_file , 'r' ) as f :
        st.session_state.categories = json.load(f)

def save_categories():
    with open(categories_file , "w") as f:
        json.dump(st.session_state.categories ,f )

def categorize_transaction(df):
    df["category"] = "uncategorized"
    df["Category"] = df["Category"].astype("object")

    for category , keywords in st.session_state.categories.items():
        if category == "uncategorized" or not keywords:
            continue

        lowered_keywords = [keyword.lower().strip() for keyword in keywords]

        for idx , row in df.iterrows():
            details = row['Details'].lower().strip()
            if details in lowered_keywords:
                df.at[idx , 'Category'] = category

    return df

def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(',', "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"] , format = '%d %b %Y')


        return categorize_transaction(df)
    except Exception as e:
        st.error(f"Error processing file : {str(e)}")
        return None

def add_keywords_to_categories(category , keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False

def main():
    st.title("Personal Finance Dashboard")

    uploaded_file = st.file_uploader("upload your transaction CSV file " , type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            credits_df = df[df["Debit/Credit"] == "Credit"]
            debits_df = df[df["Debit/Credit"] == "Debit"]


            st.session_state.debits_df = debits_df.copy()

            tab1 , tab2 = st.tabs(["Expenses (debits)", "Payments (credits)" ])

            with tab1:

                new_category = st.text_input("New Category Name")
                add_button = st.button("Add Category")

                if new_category and add_button:
                    if new_category not in st.session_state.categories :
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.success(f"Added Categories : {new_category}")
                        st.rerun()

                st.subheader("Your Expenses")
                edited_df = st.data_editor(
                    st.session_state.debits_df[["Date", "Details", "Amount", "Category"]],
                    column_config={
                        "Date" : st.column_config.DateColumn("Date",format="DD/MM/YYY"),
                        "Amount" : st.column_config.NumberColumn("Amount" , format = " ₹ %.2f"),
                        "Category" : st.column_config.SelectboxColumn(
                            "Category",
                            options= list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )

                save_button  = st.button("Apply Changes", type= "primary")
                if save_button:
                    for idx , row in edited_df.iterrows():
                        new_category = row["Category"]
                        if new_category == st.session_state.debits_df.at[idx ,"category"]:
                            continue
                        details = row["Category"]
                        st.session_state.debits_df.at[idx , "Category"] = new_category
                        add_keywords_to_categories(new_category , details)

                
                st.subheader("Expense Summary")
                category_totals = st.session_state.debits_df.groupby("Category")['Amount'].sum().reset_index()
                category_totals = category_totals.sort_values("Amount" , ascending=False)

                st.dataframe(
                    category_totals,
                    column_config= {
                        "Amount" : st.column_config.NumberColumn("Amount" , format="₹ %.2f"),
                        },
                        use_container_width=True,
                        hide_index=True
                    )
                
                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expense by Category"
                )
                st.plotly_chart( fig , use_container_width=True)


            with tab2:
                st.write(credits_df)

            



main()