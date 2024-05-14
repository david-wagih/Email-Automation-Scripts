import csv
import os


def split_emails_into_batches(input_file, output_prefix, batch_size):
    """
    Splits a text file containing emails into multiple batches, saving them in a folder named "batches_txt".

    Args:
        input_file (str): Path to the input text file containing emails.
        output_prefix (str): Prefix for the output batch file names.
        batch_size (int): Number of emails to include in each batch file.
    """

    # Create the "batches_txt" folder if it doesn't exist
    os.makedirs("batches_txt", exist_ok=True)  # Safe folder creation

    with open(input_file, "r") as infile:
        email_count = 0
        batch_num = 1
        outfile_path = f"batches_txt/{output_prefix}{batch_num}.txt"
        outfile = open(outfile_path, "w")

        for line in infile:
            email = line.strip()  # Remove leading/trailing whitespace

            # Write email to current batch file
            outfile.write(email + "\n")
            email_count += 1

            # Check if batch size reached, close current file and open new one
            if email_count == batch_size:
                outfile.close()
                email_count = 0
                batch_num += 1
                outfile_path = f"batches_txt/{output_prefix}{batch_num}.txt"
                outfile = open(outfile_path, "w")

        # Close the last batch file (if not already closed)
        outfile.close()

    print(
        f"Successfully split emails into {batch_num} batches in 'batches_txt' folder."
    )


def split_emails_into_spreadsheets(input_file, output_prefix, batch_size):
    """
    Splits a text file containing emails into multiple spreadsheets with a column named "Email", saving them in a folder named "batches_csv".

    Args:
        input_file (str): Path to the input text file containing emails.
        output_prefix (str): Prefix for the output spreadsheet file names.
        batch_size (int): Number of emails to include in each batch spreadsheet.
    """

    # Create the "batches_csv" folder if it doesn't exist
    os.makedirs("batches_csv", exist_ok=True)  # Safe folder creation

    with open(input_file, "r") as infile:
        email_count = 0
        batch_num = 1
        outfile_path = f"batches_csv/{output_prefix}{batch_num}.csv"
        outfile = open(outfile_path, "w", newline="")  # Open in CSV format

        writer = csv.writer(outfile)  # Create a CSV writer object
        writer.writerow(["Email"])  # Write the header row

        for line in infile:
            email = line.strip()  # Remove leading/trailing whitespace

            # Write email to current batch spreadsheet
            writer.writerow([email])
            email_count += 1

            # Check if batch size reached, close current file and open new one
            if email_count == batch_size:
                outfile.close()
                email_count = 0
                batch_num += 1
                outfile_path = f"batches_csv/{output_prefix}{batch_num}.csv"
                outfile = open(outfile_path, "w", newline="")
                writer = csv.writer(outfile)
                writer.writerow(["Email"])  # Write header row for new spreadsheet

        # Close the last batch spreadsheet (if not already closed)
        outfile.close()

    print(
        f"Successfully split emails into {batch_num} spreadsheets in 'batches_csv' folder."
    )


# Example usage (replace placeholders with your actual values)
input_file = "emails.txt"
output_prefix = "batch_"
batch_size = 10000

# Choose the function you want to use (comment out the other)
# split_emails_into_batches(input_file, output_prefix, batch_size)
split_emails_into_spreadsheets(input_file, output_prefix, batch_size)
