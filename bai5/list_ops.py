def find_min_max(data_list):
    #tim phan tu lon nhat va nho nhat trong danh sach
    if not data_list:
        return None, None
    min_val = min(data_list)
    max_val = max(data_list)
    return min_val, max_val

def sort_list_asc(data_list):
    #sap xep danh sach theo thu tu tang dan
    return sorted(data_list)

def find_min_max_index(data_list,min_val,max_val):
    #tim vi tri cua phan tu lon nhat va nho nhat
    min_index = data_list.index(min_val) if min_val in data_list else -1
    max_index = data_list.index(max_val) if max_val in data_list else -1
    return min_index, max_index
    