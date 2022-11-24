from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

#takes in path to data of user and generates the csv

raw_dict = pd.read_csv('data/categories/category.csv',
                       header=None, index_col=0).squeeze("columns").to_dict()
rev_dictionary = {k.strip().lower():v.strip()  for k, v in raw_dict.items()}
dictionary = {}
for k, v in rev_dictionary.items():
    dictionary[v] = dictionary.get(v, []) + [k]

def fuzz_m(value):
    if not isinstance(value, str):
        return ''
    _, score, tag = process.extractOne(value, dictionary, scorer=fuzz.partial_token_sort_ratio)
    return tag if score > 50 else 'Other'


def convert_to_csv(input_path, output_path):
    with open(input_path) as fp:
        soup = BeautifulSoup(fp, "lxml")
        all_transactions = soup.find_all(
            "div", class_="outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp")
        extracted_transactions = []
        for transaction in all_transactions:
            raw_str = list(map(lambda x: x.replace(
                '\n', ''), transaction.strings))
            str_list = list(filter(None, raw_str))
            formatted_list = list(
                map(lambda x: " ".join(x.strip().split()), str_list))
            if formatted_list[1].startswith('Used'):
                continue

            transaction_type = None
            transaction_amount = None
            second_party = None
            last_four_digits = None

            # print(repr(formatted_list[1]))
            # print(repr(formatted_list[2]))
            transaction_amount = float(formatted_list[1].split()[
                                       1][1:].replace(',', ''))
            transaction_timestamp = datetime.strptime(
                formatted_list[2], '%b %d, %Y, %I:%M:%S %p %Z')

            match_acc = re.search('Bank Account X+(.+?)$', formatted_list[1])
            if match_acc:
                last_four_digits = int(match_acc.group(1))

            if formatted_list[1].startswith('Received'):
                transaction_type = 0
            elif formatted_list[1].startswith('Paid'):
                transaction_type = 1
                match_party = re.search('to (.+?) using', formatted_list[1])
                if match_party:
                    second_party = match_party.group(1)
            elif formatted_list[1].startswith('Sent'):
                transaction_type = 2
            extracted_transactions.append(
                [transaction_type, transaction_amount, second_party, last_four_digits, transaction_timestamp])

        df = pd.DataFrame(extracted_transactions, columns=[
                          'transaction_type', 'transaction_amount', 'second_party', 'last_four_digits', 'transaction_timestamp'])
        df["transaction_timestamp"] = pd.to_datetime(
            df["transaction_timestamp"]).dt.tz_localize('Asia/Kolkata')
        df['transaction_category'] = df['second_party'].apply(fuzz_m)
        df.to_csv(output_path, index=False)

def generate_csv(input_path, userid):
    convert_to_csv(input_path,"data_folder_local/outputs/"+userid+".csv")
    print("done")

