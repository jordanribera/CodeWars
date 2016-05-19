def delete_nth(order, max_e):
    output = []
    for this_item in order:
        if output.count(this_item) < max_e:
            output.append(this_item)

    return output
