def read_employees(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def write_employees(file_path, employees):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(employees)


def main():
    # Step 1: Read employee data from the main database
    employees = read_employees("C:\\Users\\User\\PycharmProjects\\buteel\\ajilchid.txt")

    # Step 2: Print all employees' information
    print("All Employees from Main Database:")
    for employee in employees:
        print(employee.strip())

    # Step 3: Copy all employees to the Darkhan database
    write_employees("C:\\Users\\User\\PycharmProjects\\buteel\\darhan.txt", employees)

    # Step 4: Delete all information from the main database
    write_employees("C:\\Users\\User\\PycharmProjects\\buteel\\ajilchid.txt", [])

    # Re-read the Darkhan database to handle the next steps
    darkhan_employees = read_employees("C:\\Users\\User\\PycharmProjects\\buteel\\darhan.txt")

    # Step 5 and 6: Handle non-retired employees in the Darkhan database
    non_retired = [emp for emp in darkhan_employees if "тэтгэвэрт гарсан" not in emp]
    if non_retired:
        # Step 6: Copy back non-retired employees to the main database
        write_employees("C:\\Users\\User\\PycharmProjects\\buteel\\ajilchid.txt", non_retired)

        # Step 7: Delete these non-retired employees from the Darkhan database
        remaining = [emp for emp in darkhan_employees if emp not in non_retired]
        write_employees("C:\\Users\\User\\PycharmProjects\\buteel\\darhan.txt", remaining)

    print("Processing complete. Data has been transferred and cleaned accordingly.")


if __name__ == "__main__":
    main()