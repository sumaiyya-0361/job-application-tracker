
import streamlit as st
import pandas as pd
from datetime import date
from database import (
    create_table,
    add_application,
    get_applications,
    delete_application
)

st.set_page_config(
    page_title="Job Application Tracker",
    page_icon="📋",
    layout="wide"
)

create_table()

st.title("📋 Job Application Tracker")
st.caption("Your personal dashboard for managing your job search.")

applications = get_applications()

columns = [
    "ID", "Company", "Job Role", "Location",
    "Status", "Applied Date", "Job Link", "Notes"
]

df = pd.DataFrame(applications, columns=columns)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page",
    ["Dashboard", "Add Application", "Manage Applications"]
)

if page == "Dashboard":
    st.header("Your Job Search Overview")

    total = len(df)
    interviews = int((df["Status"] == "Interview").sum())
    offers = int((df["Status"] == "Offer").sum())
    applied = int((df["Status"] == "Applied").sum())

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Applications", total)
    col2.metric("Applied", applied)
    col3.metric("Interviews", interviews)
    col4.metric("Offers", offers)

    st.divider()

    if not df.empty:
        st.subheader("Application Status Breakdown")
        status_counts = (
            df["Status"]
            .value_counts()
            .reindex(
                ["Applied", "Assessment", "Interview", "Offer", "Rejected"],
                fill_value=0
            )
        )
        st.bar_chart(status_counts)

        st.subheader("Recent Applications")
        st.dataframe(
            df.sort_values("ID", ascending=False),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Job Link": st.column_config.LinkColumn("Job Link")
            }
        )
    else:
        st.info("No applications yet. Add your first one!")

elif page == "Add Application":
    st.header("➕ Add a Job Application")

    with st.form("application_form", clear_on_submit=True):
        company = st.text_input("Company Name")
        job_role = st.text_input("Job Role")
        location = st.text_input("Job Location")

        status = st.selectbox(
            "Application Status",
            ["Applied", "Assessment", "Interview", "Offer", "Rejected"]
        )

        applied_date = st.date_input("Date Applied", value=date.today())
        job_link = st.text_input("Job Posting Link (optional)")
        notes = st.text_area("Notes (optional)")

        submitted = st.form_submit_button("Save Application")

        if submitted:
            if company.strip() and job_role.strip():
                add_application(
                    company.strip(),
                    job_role.strip(),
                    location.strip(),
                    status,
                    applied_date.isoformat(),
                    job_link.strip(),
                    notes.strip()
                )
                st.success("Application saved successfully!")
                st.rerun()
            else:
                st.error("Please enter both company name and job role.")

elif page == "Manage Applications":
    st.header("🗂️ Manage Your Applications")

    if df.empty:
        st.info("No applications to manage yet.")
    else:
        selected_statuses = st.multiselect(
            "Filter by status",
            options=["Applied", "Assessment", "Interview", "Offer", "Rejected"],
            default=["Applied", "Assessment", "Interview", "Offer", "Rejected"]
        )

        filtered_df = df[df["Status"].isin(selected_statuses)]

        st.write(f"Showing {len(filtered_df)} application(s)")
        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Job Link": st.column_config.LinkColumn("Job Link")
            }
        )

        st.divider()
        st.subheader("Delete an Application")

        selected_id = st.selectbox(
            "Select an application",
            options=df["ID"].tolist(),
            format_func=lambda app_id: (
                f"ID {app_id} — "
                f"{df.loc[df['ID'] == app_id, 'Company'].iloc[0]} "
                f"({df.loc[df['ID'] == app_id, 'Job Role'].iloc[0]})"
            )
        )

        confirm_delete = st.checkbox(
            "I confirm I want to delete this application."
        )

        if st.button("Delete Selected Application", type="primary"):
            if confirm_delete:
                delete_application(int(selected_id))
                st.success("Application deleted.")
                st.rerun()
            else:
                st.warning("Please confirm before deleting.")
