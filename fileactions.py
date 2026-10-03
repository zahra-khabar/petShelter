import os
import pickle  #I suddunly Found out this lib better than File operations

from shelter import Shelter


PATH = "shelter_data.pkl"


def write_to_file(file_name, data):
    try:
        file = open(file_name, mode="wb")
        pickle.dump(data, file)
        file.close()
    except Exception as e:
        print(f"Error saving {file_name}: {e}")


def read_from_file(file_name):
    if os.path.exists(file_name):
        try:
            file = open(file_name, mode="rb")
            data = pickle.load(file)
            file.close()
            return data
        except Exception as e:
            print(f"Error loading {file_name}: {e}")
    return []


def save_shelter(shelter: Shelter, path: str = PATH):
    write_to_file(path, shelter)
    print(f"Data saved to {path}")


def load_shelter(path: str = PATH) -> Shelter:
    data = read_from_file(path)
    if not data:
        print(f"File {path} not found.")
        return Shelter()
    print(f"Data loaded from {path}")
    return data