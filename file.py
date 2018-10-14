while True:
    com = ","
    print("Input Full Url or Press Enter to leave.")
    url = input("Full Url:")
    if url == "":
        break
    else:
        code = input("File Code:")
        desc = input("File Description:")
        print(url,"   ",code,"   ",desc)
        file = open('file.txt',"a")
        file.write(url)
        file.write(com)
        file.write(code)
        file.write(com)
        file.write(desc)
        file.write("\n")
        file.flush()
  
