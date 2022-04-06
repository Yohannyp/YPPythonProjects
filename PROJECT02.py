def print_results():
    
    print("Minimum number of packages of hot dogs required = ", number_hotdogs_packages_needed)
    print("Minimum number of packages of hot dog buns required = ", number_hotdogs_buns_needed)

    print("Number of hot dogs that will be left over = ", number_hotdogs_leftover)
    print("Number of hot dog buns that will be left over = ", number_hotdogs_buns_leftover)
   

if __name__ == '__main__': 

    number_people_attending = int(input("Enter the number of people attending: "))
    number_hotdogs_per_person = int(input("Enter the number of hot dogs per person: "))

    number_hotdogs_per_package = 10
    number_buns_per_package = 8

    total_number_of_hotdogs = number_people_attending * number_hotdogs_per_person

    number_hotdogs_packages_needed = total_number_of_hotdogs // number_hotdogs_per_package
    number_hotdogs_buns_needed = total_number_of_hotdogs // number_buns_per_package

    number_hotdogs_leftover = total_number_of_hotdogs % number_hotdogs_per_package
    number_hotdogs_buns_leftover = total_number_of_hotdogs % number_buns_per_package

    print_results()
