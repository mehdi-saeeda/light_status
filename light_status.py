def count_light_changes(status_list):
    changes = 0
    for i in range(1, len(status_list)):
        if status_list[i] != status_list[i - 1]:
            changes += 1
    return changes
