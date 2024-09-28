import boto3
# Create SES client
ses_client = boto3.client('ses', region_name='us-east-1')  # Replace with your region
# Define email parameters
SENDER = "singhgaurav9698@gmail.com"
RECIPIENT = "gaurav.learning30@gmail.com"
SUBJECT = "Test Email"
BODY_TEXT = "Gaurav!! This is a test email sent from Amazon SES using boto3."
# Send email
response = ses_client.send_email(
   Source=SENDER,
   Destination={
       'ToAddresses': [RECIPIENT],
   },
   Message={
       'Subject': {
           'Data': SUBJECT,
           'Charset': 'UTF-8'
       },
       'Body': {
           'Text': {
               'Data': BODY_TEXT,
               'Charset': 'UTF-8'
           }
       }
   }
)
print(f"Email sent! Message ID: {response['MessageId']}")