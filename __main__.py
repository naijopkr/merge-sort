from merge_sort import merge_sort

if __name__ == '__main__':
    unsorted_list = [7,6,2,4,3,8,1,0,17]
    
    sorted_list = merge_sort(unsorted_list)
    print('### UNSORTED ###')
    print(unsorted_list)

    print('### SORTED ###')
    print(sorted_list)