def combine(after, before):
    count = -1
    output = ''
    for i in before.splitlines():
        count = count + 1
        if i == after.splitlines()[count]:
            output = output + after.splitlines()[count] + '\n'
        else:
            output = output + i + '\n'
    return output


