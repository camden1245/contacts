#ifndef CONTACTS_HPP
#define CONTACTS_HPP

#include <iostream>
#include <string> 

class Contact {
    private:
        std::string first_name;
        std::string last_name;
        std::string phone;
        std::string email;
        std::string nickname;

    public:
        Contact(std::string first_name, std::string last_name, std::string phone, std::string email, std::string nickname);
        std::string getFirstName() const;
        std::string getLastName() const;
        std::string getPhone() const;
        std::string getEmail() const;
        std::string getNickname() const;
        void displayContact() const;
};

#endif // CONTACTS_HPP
