from app.models import Clients
from app.modules import db

import pandas as pd

def s1(email):
    clients = Clients.query.filter()
    statement  = str(clients.statement)
    df = pd.read_sql_query(
        sql=statement,
        con=db.engine.connect().connection
    )
    tree = {}
    def get_sub_emails(email_input, tree):
        emails = df[df.referral_email == email_input]
        if len(emails) == 0:
            return
        tree[email_input] = {email:{} for email in emails.email}
        for email in emails.email:
            get_sub_emails(email, tree[email_input])

    

    get_sub_emails(email, tree)
    return tree

def s2(email):
    # technically not an API as per question requested but it still return a json.
    # can be change to an api by making a seprate route and adding ajax to the q2 page (or just load a separate page)
    client = Clients.query.filter_by(email=email).first()
    return client

