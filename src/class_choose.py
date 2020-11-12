def choose_class(sheet_list) -> int:
    print("Choose one sheet")
    for i in range(len(sheet_list)):
        print(f"{i}: {sheet_list[i].title}")
    print("other: All classes")

    try:
        index = int(input(">>>"))
        if 0 <= index < len(sheet_list):
            return index
    except:
        pass

    return -1
