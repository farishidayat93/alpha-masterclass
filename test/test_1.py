import pandas as pd


# Teesting Logic for Question 1
df = pd.read_csv('static/doc/client.csv')
tree = {}

def get_sub_emails(email_input, tree, indent=0):
    print(f'{"" : >{indent}}{email_input}')
    emails = df[df.referral_email == email_input]
    if len(emails) == 0:
        
        return
    tree[email_input] = {email:{} for email in emails.email}
    for email in emails.email:
        get_sub_emails(email,tree[email_input], indent + 4)


get_sub_emails('beemo@beemo.com', tree)
print(tree)