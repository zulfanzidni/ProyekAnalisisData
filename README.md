# E-Commerce Public Dataset Analysis

A data analysis project and interactive dashboard analyzing transaction records from the Brazilian E-Commerce public dataset by Olist (2016–2018). The project examines order volume trends, product category performance, and customer satisfaction metrics to derive actionable business insights.

Live Demo: https://ecommercezulfan.streamlit.app/

## Project Overview

The dataset contains approximately 100,000 orders placed between late 2016 and mid-2018 across Brazil. This project processes customer, order, item, payment, and review records to answer three core business questions:

1. **Sales Trend**: How did sales volume and revenue evolve over time, and what seasonality patterns exist?
2. **Product Performance**: Which product categories record the highest and lowest sales demand?
3. **Customer Satisfaction**: What is the overall rating distribution, and what operational factors correlate with customer dissatisfaction?

## Key Findings

- **Seasonality & Growth**: Monthly order volume expanded steadily throughout 2017, reaching a historical peak in **November 2017** with 7,395 orders and R$ 1.58M in revenue driven by Black Friday campaigns. Transaction volume stabilized between 6,500 and 7,200 orders per month in 2018.
- **Category Demand**: High-velocity categories are dominated by household and lifestyle goods (`bed_bath_table`, `health_beauty`, and `sports_leisure`). Specialized categories such as `security_and_services` and `cds_dvds_musicals` registered minimal demand.
- **Review Drivers**: Approximately 75.1% of reviews are positive (4 and 5 stars), with an overall average rating of 4.02 / 5.00. However, 1-star reviews correlate strongly with logistics delays, averaging ~15 days for delivery compared to ~7.7 days for 5-star ratings.
- **Demographics & Payments**: Customers in São Paulo state (SP) account for over 42% of total order volume. Credit cards represent 73.7% of all payment transactions, followed by bank slips (Boleto) at 19.5%.

## Directory Structure

```text
ProyekAnalisisData/
|-- dashboard/
|   `-- dashboard.py          # Streamlit dashboard implementation
|-- data/
|   `-- all_data.csv          # Merged and cleaned dataset
|-- Proyek_Analisis_Data_Zulfan.ipynb  # End-to-end exploratory analysis notebook
|-- requirements.txt          # Python package dependencies
|-- url.txt                   # Streamlit Cloud deployment link
`-- README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or Python 3.11
- pip package manager or Conda

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Fanbop/ProyekAnalisisData.git
   cd ProyekAnalisisData
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Dashboard

Start the Streamlit application from the project root:

```bash
streamlit run dashboard/dashboard.py
```

Alternatively, navigate to the `dashboard` directory:

```bash
cd dashboard
streamlit run dashboard.py
```

The application will open automatically in your browser at `http://localhost:8501`.

## Dependencies

The dashboard and analysis rely on the following Python packages:

- `streamlit`
- `pandas`
- `numpy`
- `altair`
- `matplotlib`
- `seaborn`

## Author

- Name: Zulfan Zidni Ilhama
- LinkedIn: https://www.linkedin.com/in/zulfanzidni
- Email: zulfanzidni@gmail.com