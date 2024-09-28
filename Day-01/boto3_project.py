import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
# Initialize S3 and SES client
s3_client = boto3.client('s3')
ses_client = boto3.client('ses', region_name='us-east-1') 
# Define email details
SENDER = "gaurav.learning30@gmail.com"
RECIPIENT = "singhgaurav9698@gmail.com"
SUBJECT = "File from S3"
# Define the S3 bucket and file
S3_BUCKET_NAME = "singhgaurav30-send-email-using-ses"
S3_FILE_NAME = "447428702001_response.txt"
LOCAL_FILE_PATH = "/tmp/" + S3_FILE_NAME  # You can adjust the local path
def download_file_from_s3(bucket_name, s3_file_name, local_file_path):
   try:
       s3_client.download_file(bucket_name, s3_file_name, local_file_path)
       print(f"File {s3_file_name} downloaded from S3 bucket {bucket_name}.")
   except NoCredentialsError:
       print("Credentials not available.")
   except PartialCredentialsError:
       print("Incomplete credentials provided.")
   except Exception as e:
       print(f"Error downloading file: {str(e)}")

def create_email_with_attachment(sender, recipient, subject, body_text, attachment_path):
   # Create a multipart email
   msg = MIMEMultipart()
   msg['Subject'] = subject
   msg['From'] = sender
   msg['To'] = recipient
   # Attach the body
   body = MIMEText(body_text)
   msg.attach(body)
   # Guess the file type based on the file name
   mime_type, _ = mimetypes.guess_type(attachment_path)
   mime_type = mime_type or "application/octet-stream"
   part = MIMEBase(*mime_type.split("/"))
   # Read the attachment and encode it
   with open(attachment_path, 'rb') as attachment:
       part.set_payload(attachment.read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
   msg.attach(part)
   return msg

def send_email_with_attachment(sender, recipient, subject, attachment_path):
   try:
       # Create email content
       email_content = create_email_with_attachment(sender, recipient, subject, "Please find the attached file.", attachment_path)
       # Send the email via SES
       response = ses_client.send_raw_email(
           Source=sender,
           Destinations=[recipient],
           RawMessage={'Data': email_content.as_string()}
       )
       print(f"Email sent! Message ID: {response['MessageId']}")
   except Exception as e:
       print(f"Error sending email: {str(e)}")

# Download the file from S3
download_file_from_s3(S3_BUCKET_NAME, S3_FILE_NAME, LOCAL_FILE_PATH)
# Send the email with the downloaded file as an attachment
send_email_with_attachment(SENDER, RECIPIENT, SUBJECT, LOCAL_FILE_PATH)