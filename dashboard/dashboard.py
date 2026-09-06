import os
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Analysis | Zulfan Zidni",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# MINIMALIST DESIGN SYSTEM (Custom CSS)
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header styling */
    .header-container {
        padding: 1.2rem 0 1rem 0;
        border-bottom: 1px solid #E5E7EB;
        margin-bottom: 1.5rem;
    }
    .header-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0F172A;
        letter-spacing: -0.025em;
        margin: 0;
    }
    .header-subtitle {
        font-size: 0.95rem;
        color: #64748B;
        margin-top: 0.35rem;
        margin-bottom: 0;
    }

    /* Minimalist Metric Card */
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .metric-label {
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #64748B;
        margin-bottom: 0.3rem;
    }
    .metric-value {
        font-size: 1.65rem;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.2;
    }
    .metric-caption {
        font-size: 0.8rem;
        color: #94A3B8;
        margin-top: 0.25rem;
    }

    /* Section Headings */
    .section-header {
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid #F1F5F9;
    }
    .section-title {
        font-size: 1.12rem;
        font-weight: 600;
        color: #0F172A;
        margin: 0;
    }
    .section-desc {
        font-size: 0.85rem;
        color: #64748B;
        margin-top: 0.2rem;
    }

    /* Analytical Insight Box */
    .insight-box {
        background-color: #F8FAFC;
        border-left: 3px solid #1E3A8A;
        border-radius: 0 6px 6px 0;
        padding: 0.85rem 1.1rem;
        margin-top: 1rem;
        font-size: 0.88rem;
        color: #334155;
        line-height: 1.55;
    }

    /* Conclusion Card */
    .conclusion-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        height: 100%;
        box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    .conclusion-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .conclusion-body {
        font-size: 0.85rem;
        color: #475569;
        line-height: 1.55;
    }

    /* Sidebar Clean Styling */
    .sidebar-author-box {
        padding: 0.8rem 0;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 1rem;
    }
    .author-name {
        font-size: 1rem;
        font-weight: 600;
        color: #0F172A;
        margin-top: 0.5rem;
        margin-bottom: 0.1rem;
    }
    .author-meta {
        font-size: 0.8rem;
        color: #64748B;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# DATA LOADING & CACHING
# -----------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data():
    """
    Load all_data.csv efficiently. First checks local workspace paths,
    then falls back to GitHub raw URL.
    """
    possible_local_paths = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "all_data.csv"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "all_data.csv"),
        os.path.join(os.getcwd(), "data", "all_data.csv"),
    ]
    
    file_path = None
    for path in possible_local_paths:
        if os.path.isfile(path):
            file_path = path
            break
            
    if file_path:
        df = pd.read_csv(file_path)
    else:
        url = "https://raw.githubusercontent.com/Fanbop/ProyekAnalisisData/main/data/all_data.csv"
        df = pd.read_csv(url)

    df["order_approved_at"] = pd.to_datetime(df["order_approved_at"], errors="coerce")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"], errors="coerce")
    
    return df

all_df = load_data()

# Date bounds (ignoring NaT)
valid_dates = all_df["order_approved_at"].dropna()
min_date = valid_dates.min().date()
max_date = valid_dates.max().date()

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    avatar_url = "https://firebasestorage.googleapis.com/v0/b/bangkit-dashboard/o/production%2F2024-B1%2Fprofiles%2F276daebc-c17a-4d5e-8555-b76387073971.jpeg?alt=media&token=d786f3fb-6e8d-4baa-b164-3bcde0f2278d"
    try:
        st.image(avatar_url, width=72)
    except Exception:
        pass
        
    st.markdown(
        """
        <div class="sidebar-author-box">
            <div class="author-name">Zulfan Zidni Ilhama</div>
            <div class="author-meta">Proyek Analisis Data · Dicoding</div>
            <div class="author-meta" style="margin-top: 4px;">
                <a href="https://www.linkedin.com/in/zulfanzidni" target="_blank" style="color: #2563EB; text-decoration: none;">LinkedIn</a> · 
                <a href="mailto:zulfanzidni@gmail.com" style="color: #2563EB; text-decoration: none;">Email</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("##### Pengaturan Filter")
    
    preset = st.radio(
        "Pilihan Periode",
        options=["Kustom", "Seluruh Periode (2016-2018)", "Tahun 2017", "Tahun 2018"],
        index=0,
        help="Pilih rentang tanggal cepat atau kustom.",
    )
    
    if preset == "Seluruh Periode (2016-2018)":
        default_start, default_end = min_date, max_date
    elif preset == "Tahun 2017":
        default_start, default_end = pd.to_datetime("2017-01-01").date(), pd.to_datetime("2017-12-31").date()
    elif preset == "Tahun 2018":
        default_start, default_end = pd.to_datetime("2018-01-01").date(), max_date
    else:
        default_start = pd.to_datetime("2017-01-01").date()
        default_end = max_date

    date_range = st.date_input(
        "Rentang Tanggal Analisis",
        min_value=min_date,
        max_value=max_date,
        value=[default_start, default_end],
    )
    
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = default_start, default_end

    top_n = st.slider("Jumlah Kategori (Top/Bottom N)", min_value=3, max_value=10, value=5)

    st.markdown("<hr style='border: none; border-top: 1px solid #E2E8F0; margin: 1.5rem 0;'>", unsafe_allow_html=True)
    st.caption("Sumber Dataset: [Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")

# -----------------------------------------------------------------------------
# FILTER MAIN DATASET
# -----------------------------------------------------------------------------
start_ts = pd.to_datetime(start_date)
end_ts = pd.to_datetime(end_date) + pd.Timedelta(days=1) - pd.Timedelta(nanoseconds=1)

mask = (all_df["order_approved_at"] >= start_ts) & (all_df["order_approved_at"] <= end_ts)
main_df = all_df[mask]

if main_df.empty:
    st.warning("Tidak ada transaksi pada rentang tanggal yang dipilih. Menampilkan seluruh data.")
    main_df = all_df

# -----------------------------------------------------------------------------
# APP HEADER
# -----------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="header-container">
        <div class="header-title">E-Commerce Public Data Analysis</div>
        <div class="header-subtitle">
            Hasil analisis tren penjualan, performa kategori produk, dan kepuasan pelanggan pada platform E-Commerce Olist Brasil 
            &nbsp;·&nbsp; <strong>{start_date.strftime('%d %b %Y')}</strong> s/d <strong>{end_date.strftime('%d %b %Y')}</strong>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# EXECUTIVE KPI ROW
# -----------------------------------------------------------------------------
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

total_orders = main_df["order_id"].nunique()
total_revenue = main_df.groupby("order_id")["payment_value"].first().sum()
avg_rating = main_df["review_score"].mean()
total_customers = main_df["customer_unique_id"].nunique()

with col_kpi1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Total Pesanan</div>
            <div class="metric-value">{total_orders:,.0f}</div>
            <div class="metric-caption">Pesanan unik</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_kpi2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Total Pendapatan</div>
            <div class="metric-value">R$ {total_revenue:,.0f}</div>
            <div class="metric-caption">Nilai transaksi (BRL)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_kpi3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Rata-Rata Kepuasan</div>
            <div class="metric-value">{avg_rating:.2f} <span style="font-size: 1.1rem; color: #F59E0B;">★</span></div>
            <div class="metric-caption">Skala ulasan 1.0 – 5.0</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_kpi4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Jumlah Pelanggan</div>
            <div class="metric-value">{total_customers:,.0f}</div>
            <div class="metric-caption">Pelanggan unik</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# TABS FOR NARRATIVE PRESENTATION
# -----------------------------------------------------------------------------
tab_trend, tab_product, tab_rating, tab_geo, tab_conclusions = st.tabs([
    "1. Tren Penjualan",
    "2. Performa Produk",
    "3. Kepuasan Pelanggan",
    "4. Wilayah & Pembayaran",
    "5. Kesimpulan & Rekomendasi"
])

# -----------------------------------------------------------------------------
# TAB 1: TREN PENJUALAN
# -----------------------------------------------------------------------------
with tab_trend:
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">Bagaimana tren penjualan pada platform e-commerce?</div>
            <div class="section-desc">Analisis perkembangan pesanan dan pendapatan bulanan sepanjang operasional platform.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    monthly_df = (
        main_df.dropna(subset=["order_approved_at"])
        .set_index("order_approved_at")
        .resample("ME")
        .agg({"order_id": "nunique", "payment_value": "sum"})
        .reset_index()
    )
    monthly_df["year_month"] = monthly_df["order_approved_at"].dt.strftime("%Y-%m")
    monthly_df["month_label"] = monthly_df["order_approved_at"].dt.strftime("%b %Y")
    monthly_df.rename(columns={"order_id": "order_count", "payment_value": "revenue"}, inplace=True)

    trend_metric = st.radio(
        "Pilih Metrik Visualisasi:",
        options=["Jumlah Pesanan (Orders)", "Total Pendapatan (Revenue R$)"],
        horizontal=True,
        label_visibility="collapsed"
    )

    y_col = "order_count" if "Jumlah Pesanan" in trend_metric else "revenue"
    y_title = "Jumlah Pesanan" if y_col == "order_count" else "Pendapatan (R$)"

    base = alt.Chart(monthly_df).encode(
        x=alt.X("year_month:N", title="Periode (Tahun-Bulan)", axis=alt.Axis(labelAngle=-45, grid=False)),
        tooltip=[
            alt.Tooltip("month_label:N", title="Bulan"),
            alt.Tooltip("order_count:Q", title="Pesanan", format=",.0f"),
            alt.Tooltip("revenue:Q", title="Pendapatan (R$)", format=",.2f")
        ]
    )

    area = base.mark_area(
        color="#2563EB",
        opacity=0.12,
        line=False
    ).encode(
        y=alt.Y(f"{y_col}:Q", title=y_title, axis=alt.Axis(gridColor="#F1F5F9"))
    )

    line = base.mark_line(
        color="#1E3A8A",
        strokeWidth=2.2,
        point=alt.OverlayMarkDef(color="#1E3A8A", size=45, filled=True)
    ).encode(
        y=alt.Y(f"{y_col}:Q")
    )

    chart_trend = (area + line).properties(
        height=350,
        title=alt.TitleParams(
            text=f"Perkembangan {y_title} Berdasarkan Waktu Persetujuan Pesanan",
            subtitle="Menampilkan fluktuasi bulanan dengan titik puncak transaksi",
            fontSize=14,
            subtitleFontSize=12,
            subtitleColor="#64748B",
            anchor="start"
        )
    ).configure_view(
        strokeWidth=0
    )

    st.altair_chart(chart_trend, use_container_width=True)

    if not monthly_df.empty:
        peak_row = monthly_df.loc[monthly_df[y_col].idxmax()]
        low_row = monthly_df.loc[monthly_df[y_col].idxmin()]
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown(
                f"""
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:0.9rem 1.1rem;">
                    <div style="font-size:0.75rem; font-weight:600; color:#059669; text-transform:uppercase;">Puncak Tertinggi ({peak_row['month_label']})</div>
                    <div style="font-size:1.35rem; font-weight:700; color:#0F172A; margin-top:0.2rem;">
                        {peak_row[y_col]:,.0f} {'' if y_col == 'order_count' else 'R$'}
                    </div>
                    <div style="font-size:0.8rem; color:#64748B; margin-top:0.2rem;">
                        Bulan dengan aktivitas transaksi tertinggi dalam rentang waktu yang dipilih.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_t2:
            st.markdown(
                f"""
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:0.9rem 1.1rem;">
                    <div style="font-size:0.75rem; font-weight:600; color:#DC2626; text-transform:uppercase;">Titik Terendah ({low_row['month_label']})</div>
                    <div style="font-size:1.35rem; font-weight:700; color:#0F172A; margin-top:0.2rem;">
                        {low_row[y_col]:,.0f} {'' if y_col == 'order_count' else 'R$'}
                    </div>
                    <div style="font-size:0.8rem; color:#64748B; margin-top:0.2rem;">
                        Bulan dengan transaksi terendah dalam rentang waktu yang dipilih.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        """
        <div class="insight-box">
            <strong>Analisis Tren:</strong> Volume penjualan menunjukkan tren ekspansi yang sangat konsisten sepanjang tahun 2017, mencapai puncaknya pada <strong>November 2017</strong> (terdorong oleh momentum promosi <em>Black Friday</em> dan awal belanja akhir tahun). Pada tahun 2018, platform mencapai kestabilan volume di kisaran ~6.500 hingga 7.200 pesanan per bulan sebelum periode pencatatan dataset berakhir pada Agustus 2018.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# TAB 2: PERFORMA PRODUK
# -----------------------------------------------------------------------------
with tab_product:
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">Produk mana yang paling laris dan kurang diminati?</div>
            <div class="section-desc">Perbandingan kuantitas penjualan serta kontribusi kategori produk terhadap bisnis.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    category_summary = (
        main_df.groupby("product_category_name_english")
        .agg(
            quantity=("product_id", "count"),
            total_revenue=("price", "sum"),
            avg_price=("price", "mean")
        )
        .reset_index()
    )

    top_categories = category_summary.sort_values(by="quantity", ascending=False).head(top_n)
    bottom_categories = category_summary.sort_values(by="quantity", ascending=True).head(top_n)

    col_prod_left, col_prod_right = st.columns(2)

    with col_prod_left:
        chart_best = alt.Chart(top_categories).mark_bar(
            cornerRadiusTopRight=4,
            cornerRadiusBottomRight=4,
            color="#1E3A8A"
        ).encode(
            x=alt.X("quantity:Q", title="Jumlah Unit Terjual", axis=alt.Axis(gridColor="#F1F5F9")),
            y=alt.Y("product_category_name_english:N", title=None, sort="-x"),
            tooltip=[
                alt.Tooltip("product_category_name_english:N", title="Kategori"),
                alt.Tooltip("quantity:Q", title="Terjual", format=",.0f"),
                alt.Tooltip("total_revenue:Q", title="Pendapatan (R$)", format=",.2f"),
                alt.Tooltip("avg_price:Q", title="Harga Rata-Rata (R$)", format=",.2f")
            ]
        ).properties(
            title=alt.TitleParams(
                text=f"Top {top_n} Produk Paling Laris",
                subtitle="Kategori dengan kuantitas penjualan tertinggi",
                fontSize=13,
                subtitleFontSize=11,
                subtitleColor="#64748B"
            ),
            height=280
        )
        st.altair_chart(chart_best, use_container_width=True)

    with col_prod_right:
        chart_worst = alt.Chart(bottom_categories).mark_bar(
            cornerRadiusTopRight=4,
            cornerRadiusBottomRight=4,
            color="#BE123C"
        ).encode(
            x=alt.X("quantity:Q", title="Jumlah Unit Terjual", axis=alt.Axis(gridColor="#F1F5F9")),
            y=alt.Y("product_category_name_english:N", title=None, sort="x"),
            tooltip=[
                alt.Tooltip("product_category_name_english:N", title="Kategori"),
                alt.Tooltip("quantity:Q", title="Terjual", format=",.0f"),
                alt.Tooltip("total_revenue:Q", title="Pendapatan (R$)", format=",.2f"),
                alt.Tooltip("avg_price:Q", title="Harga Rata-Rata (R$)", format=",.2f")
            ]
        ).properties(
            title=alt.TitleParams(
                text=f"Top {top_n} Produk Kurang Diminati",
                subtitle="Kategori dengan kuantitas transaksi terendah",
                fontSize=13,
                subtitleFontSize=11,
                subtitleColor="#64748B"
            ),
            height=280
        )
        st.altair_chart(chart_worst, use_container_width=True)

    st.markdown(
        """
        <div class="insight-box">
            <strong>Wawasan Produk:</strong> Kategori kebutuhan rumah tangga dan gaya hidup seperti <code>bed_bath_table</code>, <code>health_beauty</code>, dan <code>sports_leisure</code> mendominasi volume penjualan. Sebaliknya, kategori khusus seperti <code>security_and_services</code> dan <code>cds_dvds_musicals</code> mencatat transaksi sangat minim. Strategi <em>bundling</em> atau promosi silang (cross-selling) dengan produk unggulan dapat diuji untuk mendongkrak visibilitas barang-barang dengan perputaran rendah.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# TAB 3: KEPUASAN PELANGGAN
# -----------------------------------------------------------------------------
with tab_rating:
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">Bagaimana tingkat kepuasan pelanggan terhadap produk yang dibelinya?</div>
            <div class="section-desc">Distribusi skor ulasan (review score) serta hubungannya dengan performa pengiriman.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    review_counts = (
        main_df["review_score"]
        .value_counts()
        .sort_index(ascending=False)
        .reset_index()
    )
    review_counts.columns = ["review_score", "count"]
    total_reviews = review_counts["count"].sum()
    review_counts["percentage"] = (review_counts["count"] / total_reviews) * 100
    review_counts["score_label"] = review_counts["review_score"].astype(int).astype(str) + " Bintang"
    
    # Direct color mapping
    def assign_review_color(score):
        if score >= 4:
            return "#1E3A8A" # High satisfaction navy
        elif score == 3:
            return "#94A3B8" # Neutral slate
        else:
            return "#BE123C" # Low satisfaction red
            
    review_counts["bar_color"] = review_counts["review_score"].apply(assign_review_color)

    col_r1, col_r2 = st.columns([3, 2])

    with col_r1:
        chart_reviews = alt.Chart(review_counts).mark_bar(
            cornerRadiusTopRight=4,
            cornerRadiusBottomRight=4
        ).encode(
            x=alt.X("count:Q", title="Jumlah Ulasan", axis=alt.Axis(gridColor="#F1F5F9")),
            y=alt.Y("score_label:N", title=None, sort=["5 Bintang", "4 Bintang", "3 Bintang", "2 Bintang", "1 Bintang"]),
            color=alt.Color("bar_color:N", scale=None),
            tooltip=[
                alt.Tooltip("score_label:N", title="Skor"),
                alt.Tooltip("count:Q", title="Jumlah Ulasan", format=",.0f"),
                alt.Tooltip("percentage:Q", title="Persentase", format=".1f")
            ]
        ).properties(
            title=alt.TitleParams(
                text="Distribusi Skor Ulasan Pelanggan",
                subtitle="Sebagian besar ulasan berada pada rating 5 bintang",
                fontSize=13,
                subtitleFontSize=11,
                subtitleColor="#64748B"
            ),
            height=260
        )
        st.altair_chart(chart_reviews, use_container_width=True)

    with col_r2:
        delivery_by_rating = (
            main_df.groupby("review_score")["delivery_time"]
            .mean()
            .reset_index()
        )
        delivery_by_rating["score_label"] = delivery_by_rating["review_score"].astype(int).astype(str) + " ★"
        
        chart_delivery = alt.Chart(delivery_by_rating).mark_bar(
            cornerRadiusTopLeft=4,
            cornerRadiusTopRight=4,
            color="#475569"
        ).encode(
            x=alt.X("score_label:N", title="Skor Ulasan", sort=["1 ★", "2 ★", "3 ★", "4 ★", "5 ★"]),
            y=alt.Y("delivery_time:Q", title="Rata-rata Waktu Pengiriman (Hari)", axis=alt.Axis(gridColor="#F1F5F9")),
            tooltip=[
                alt.Tooltip("score_label:N", title="Rating"),
                alt.Tooltip("delivery_time:Q", title="Durasi Pengiriman (Hari)", format=".1f")
            ]
        ).properties(
            title=alt.TitleParams(
                text="Pengaruh Durasi Pengiriman",
                subtitle="Rata-rata hari pengiriman per skor rating",
                fontSize=13,
                subtitleFontSize=11,
                subtitleColor="#64748B"
            ),
            height=260
        )
        st.altair_chart(chart_delivery, use_container_width=True)

    pos_pct = review_counts[review_counts["review_score"] >= 4]["percentage"].sum()
    neg_pct = review_counts[review_counts["review_score"] <= 2]["percentage"].sum()

    st.markdown(
        f"""
        <div class="insight-box">
            <strong>Analisis Kepuasan:</strong> Sebanyak <strong>{pos_pct:.1f}%</strong> pelanggan memberikan ulasan positif (skor 4 dan 5), mencerminkan tingkat kepuasan yang tinggi secara keseluruhan. Namun demikian, terdapat <strong>{neg_pct:.1f}%</strong> ulasan negatif (skor 1 dan 2). Data membuktikan bahwa ulasan bintang 1 memiliki rata-rata waktu pengiriman hampir <strong>dua kali lipat</strong> lebih lama (~15 hari vs ~7.7 hari pada bintang 5), menandakan bahwa ketepatan logistik merupakan faktor penentu kepuasan konsumen.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# TAB 4: WILAYAH & METODE PEMBAYARAN
# -----------------------------------------------------------------------------
with tab_geo:
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">Sebaran Pelanggan & Metode Pembayaran</div>
            <div class="section-desc">Distribusi transaksi berdasarkan negara bagian (state) dan instrumen pembayaran yang digunakan.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        state_df = (
            main_df.groupby("customer_state")["order_id"]
            .nunique()
            .reset_index(name="order_count")
            .sort_values(by="order_count", ascending=False)
            .head(7)
        )
        chart_state = alt.Chart(state_df).mark_bar(
            cornerRadiusTopRight=4,
            cornerRadiusBottomRight=4,
            color="#2563EB"
        ).encode(
            x=alt.X("order_count:Q", title="Jumlah Pesanan", axis=alt.Axis(gridColor="#F1F5F9")),
            y=alt.Y("customer_state:N", title="Negara Bagian (State)", sort="-x"),
            tooltip=[
                alt.Tooltip("customer_state:N", title="State"),
                alt.Tooltip("order_count:Q", title="Pesanan", format=",.0f")
            ]
        ).properties(
            title=alt.TitleParams(
                text="Top 7 Negara Bagian Berdasarkan Jumlah Pesanan",
                subtitle="Konsentrasi terbesar berada di wilayah São Paulo (SP)",
                fontSize=13,
                subtitleFontSize=11,
                subtitleColor="#64748B"
            ),
            height=260
        )
        st.altair_chart(chart_state, use_container_width=True)

    with col_g2:
        pay_df = (
            main_df.groupby("payment_type")["order_id"]
            .nunique()
            .reset_index(name="order_count")
            .sort_values(by="order_count", ascending=False)
        )
        pay_df["payment_clean"] = pay_df["payment_type"].str.replace("_", " ").str.title()

        chart_pay = alt.Chart(pay_df).mark_bar(
            cornerRadiusTopRight=4,
            cornerRadiusBottomRight=4,
            color="#475569"
        ).encode(
            x=alt.X("order_count:Q", title="Jumlah Transaksi", axis=alt.Axis(gridColor="#F1F5F9")),
            y=alt.Y("payment_clean:N", title="Metode Pembayaran", sort="-x"),
            tooltip=[
                alt.Tooltip("payment_clean:N", title="Metode"),
                alt.Tooltip("order_count:Q", title="Transaksi", format=",.0f")
            ]
        ).properties(
            title=alt.TitleParams(
                text="Distribusi Penggunaan Metode Pembayaran",
                subtitle="Kartu kredit (credit card) merupakan preferensi utama",
                fontSize=13,
                subtitleFontSize=11,
                subtitleColor="#64748B"
            ),
            height=260
        )
        st.altair_chart(chart_pay, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 5: KESIMPULAN & REKOMENDASI STRATEGIS
# -----------------------------------------------------------------------------
with tab_conclusions:
    st.markdown(
        """
        <div class="section-header">
            <div class="section-title">Kesimpulan & Rekomendasi Bisnis</div>
            <div class="section-desc">Sintesis analitis dari ketiga pertanyaan bisnis utama yang diajukan dalam proyek ini.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_c1, col_c2, col_c3 = st.columns(3)

    with col_c1:
        st.markdown(
            """
            <div class="conclusion-card">
                <div class="conclusion-title">1. Tren Penjualan E-Commerce</div>
                <div class="conclusion-body">
                    <strong>Pola Pertumbuhan:</strong> Penjualan mengalami pertumbuhan signifikan sepanjang 2017 dan mencapai puncak rekor pada bulan <strong>November</strong> seiring momentum <em>Black Friday</em> dan belanja akhir tahun.
                    <br><br>
                    <strong>Rekomendasi:</strong>
                    <ul>
                        <li>Persiapkan kapasitas infrastruktur pergudangan dan logistik 1-2 bulan menjelang Q4.</li>
                        <li>Buat kampanye promosi khusus pada bulan-bulan beraktivitas rendah (seperti September) untuk menstabilkan arus kas.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_c2:
        st.markdown(
            """
            <div class="conclusion-card">
                <div class="conclusion-title">2. Performa Kategori Produk</div>
                <div class="conclusion-body">
                    <strong>Kategori Unggulan:</strong> <code>bed_bath_table</code>, <code>health_beauty</code>, dan <code>sports_leisure</code> merupakan kontributor volume terbesar. Sebaliknya, <code>security_and_services</code> memiliki minat paling rendah.
                    <br><br>
                    <strong>Rekomendasi:</strong>
                    <ul>
                        <li>Terapkan strategi <em>product bundling</em>: gabungkan produk berputar lambat dengan kategori populer lewat diskon paket.</li>
                        <li>Fokuskan alokasi inventaris pada kategori esensial rumah tangga dan kecantikan.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_c3:
        st.markdown(
            """
            <div class="conclusion-card">
                <div class="conclusion-title">3. Kepuasan & Loyalitas Pelanggan</div>
                <div class="conclusion-body">
                    <strong>Tingkat Kepuasan:</strong> Mayoritas pelanggan sangat puas dengan <strong>56.2%</strong> memberikan rating bintang 5. Namun, <strong>13.1%</strong> ulasan bintang 1 sangat dipengaruhi oleh keterlambatan pengiriman.
                    <br><br>
                    <strong>Rekomendasi:</strong>
                    <ul>
                        <li>Optimalisasi kemitraan logistik kurir untuk menekan <em>lead time</em> pengiriman, khususnya di luar area São Paulo.</li>
                        <li>Sediakan sistem tracking pesanan proaktif agar ekspektasi tanggal penerimaan barang selalu transparan.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown("<hr style='border: none; border-top: 1px solid #E2E8F0; margin-top: 2.5rem; margin-bottom: 1.2rem;'>", unsafe_allow_html=True)
st.caption(
    "Proyek Analisis Data E-Commerce Public Dataset · Dikembangkan oleh Zulfan Zidni Ilhama · Dibuat dengan Streamlit & Altair"
)