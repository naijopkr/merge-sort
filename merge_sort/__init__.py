def merge_sort(original_list):
    if len(original_list) <= 1:
        return original_list

    half_index = len(original_list) // 2
    left = merge_sort(original_list[:half_index])
    right = merge_sort(original_list[half_index:])

    ileft = iright = 0

    merged_list = []

    while ileft < len(left) and iright < len(right):
        if left[ileft] < right[iright]:
            merged_list.append(left[ileft])
            ileft += 1
        else :
            merged_list.append(right[iright])
            iright += 1

    while ileft < len(left):
        merged_list.append(left[ileft])
        ileft += 1

    while iright < len(right):
        merged_list.append(right[iright])
        iright += 1
        

    return merged_list
        