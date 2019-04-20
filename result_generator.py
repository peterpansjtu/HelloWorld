import openpyxl


class PLCResult(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = "PLC结果"
        self.time_column = 1
        self.value_column = 2
        self.ws.cell(1, self.time_column, "时间戳(ms)")
        self.ws.cell(1, self.value_column, "压强(Kpa)")
        self.time_row = 2
        self.value_row = 2

    def add_result(self, timestamp, value):
        self.ws.cell(self.time_row, self.time_column, timestamp)
        self.ws.cell(self.value_row, self.value_column, value)
        self.time_row += 1
        self.value_row += 1

    def get_results(self):
        print(self.ws.columns[0])
        return

    def save(self, file_):
        self.wb.save(file_)


if __name__ == '__main__':
    result = PLCResult()
    result.add_result(0.000001, 1)
    result.add_result(0.000002, 2)
    print(result.get_results())
    result.save('1.xlsx')
