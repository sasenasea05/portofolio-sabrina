import streamlit as st

# ---------------------------------------------------------
# KONFIGURASI HALAMAN
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sabrina Septiananda | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# STYLING CUSTOM CSS (CYBERPUNK / DARK TERMINAL THEME)
# ---------------------------------------------------------
custom_css = """
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&family=Inter:wght@300;400;600;700&display=swap');

    /* Color Palette Variables */
    :root {
        --bg-main: #0b2d4a;
        --bg-card: #1e6fb8;
        --accent-teal: #14bba6;
        --text-light: #e8eaf0;
        --text-muted: #94a3b8;
    }

    /* Main Container Styling */
    .stApp {
        background-color: var(--bg-main) !important;
        font-family: 'Inter', sans-serif;
        color: var(--text-light);
    }

    /* Header / Hero Section Styling */
    .hero-box {
        background: linear-gradient(135deg, rgba(30, 111, 184, 0.4) 0%, rgba(11, 45, 74, 0.8) 100%);
        border: 1px solid var(--accent-teal);
        border-radius: 12px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 0 20px rgba(20, 187, 166, 0.15);
    }

    .hero-title {
        font-family: 'Fira Code', monospace;
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .hero-subtitle {
        color: var(--accent-teal);
        font-family: 'Fira Code', monospace;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 15px;
    }

    /* Status Metric Box */
    .metric-card {
        background-color: rgba(30, 111, 184, 0.3);
        border-left: 4px solid var(--accent-teal);
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }

    .metric-label {
        font-size: 0.8rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        font-family: 'Fira Code', monospace;
        font-size: 1.2rem;
        font-weight: bold;
        color: #ffffff;
    }

    /* Certificate Card Styling */
    .cert-card {
        background-color: var(--bg-card);
        border-radius: 10px;
        padding: 20px;
        border: 1px solid rgba(20, 187, 166, 0.3);
        transition: transform 0.2s, box-shadow 0.2s;
        margin-bottom: 15px;
    }

    .cert-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(20, 187, 166, 0.3);
    }

    .cert-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: bold;
    }

    .cert-tag {
        display: inline-block;
        background-color: rgba(20, 187, 166, 0.2);
        color: var(--accent-teal);
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-family: 'Fira Code', monospace;
        margin-top: 8px;
    }

    /* Links & Buttons */
    a {
        color: var(--accent-teal) !important;
        text-decoration: none !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR / BIODATA & SOSMED
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 💻 SYSTEM METRICS")
    st.markdown("---")
    
    # Custom Profile Card
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Developer</div>
            <div class="metric-value">Sabrina Septiananda</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Status</div>
            <div class="metric-value" style="color: #14bba6;">● Active Student</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Campus</div>
            <div class="metric-value">UNSURYA</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">GPA / IPK</div>
            <div class="metric-value">3.76 / 4.00</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔗 NETWORK / CONTACT")
    
    # URL Github sasenasea05
    st.markdown("🐙 **GitHub:** [github.com/sasenasea05](https://github.com/sasenasea05)")
    st.markdown("📧 **Email:** [sabrinasnanda0509@gmail.com](mailto:sabrinasnanda0509@gmail.com)")
    st.markdown("📷 **Instagram:** [@sabrinassn_](https://instagram.com/sabrinassn_)")
    st.markdown("📍 **Location:** Jakarta Timur, Indonesia")

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------
st.markdown("""
    <div class="hero-box">
        <div class="hero-title">SABRINA SEPTIANANDA</div>
        <p style="color: #e8eaf0; font-size: 1.05rem;">
            Mahasiswi Sistem Informasi dengan fokus pada <b>Java Web Development</b>, <b>Data Automation</b>, 
            serta <b>Machine Learning Classification</b>. Berpengalaman aktif dalam organisasi kampus dan pengembangan proyek perangkat lunak.
        </p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB UTAMA
# ---------------------------------------------------------
tab_skills, tab_org, tab_cert = st.tabs([
    "⚡ KEAHLIAN TEKNIS", 
    "👥 ORGANISASI & AKTIVITAS", 
    "🏆 SERTIFIKAT & PRESTASI"
])

# ---------------------------------------------------------
# TAB 1: KEAHLIAN TEKNIS
# ---------------------------------------------------------
with tab_skills:
    st.subheader("TECHNICAL STACK & SKILLS")
    
    skills_data = [
        {"name": "Java Web Development (JSP, Servlet, Apache Tomcat)", "level": 80, "cat": "Backend"},
        {"name": "Relational Database & SQL (MySQL)", "level": 85, "cat": "Database"},
        {"name": "Web Programming (PHP, JavaScript, HTML/CSS)", "level": 75, "cat": "Web"},
        {"name": "Python Data Automation (Selenium & BeautifulSoup)", "level": 80, "cat": "Automation"},
        {"name": "Image Preprocessing & Machine Learning (Python)", "level": 85, "cat": "Data Science"}
    ]
    
    for item in skills_data:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{item['name']}**")
            st.progress(item['level'])
        with col2:
            st.markdown(f"`{item['cat']}`")
        st.write("")

# ---------------------------------------------------------
# TAB 2: PENGALAMAN ORGANISASI
# ---------------------------------------------------------
with tab_org:
    st.subheader("ORGANIZATION & ACTIVITIES")
    
    st.markdown("""
        <div class="cert-card">
            <div class="cert-title">Himpunan Mahasiswa Informatika (HIMI)</div>
            <div class="cert-tag">ROLE: HUMAS (HUBUNGAN MASYARAKAT)</div>
            <p style="margin-top: 10px; color: #e8eaf0;">
                Berperan aktif dalam menjalin komunikasi internal/eksternal organisasi serta menyukseskan berbagai program kerja utama:
            </p>
            <ul style="color: #e8eaf0;">
                <li><b>BAKSOS HIMI 2026:</b> Berkontribusi langsung dalam pelaksanaan kegiatan bakti sosial masyarakat.</li>
                <li><b>DIKLAT HIMI 2026:</b> Penggemblengan kepemimpinan, kerja tim, dan manajemen organisasi.</li>
                <li><b>HIMI Mengajar 2026:</b> Program pengabdian masyarakat dalam memberikan edukasi teknologi.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 3: SERTIFIKAT & PRESTASI
# ---------------------------------------------------------
with tab_cert:
    st.subheader("CERTIFICATES & AWARDS")
    st.caption("Pilih file gambar sertifikat atau gunakan preview tautan yang ada.")
    
    certificates = [
        {
            "title": "PKM Internal Universitas Dirgantara Marsekal Suryadarma",
            "category": "PRESTASI AKADEMIK",
            "rank": "HARAPAN 2 (LOKAL)",
            "desc": "Penghargaan karya tulis Program Kreativitas Mahasiswa tingkat internal kampus.",
            "img": "sertifikat_pkm.jpg"
        },
        {
            "title": "Sertifikat Web Seminar / Tech Workshop",
            "category": "SEMINAR & WORKSHOP",
            "rank": "PESERTA",
            "desc": "Sertifikat partisipasi dalam pelatihan dan diskusi teknologi web/data.",
            "img": "sertifikat_seminar.jpg"
        }
    ]
    
    c1, c2 = st.columns(2)
    cols = [c1, c2]
    
    for idx, cert in enumerate(certificates):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class="cert-card">
                    <div class="cert-title">{cert['title']}</div>
                    <div class="cert-tag">📌 {cert['category']} | 🏆 {cert['rank']}</div>
                    <p style="margin-top: 8px; font-size: 0.9rem;">{cert['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Fitur Upload / Tampil Gambar
            uploaded_file = st.file_uploader(f"Upload Gambar ({cert['title']})", type=['jpg', 'jpeg', 'png'], key=f"file_{idx}")
            
            if uploaded_file is not None:
                st.image(uploaded_file, use_column_width=True)
            else:
                try:
                    st.image(cert['img'], use_column_width=True)
                except:
                    st.info(f"💡 Simpan gambar `{cert['img']}` di folder project atau gunakan tombol Upload di atas.")
            st.divider()