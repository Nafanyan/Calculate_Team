from datetime import datetime as dt

def data_logger(expression, result):
    time = dt.now().strftime('%H:%M')
    with open('data.txt', 'a') as file:
        file.write(f'{expression} = {result} {time}\n')
