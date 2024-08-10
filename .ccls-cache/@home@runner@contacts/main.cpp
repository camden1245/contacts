#include <iostream>
#include "contact_manager.hpp"
#include "contacts.hpp"

int main() {
    // Create a ContactManager object
    ContactManager manager;

    // Create some Contact objects
    Contact contact1("Alice","Smith", "123-456-7890", "asmith@gmail.com", "alice");
    Contact contact2("Bob", "Johnson", "987-654-3210","bobj12345@outlook.com","Bobby");

    // Add contacts to the manager
    manager.add_new_contact(contact1);
    manager.add_new_contact(contact2);

    // Display all contacts
    std::cout << "Contacts List:" << std::endl;
    manager.disp_all_contacts();

    return 0;
}