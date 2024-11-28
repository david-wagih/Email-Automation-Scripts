# Email Handling and Sales Report Automation Documentation

## Project Overview
This repository contains scripts designed to automate email handling tasks and streamline the generation of sales reports. The scripts facilitate sending emails, organizing email lists into batches, and creating structured sales reports in PDF format. The goal is to enhance efficiency in email communication and reporting processes.

## Key Features
### Email Handling:
- **send_email:**
  - Function to send emails using SMTP with SSL support.
- **send_emails_in_batches:**
  - Function to send emails in batches.
- **split_emails_into_batches:**
  - Splits a list of emails into manageable batches.
- **split_emails_into_spreadsheets:**
  - Divides emails into spreadsheets.

### Sales Reports Automation:
- Generates sales reports in PDF format using ReportLab.
- Provides a template for creating tables and styles within the reports.

## Installation Instructions
1. Clone the repository to your local machine.
2. Ensure Python is installed on your system.
3. Install required dependencies by running `pip install -r requirements.txt`.
4. Execute the scripts as needed for email handling and sales report generation.

## Usage Examples
### Sending Emails:
```python
from emails-cleaning.mail import send_email

send_email(sender_email, receiver_email, subject, body)
```

### Splitting Emails into Batches:
```python
from emails-cleaning.main import split_emails_into_batches

split_emails_into_batches(input_file, output_prefix, batch_size)
```

### Generating Sales Reports:
```python
from sales-reports-automation.main import generate_sales_report

generate_sales_report(data)
```

## Architecture Overview
The repository comprises three main scripts:
- `mail.py`: Functions for sending emails using `smtplib`.
- `main.py`: Handles the organization of emails into batches.
- `sales-reports-automation/main.py`: Manages the generation of sales reports using ReportLab for PDF creation.

## Contributing Guidelines
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Make changes and commit with descriptive messages.
4. Push changes to your forked repository.
5. Create a pull request to the main repository's `main` branch for review and integration.