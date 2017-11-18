from functools import reduce
from collections import Counter
import matplotlib.pyplot as plt
import scic as s


def plot_from_csv(file_csv):
    try:
        csv = s.open_csv_metadata(file_csv)

        # get column name by id
        column_to_count = csv["data"]["header"][2]

        def get_labels(row):
            return row[column_to_count]
        # def get_sizes(label): return label.column_to_count
        # sizes = [[el,labels.count(el)] from el in set(labels)]
        labels_raw = list(map(get_labels, csv["data"]["rows"]))
        c_labels_raw = Counter(labels_raw)
        labels, sizes = c_labels_raw.keys(), c_labels_raw.values()
        explode = (0.3, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=40)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')

        plt.show()
        return 0
    except:
        return -1
