#ifndef CONTACT_MANAGER_HPP
#define CONTACT_MANAGER_HPP

#include <iostream>
#include <vector>
#include "contacts.hpp" 
class ContactManager {
    private:
        std::vector<Contact> contacts;

    public:
        void add_new_contact(const Contact& contact);
        void disp_all_contacts();
};

#endif // CONTACT_MANAGER_HPP
