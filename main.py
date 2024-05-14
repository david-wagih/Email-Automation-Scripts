def split_emails_into_batches(input_file, output_prefix, batch_size):
    """
    Splits a text file containing emails into multiple batches.

    Args:
        input_file (str): Path to the input text file containing emails.
        output_prefix (str): Prefix for the output batch file names.
        batch_size (int): Number of emails to include in each batch file.
    """

    with open(input_file, "r") as infile:
        email_count = 0
        batch_num = 1
        outfile = open(f"{output_prefix}{batch_num}.txt", "w")

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
                outfile = open(f"{output_prefix}{batch_num}.txt", "w")

        # Close the last batch file (if not already closed)
        outfile.close()

    print(f"Successfully split emails into {batch_num} batches.")


# Example usage (replace placeholders with your actual values)
input_file = "emails.txt"
output_prefix = "batch_"
batch_size = 400000

split_emails_into_batches(input_file, output_prefix, batch_size)
