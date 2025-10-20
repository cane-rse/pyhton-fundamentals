def number_converter():
    print("Welcome to the Universal Number Converter!\n")
    print("Supported bases: decimal, binary, octal, hex")
    
    while True:
        number = input("\nEnter a number (or type 'exit' to quit): ").strip()
        if number.lower() == "exit":
            print("Exiting Number Converter. Goodbye!")
            break

        input_base = input("Enter the base of your number: ").strip().lower()
        output_base = input("Enter the base to convert to: ").strip().lower()

        # Convert input to decimal first
        try:
            if input_base == "decimal":
                num = int(number)
            elif input_base == "binary":
                num = int(number, 2)
            elif input_base == "octal":
                num = int(number, 8)
            elif input_base == "hex":
                num = int(number, 16)
            else:
                print("❌ Invalid input base. Try again.")
                continue
        except ValueError:
            print("⚠️ Invalid number for the specified input base. Try again.")
            continue

        # Convert decimal number to desired output base
        if output_base == "decimal":
            result = str(num)
        elif output_base == "binary":
            result = bin(num)[2:]
        elif output_base == "octal":
            result = oct(num)[2:]
        elif output_base == "hex":
            result = hex(num)[2:].upper()
        else:
            print("❌ Invalid output base. Try again.")
            continue

        print(f"\n✅ Conversion Result: {number} ({input_base}) → {result} ({output_base})")

if __name__ == "__main__":
    number_converter()
