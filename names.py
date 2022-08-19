def read_sort(filename):
    with open(filename) as fp:
        file_text = fp.read()
        str_names = file_text.splitlines()
        str_names.sort()
        return str_names



def main():
    sorted_names = read_sort("sorted_names.csv")
    with open("sorted_names.csv",  "w") as sfp:
        for name in sorted_names:
            sfp.write(f"{name}\n" )

if __name__ == "__main__":
    main()


