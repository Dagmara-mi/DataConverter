import sys
import os
import json
import xml.etree.ElementTree as ET


def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("JSON poprawny")
        return data
    except json.JSONDecodeError:
        print("Błąd: niepoprawny JSON")
        return None
    except Exception as e:
        print("Błąd:", e)
        return None


def save_json(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print("Zapisano do pliku JSON:", file_path)
    except Exception as e:
        print("Błąd zapisu:", e)


def load_yaml(file_path):
    try:
        data = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if ":" in line:
                    key, value = line.split(":", 1)
                    data[key.strip()] = value.strip()
        print("YAML poprawny")
        return data
    except Exception as e:
        print("Błąd YAML:", e)
        return None


def save_yaml(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
        print("Zapisano do pliku YAML:", file_path)
    except Exception as e:
        print("Błąd zapisu YAML:", e)


def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text

        print("XML poprawny")
        return data

    except Exception as e:
        print("Błąd XML:", e)
        return None


def save_xml(file_path, data):
    try:
        root = ET.Element("root")

        for key, value in data.items():
            elem = ET.SubElement(root, key)
            elem.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(file_path)

        print("Zapisano do pliku XML:", file_path)

    except Exception as e:
        print("Błąd zapisu XML:", e)


def main():
    if len(sys.argv) != 3:
        print("Użycie: program.exe plikWejściowy plikWyjściowy")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print("Błąd: plik nie istnieje")
        return

    if input_file.endswith(".json"):
        data = load_json(input_file)

        if data is not None:
            print("Wczytane dane:")
            print(data)

            save_json(output_file, data)

    elif input_file.endswith(".yml") or input_file.endswith(".yaml"):
        data = load_yaml(input_file)

        if data is not None:
            print("Wczytane dane:")
            print(data)

            save_yaml(output_file, data)

    elif input_file.endswith(".xml"):
        data = load_xml(input_file)

        if data is not None:
            print("Wczytane dane:")
            print(data)

            save_xml(output_file, data)


if __name__ == "__main__":
    main()


