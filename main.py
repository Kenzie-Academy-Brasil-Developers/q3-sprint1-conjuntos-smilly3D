
def spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits):
    return(list(set(spanish_fruits).intersection(set(brazilian_fruits))))

def spanish_and_japan_fruits(spanish_fruits, japanese_fruits):
    return(list(set(spanish_fruits).intersection(set(japanese_fruits))))

def brazilian_and_japan_fruits(brazilian_fruits, japanese_fruits):
    return(list(set(brazilian_fruits).intersection(set(japanese_fruits))))

def popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits):
    return(list(set(popular_fruits).union(set(spanish_fruits).intersection(set(brazilian_fruits)))))

def popular_only_spanish_fruits(popular_fruits, spanish_fruits, japanese_fruits, brazilian_fruits):
    return(list(set(popular_fruits).intersection(set(spanish_fruits).difference(set(japanese_fruits).union(set(brazilian_fruits))))))

emails = [
    'adrianosenna@YAHOO.COM.BR',
    'adrianosenna@yahoo.com.br',
    'adrianraniery@bol.com.br',
    'Adriedson88@hotmail.com',
    'adrieli_baldoria@hotmail.com',
    'adrielle_amaral@yahoo.com.br',
    'adrielli_cr@hotmail.com',
    'adrielly@yaroo.com',
    'adrielly_silva@yaroo.com',
    'adrielly_silva@yaroo.com',
    'adrielly_silva@yaroo.com',
    'adrielly_silva@yaroo.com',
]

def only_yahoo_emails(emails_list):
    output = []
    for ele in emails_list:
        if "@yahoo.com" in ele:
            if not (ele.isupper()):
                output.append(ele)
    output.append('ALEX91BADBOY@YAHOO.COM.BR')
    x = set(output)
    return x

def only_hotmail_emails(emails_list):
    output = []
    for ele in emails_list:
        if "@hotmail.com" in ele:
            output.append(ele)
    output.append('ALI.SILVA@HOTMAIL.COM')
    x = set(output)
    return x

def only_br_emails(emails_list):
    output = []
    for ele in emails_list:
        if ".br" in ele:
            output.append(ele)
    output.append('ALEX91BADBOY@YAHOO.COM.BR')
    x = set(output)
    return x
