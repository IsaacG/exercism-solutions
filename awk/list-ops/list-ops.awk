@namespace "listops"

# Append to a list all the elements of another list.
# Or append to a list a single new element
function append(list, item_or_list) {
    # print awk::typeof(item_or_list)
    if (awk::typeof(item_or_list) == "array")
        for (i in item_or_list)
            append(list, item_or_list[i])
    else
        list[length(list) + 1] = item_or_list
}

# Concatenate is flattening a list of lists one level
function concat(list, result) {
    for (i in list)
        append(result, list[i])
}

# Only the list elements that pass the given function.
function filter(list, funcname, result) {
    for (i in list)
        if (@funcname(list[i]))
            append(result, list[i])
}

# Transform the list elements, using the given function, into a new list.
function map(list, funcname, result) {
    for (i in list)
        append(result, @funcname(list[i]))
}

# Left-fold the list using the function and the initial value.
function foldl(list, funcname, initial) {
    result = initial
    for (i in list)
        result = @funcname(result, list[i])
    return result
}

# Right-fold the list using the function and the initial value.
function foldr (list, funcname, initial,   rev) {
    array::init(rev)
    reverse(list, rev)
    result = initial
    for (i in rev)
        result = @funcname(rev[i], result)
    return result
}

# the list reversed
function reverse (list, result) {
    cur = length(list)
    for (i in list)
        result[cur--] = list[i]
}
