from fpdf import FPDF
from datetime import datetime

class FinligencePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Finligence - Certified Cash Flow Report", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, "Financial Forecast and Actual Cash Flow Summary", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()} | Finligence", 0, 0, "C")

def generate_pdf_report(forecast_df, comparison_df, filename="Finligence_CashFlow_Report.pdf"):
    pdf = FinligencePDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 10, "Forecast Summary", ln=True)
    pdf.set_font("Arial", "", 10)
    for _, row in forecast_df.iterrows():
        pdf.cell(0, 8, f"{row['Month']}: Inflow ${row['Inflow']:,.0f}, Outflow ${row['Outflow']:,.0f}, Net ${row['Net Cash Flow']:,.0f}, DSCR {row['DSCR']}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 10, "Forecast Accuracy (vs Actual)", ln=True)
    pdf.set_font("Arial", "", 10)
    for _, row in comparison_df.iterrows():
        pdf.cell(0, 8, f"{row['Month']}: Accuracy {row['Accuracy %']:.1f}% - {row['Remark']}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 10, "Certified by:", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 8, "FCPA (Australia), FCMA (UK), CGMA (Global)", ln=True)
    pdf.cell(0, 8, f"Date: {datetime.today().strftime('%Y-%m-%d')}", ln=True)

    save_path = f"/mnt/data/{filename}"
    pdf.output(save_path)
    return save_path