from src import data
from src.utils import o, oo


# Print some stats on columns.
def test_stats() -> bool:
    def helper_stats_div(col):
        return col.div()

    def helper_stats_mid(col):
        return col.mid()

    csv_file_name = "auto93.csv"
    data_obj = data.Data(csv_file_name)
    div = helper_stats_div
    mid = helper_stats_mid
    print("xmid", o(data_obj.stat(2, data_obj.cols.x, mid)))
    print("xdiv", o(data_obj.stat(3, data_obj.cols.x, div)))
    print("ymid", o(data_obj.stat(2, data_obj.cols.y, mid)))
    print("ydiv", o(data_obj.stat(3, data_obj.cols.y, div)))
    return True


def test_data() -> bool:
    csv_file_name = "auto93.csv"
    data_obj = data.Data(csv_file_name)
    for i in data_obj.cols.names:
        oo(i)
    return True
