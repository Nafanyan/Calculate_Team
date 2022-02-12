import logger as lg

def data_input():
    global in_data
    in_data = input()
    return in_data

def data_viewer(res):
    print(f'Result = {res}')
    lg.data_logger(in_data,res)