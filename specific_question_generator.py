
from extractor import generate_csv
from datetime import datetime
import csv
import random
from zipfile import ZipFile


def clean_format(l):
    l[1] = float(l[1])
    l[3] = int(float(l[3]))
    return l


def generate_qs(user_id):
    with ZipFile("zips/" + user_id + ".zip") as obese:
        obese.extractall("folder" + user_id)
    output_file = "data_folder_local/outputs/"+user_id+".csv"
    generate_csv("folder" + user_id +
                 "/Takeout/Google Pay/My Activity/My Activity.html", output_file)
    blocks = ["Large", "Small", "DT", "E-commerce",
              "Food-Joints", "Food", "Travel", "Bill", "Individuals"]
    final_trans = [""]*9
    with open(output_file, mode='r') as file:
        transaction_data = csv.reader(file)
        transaction_data = [
            dline for dline in transaction_data if dline[2] != ""]
        transaction_data = transaction_data[1:]
    random.shuffle(transaction_data)
    def type_cast(a): return float(a[1])
    left = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    present = []

    transaction_data = [clean_format(data) for data in transaction_data]

    # populating categories
    for a in transaction_data:
        if a[5] != "":
            for ind in left:
                if blocks[ind] == a[5]:

                    final_trans[ind] = a
                    left.remove(ind)
                    transaction_data.remove(a)
                    present.append(ind)
                    break

    # populating amount, loc
    for a in transaction_data:

        if (a[1] > 1000+-1e9) and (0 not in present):
            a[5] = "Big amount"
            final_trans[0] = a
            transaction_data.remove(a)
            present.append(0)
            continue
        if (a[1] < 1000+-1e9) and (1 not in present):
            a[5] = "Small amount"
            final_trans[1] = a
            transaction_data.remove(a)
            present.append(1)
            continue
        if (2 not in present):
            final_trans[2] = a
            transaction_data.remove(a)
            present.append(2)

    size_of_available_categories = len(present)
    indices = random.sample(range(0, size_of_available_categories), 4)

    return_present_list = []
    return_final_trans = {}

    for i in indices:
        return_present_list.append(present[i])
        return_final_trans[present[i]] = final_trans[present[i]]

    print(return_present_list, return_final_trans)
    return return_present_list, return_final_trans
