import sys
import os

def main():
    # sprawdzam ilość argumentów
    if len(sys.argv) != 3:
        print("Użycie; program.exe plikWejściowy plikWyjściowy")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print ("Plik wejściowy:", input_file)
    print("Plik wyjściowy:", output_file)

    # sprawdzam czy plik istnieje
    if not os.path.exists(input_file):
        print("Błąd: plik wejściowy nie istnieje")
        return
    
    print("Plik istnieje - OK")

if __name__== "__main__":
    main()