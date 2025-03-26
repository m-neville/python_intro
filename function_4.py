# TCO3V7DNGM Confirmed. Ksh3,000 sent to FRANCIS KINUNGI on 24/3/25 at 8:02AM.
def extract_amount(mpesa_message):
    index_Ksh = mpesa_message.index("Ksh")
    index_sent = mpesa_message.index("sent")
    amount = mpesa_message[index_Ksh: index_sent]
    # Ksh3,000
    amount = amount.replace("Ksh", "")
    amount = amount.replace(",", "")
    print(amount)


def extract_date(mpesa_message):
    index_on = mpesa_message.index(" on ")
    index_at = mpesa_message.index("at")
    date = mpesa_message[index_on: index_at]
    date = date.replace(" on ", "")
    date = date.strip() # remove whitespace
    print(date)


message_1 = "TCO3V7DNGM Confirmed. Ksh3,000 sent to FRANCIS Simon on 24/3/25 at 8:02AM."
extract_amount(message_1)
extract_date(message_1)
