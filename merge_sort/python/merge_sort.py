


def merge_sort( array : [] ):
    array = helper(array, 0, len(array) - 1 )
    return array


def helper( sub_array: [], start_idx: int, end_idx: int):

    #  Leaf worker
    if start_idx == end_idx:
        return

    # internal worker
    mid = int((start_idx + end_idx)/2)
    helper(sub_array, start_idx, mid)
    helper(sub_array, mid + 1, end_idx)

    # merge two sorted halfs
    idx_i = start_idx
    idx_j = mid + 1
    aux_array = []

    while idx_i <= mid and idx_j <= end_idx:
        if sub_array[idx_i] < sub_array[idx_j]:
            aux_array.append(sub_array[idx_i])
            idx_i += 1
        else:
            aux_array.append(sub_array[idx_j])
            idx_j += 1

    # gather
    while idx_i <= mid:
        aux_array.append(sub_array[idx_i])
        idx_i += 1
    while idx_j <= end_idx:
        aux_array.append(sub_array[idx_j])
        idx_j += 1

    count = 0
    for idx in range(start_idx, end_idx + 1):
        sub_array[idx] = aux_array[count]
        count += 1
    return sub_array


if __name__ == "__main__":
    list_to_sort = [10,1,34,2,11,44,12]
    print(f'Orig List {list_to_sort}')
    sorted_list = merge_sort(list_to_sort)
    print(f'Sorted List {sorted_list}')
