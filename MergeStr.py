def MergeStr(a,b):
    if len(a) != len(b):
        return 
    elif a == '' and b == '':
        return ''
    else:
        return a[0] + b[0] + MergeStr(a[1:], b[1:])
