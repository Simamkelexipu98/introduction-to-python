
def main():
    Filename = fileName(input("filename ? "))
    print(Filename)


def fileName(extensions):
    extensions = extensions.strip()
    extensions = extensions.lower()
    if extensions.find(".jpg") != -1 or extensions.find(".jpeg") != -1  :
        fileformat = "image/jpeg"
        return fileformat

    elif  extensions.find(".gif") != -1:
       fileformat1 ="image/gif"
       return fileformat1

    elif  extensions.find(".png") != -1:
        fileformat2 ="image/png"
        return fileformat2

    elif extensions.find(".pdf") != -1:
        fileformat3 = "application/pdf"
        return fileformat3

    elif  extensions.find(".zip") != -1:
        fileformat4 = "application/zip"
        return fileformat4

    elif  extensions.find(".txt") != -1:
        fileformat5 = "text/plain"
        return fileformat5
    else:
        fileformat6 ="application/octet-stream"
        return fileformat6
main()
