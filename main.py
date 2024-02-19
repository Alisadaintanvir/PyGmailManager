from dotenv import load_dotenv
import os
from emailManager import EmailManager
load_dotenv()

username = os.environ.get('EMAIL')
password = os.environ.get("PASSWORD")

key = "FROM"
value = "Canva"

if __name__ == "__main__":
    email_manager = EmailManager(username, password)
    if email_manager.search(key, value):
        delete_choice = input("Do you want to delete this email? (yes/no): ").lower()
        if delete_choice == 'yes':
            email_manager.delete_email(key, value)
        else:
            print("Email not deleted.")
    email_manager.close_connection()
