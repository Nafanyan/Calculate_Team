import calculate as cl
import user_interface as ui
import converting_data as cd

def button():
    sup_arr = cd.convert()
    one_value = int(sup_arr[0])
    two_value = int(sup_arr[2])
    cl.init(one_value,two_value)
    result = cl.distribution(sup_arr[1])
    ui.data_viewer(result)
