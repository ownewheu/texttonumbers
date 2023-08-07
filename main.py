def parse_int(string):
    def hundred(list):
        if "100" in list:
            list = list[-4:]
            i = list.index("100")
            y = 0
            y = int(list[i-1])
            a = y * int(list[i])
            return a
        else:
            return 0
    def thousand(list):
        i = list.index("1000")
        y = 0
        if "100" in list[:i]:
            x = str(hundred(list[:i]))
            del list[0:2]
            list.insert(0, x)
            i = list.index("1000")
        for x in list[:i]:
            y += int(x)
        b = y * int(list[i])
        return b
    def lessthanhundred(list):
        if "1000" not in list[-2:] and "100" not in list[-2:]:
            l = list[-2:]
        elif "1000" not in list[-1:] and "100" not in list[-1:]:
            l = list[-1:]
        else:
            return 0
        y = 0
        for x in l:
            y += int(x)    
        return y
    def result(list):
        if "1000000" in list:
            return(1000000)
        elif "1000" in list:
            return thousand(list) + hundred(list) + lessthanhundred(list)
        elif "100" in list:
            return hundred(list) + lessthanhundred(list)
        else:
            return lessthanhundred(list)
    string = string.replace("-", " ")
    string = string.replace("eleven", "11")
    string = string.replace("twelve", "12")
    string = string.replace("thirteen", "13")
    string = string.replace("fourteen", "14")
    string = string.replace("fifteen", "15")
    string = string.replace("sixteen", "16")
    string = string.replace("seventeen", "17")
    string = string.replace("eighteen", "18")
    string = string.replace("nineteen", "19")
    string = string.replace("twenty", "20")
    string = string.replace("thirty", "30")
    string = string.replace("forty", "40")
    string = string.replace("fifty", "50")
    string = string.replace("sixty", "60")
    string = string.replace("seventy", "70")
    string = string.replace("eighty", "80")
    string = string.replace("ninety", "90")
    string = string.replace("hundred", "100")
    string = string.replace("thousand", "1000")
    string = string.replace("million", "1000000")
    string = string.replace("zero", "0")
    string = string.replace("one", "1")
    string = string.replace("two", "2")
    string = string.replace("three", "3")
    string = string.replace("four", "4")
    string = string.replace("five", "5")
    string = string.replace("six", "6")
    string = string.replace("seven", "7")
    string = string.replace("eight", "8")
    string = string.replace("nine", "9")
    string = string.replace("ten", "10")
    string = string.replace("and ", "")
    list = string.split(" ")
    return result(list)

x = input("Write the number:")
print(parse_int(x))
