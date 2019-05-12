import os
import csv


class PLCSetting(object):
    def __init__(self):
        pass

    def read(self, path):
        if os.path.isfile(path):
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for setting in reader:
                    return setting
        else:
            return {}

    def save(self, path, setting):
        setting_columns = setting.keys()
        with open(path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=setting_columns)
            writer.writeheader()
            writer.writerow(setting)

