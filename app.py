from pathlib import Path

import streamlit as st
from PIL import Image
#test

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV - Irfan Aldiansyah.pdf"
profile_pic = current_dir / "assets" / "profile-pic (1).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Irfan Aldiansyah"
PAGE_ICON = "⚡"
NAME = "Irfan Aldiansyah"
DESCRIPTION = """
Data Engineer at Citilink Indonesia.
"""
EMAIL = "irfanaldi49@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/irfanaldiansyah/",
    "GitHub": "https://github.com/irfanaldi/",
    "Instagram": ""
}
Certified = {
    "🏆 Data Analytics Google": "https://www.coursera.org/account/accomplishments/professional-cert/8NU5ZQMLNATR?utm_source=mobile&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=prof",
    "🏆 AWS Academy Cloud Architecting": "https://www.credly.com/badges/11f18cbd-60f2-45e8-89d0-f4e30cf2f91b/linked_in_profile",
    "🏆 Machine Learning for Data Scientist (R Programming) (ID : 1987300840-506)": "https://digitalent.kominfo.go.id/cek-sertifikat#",
    "🏆 PCAP Programming Essentials in Pyhton": "https://drive.google.com/file/d/1byGJ2jg-yrMdJ4xRbXjnPfl6e0I13Lv6/view",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3 Years expereince Created Flow ETL, Created Dashboard, Created Report, and Querying SQL 
- ✔️ Strong hands on experience and knowledge in SQL, Excel, PowerBI, Python
- ✔️ Good understanding of Cloud Azure Synapse Analytics
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (streamlit, Pandas), SQL, SSRS, SSIS
- 📊 Data Visulization: PowerBi & MS Excel
- 📚 Method Data Ingestion: Sequence Flow & Pararel Flow
- 🗄️ Databases: Postgres, SQL Server, MySql, Azure Synapse Analytics (Azure Storage Blob)
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Engineer | Citilink Indonesia**")
st.write("09/2022 - Present")
st.write(
    """
- ► Responsible to Build Dashboard
- ► Responsible to Build Data Reporting
- ► Responsible to Data Analysis
- ► Responsible to Build ETL & ELT
- ► Responsible to Maintanance Data Warehouse
- ► Responsible to Build Pipeline Data Ingestion & Integration with Azure Synapse Analytics
- ► Responsible to Providing Ad-hoc Data
- ► Responsible to Providing Solutions for Inter-Divisional Decision Making
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Governance Analyst | Sinarmas Land**")
st.write("12/2021 - 08/2022")
st.write(
    """
- ► Data Entry using SAP CRM 
- ► ETL using SAP BO Data Service and Visual Studio (SSIS)
- ► Responsible to recap data migration between department
- ► Responsible to mapping, cleansing, standardization, policy and rule data for data quality improvement 
- ► Build dashboard monitoring data report visual using Power BI
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Sinarmas Land**")
st.write("09/2021 - 12/2021")
st.write(
    """
- ► Data preparation, preprocessing, and analysis
- ► Build analytics dashboard result 
- ► Build report insight and recommendation and help to make decision business strategy.
- ► Ad hoc report analytics.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Certified & Completions")
st.write("---")
for project, link in Certified.items():
    st.write(f"[{project}]({link})")
