#include <iostream> 
#include "contacts.hpp"
#include "contact_manager.hpp"
#include <vector>

void ContactManager::add_new_contact(const Contact& contact){
    contacts.push_back(contact);
};
void ContactManager::disp_all_contacts() {
    for (const auto& contact : contacts) {
        contact.displayContact();
        std::cout << "--------------" << std::endl;
    }
}
