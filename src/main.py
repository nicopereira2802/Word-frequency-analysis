import re
import os

def main():

    counter = {}
    file_path = "data/input.txt"
    output_path= "output/results.txt"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:

                line = line.lower()
                line = re.sub(r"[^\w\s]", "", line)

                words = line.split()

                for i in words:
                    if i in counter:
                        counter[i] += 1
                    else:
                        counter[i] = 1

        sorted_words = sorted(counter.items(), key=lambda x: x[1],reverse=True)

        os.makedirs("output", exist_ok=True)

        with open(output_path, "w",encoding="utf-8") as out:

            header = f"{'WORD':<15} | {'FREQUENCY':<10}"
            separator = "-" *30

            print(header)
            print(separator)

            out.write(header +"\n")
            out.write(separator + "\n")

            for word, i in sorted_words[:10]:

                line = f"{word:<15} | {i:<10}"

                print(line)
                out.write(line +"\n")

        print(f"\nResults saved in {output_path}")

    except FileNotFoundError:
        print("Error!! file not found!!!!")
    

if __name__ == "__main__":
    main()