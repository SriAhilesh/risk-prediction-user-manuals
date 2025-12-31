import csv

DATASET_PATH = "data/raw/instruction_misuse_dataset.csv"

def load_dataset(path):
    data = []
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    dataset = load_dataset(DATASET_PATH)
    print("Number of instructions:", len(dataset))
    print("\nSample entries:\n")
    for entry in dataset:
        print(entry)
