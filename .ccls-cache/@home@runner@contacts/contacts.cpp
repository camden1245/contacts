#include <iostream>
#include <vector>
#include "contacts.hpp"

Contact::Contact(std::string first_name, std::string last_name, std::string phone, std::string email, std::string nickname)
 : first_name(first_name), last_name(last_name), phone(phone), email(email), nickname(nickname) {}

 std::string Contact::getFirstName() const {
    return first_name;
 }

std::string Contact::getLastName() const {
    return last_name;
 }
std::string Contact::getPhone() const {
    return phone;
 }

 std::string Contact::getEmail() const {
    return email;
 }

 std::string Contact::getNickname() const {
    return nickname;
 }

 void Contact::displayContact() const {
    std::cout << "First Name: " << first_name << "\n";
    std::cout << "Last Name: " << last_name << "\n";
    std::cout << "------------------\n";
    std::cout << "Phone #: " << phone << "\n";
    std::cout << "Email Address: " << email << "\n";
    std::cout << ">-------------------<\n";
}