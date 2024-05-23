import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Sample data (replace with actual data)
data = [
    {
        "order_number": 48,
        "item_sold_from": "Remotada",
        "item_sold_sku": "FLEXTOCK-2531-305gb",
        "item_sold_name": "Remotada 3 In 1",
        "sold_date": "29/4/2024",
        "item_price": 365,
        "slash_commission": 36.5,
        "amount_to_transfer": 28.5,
        "transfer_date": "23/5/2024",
    }
]

# Create a DataFrame with clear column names
df = pd.DataFrame(data)

# Define the PDF filename
pdf_filename = "Brand_Sales_Report.pdf"

# Create a SimpleDocTemplate object
document = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Get pre-defined styles from ReportLab
styles = getSampleStyleSheet()
title_style = styles["Title"]
header_style = styles["Heading2"]
normal_style = styles["Normal"]

# Create the title with clear date range
title = Paragraph("Brand Sales Report (Second Half of April 2024)", title_style)

# Convert DataFrame to a list of lists for the table
table_data = [list(df.columns)] + df.values.tolist()

# Calculate column widths dynamically based on document width
available_width = document.width
num_columns = len(df.columns)
col_widths = [available_width / num_columns] * num_columns

# Create the table with clear column names
table = Table(table_data, colWidths=col_widths)

# Define table style with formatting improvements
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 5),  # Reduced padding
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),  # Reduced padding
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),  # Reduced padding
            ("TOPPADDING", (0, 0), (-1, -1), 5),  # Reduced padding
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),  # Reduced padding
            ("WORDWRAP", (0, 0), (-1, -1), "CJK"),
        ]
    )
)

# Build the PDF content
elements = [title, Spacer(1, 8), table]
document.build(elements)

print(f"PDF report generated: {pdf_filename}")
