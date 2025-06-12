#include <iostream> // For input/output operations
#include <cstring>  // For C-style string functions like strcpy, strcmp
#include <limits>   // For numeric_limits used in clearing input buffer
using namespace std;

// Structure to hold contact details
struct Contact {
    char name[30];  // Contact's name
    char phone[15]; // Contact's phone number
};

// Abstract base class for contacts
class ContactBase {
public:
    virtual void display() = 0;             // Pure virtual function to display contact
    virtual const char* getName() = 0;      // Pure virtual function to get contact name
    virtual ~ContactBase() {}               // Virtual destructor
};

// Derived class for family contacts
class FamilyContact : public ContactBase {
    Contact info; // Holds name and phone
public:
    FamilyContact(const Contact& c) {
        strcpy(info.name, c.name);   // Copy name from input
        strcpy(info.phone, c.phone); // Copy phone from input
    }
    void display() override {
        cout << "[Family] Name: " << info.name << ", Phone: " << info.phone << endl;
    }
    const char* getName() override {
        return info.name; // Return contact's name
    }
};

// Derived class for professional contacts
class ProfessionalContact : public ContactBase {
    Contact info; // Holds name and phone
public:
    ProfessionalContact(const Contact& c) {
        strcpy(info.name, c.name);   // Copy name
        strcpy(info.phone, c.phone); // Copy phone
    }
    void display() override {
        cout << "[Professional] Name: " << info.name << ", Phone: " << info.phone << endl;
    }
    const char* getName() override {
        return info.name; // Return name
    }
};

// Structure for a group that contains a name and a dynamic array of members
struct Group {
    char groupName[20];           // Name of the group
    ContactBase** members;        // Dynamic array of pointers to members
    int memberCount, capacity;    // Track number of members and current capacity
};

// Global contact list
ContactBase** allContacts = new ContactBase*[100]; // Stores up to 100 contact pointers
int contactCount = 0;                              // Number of contacts added

// Global group list
Group* allGroups = nullptr;  // Pointer to array of groups
int groupCount = 0;          // Number of groups
int groupCapacity = 2;       // Initial group array capacity

// Function to add a new contact
void addContact() {
    Contact c;   // Temporary contact struct
    char type;   // Type of contact: F or P

    cout << "Enter name: ";
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Clear any leftover input
    cin.getline(c.name, 30); // Get contact name

    cout << "Enter phone: ";
    cin.getline(c.phone, 15); // Get phone number

    cout << "Type (F/P): ";
    cin >> type; // Ask whether contact is Family or Professional

    // Add contact based on type
    if (type == 'F' || type == 'f')
        allContacts[contactCount++] = new FamilyContact(c);
    else if (type == 'P' || type == 'p')
        allContacts[contactCount++] = new ProfessionalContact(c);
    else
        cout << "Invalid type!\n";
}

// Function to add a new group
void addGroup(const char* name) {
    // Allocate memory for group list if it's the first group
    if (groupCount == 0)
        allGroups = new Group[groupCapacity];
    // If array is full, increase capacity
    else if (groupCount >= groupCapacity) {
        groupCapacity *= 2;
        Group* temp = new Group[groupCapacity];
        for (int i = 0; i < groupCount; i++) temp[i] = allGroups[i];
        delete[] allGroups;
        allGroups = temp;
    }

    // Set new group details
    strcpy(allGroups[groupCount].groupName, name);
    allGroups[groupCount].memberCount = 0;
    allGroups[groupCount].capacity = 2;
    allGroups[groupCount].members = new ContactBase*[2];
    groupCount++; // Increase group count
    cout << "Group added!\n";
}

// Function to remove a group by name
void removeGroup(const char* name) {
    for (int i = 0; i < groupCount; i++) {
        if (strcmp(allGroups[i].groupName, name) == 0) {
            delete[] allGroups[i].members; // Free memory of group's members
            for (int j = i; j < groupCount - 1; j++)
                allGroups[j] = allGroups[j + 1]; // Shift groups left
            groupCount--; // Reduce count
            cout << "Group removed!\n";
            return;
        }
    }
    cout << "Group not found!\n";
}

// Function to add a contact to a group
void addMember(const char* groupName) {
    if (contactCount == 0) {
        cout << "No contacts available. Please add contacts first.\n";
        return;
    }

    Group* grp = nullptr;
    // Search for group by name
    for (int i = 0; i < groupCount; i++) {
        if (strcmp(allGroups[i].groupName, groupName) == 0) {
            grp = &allGroups[i];
            break;
        }
    }

    if (!grp) {
        cout << "Group not found!\n";
        return;
    }

    // Display all available contacts
    cout << "\nAvailable contacts:\n";
    for (int i = 0; i < contactCount; i++) {
        cout << i + 1 << ". ";
        allContacts[i]->display();
    }

    char contactName[30];
    cout << "Enter contact name to add: ";
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Clear input buffer
    cin.getline(contactName, 30); // Get contact name

    ContactBase* ct = nullptr;
    // Find contact by name
    for (int i = 0; i < contactCount; i++) {
        if (strcmp(allContacts[i]->getName(), contactName) == 0) {
            ct = allContacts[i];
            break;
        }
    }

    if (!ct) {
        cout << "Contact not found!\n";
        return;
    }

    // Resize member array if full
    if (grp->memberCount >= grp->capacity) {
        int newCap = grp->capacity * 2;
        ContactBase** temp = new ContactBase*[newCap];
        for (int i = 0; i < grp->memberCount; i++) temp[i] = grp->members[i];
        delete[] grp->members;
        grp->members = temp;
        grp->capacity = newCap;
    }

    // Add member to group
    grp->members[grp->memberCount++] = ct;
    cout << "Member added!\n";
}

// Function to remove a contact from a group
void removeMember(const char* groupName, const char* contactName) {
    for (int i = 0; i < groupCount; i++) {
        if (strcmp(allGroups[i].groupName, groupName) == 0) {
            Group& grp = allGroups[i];
            for (int j = 0; j < grp.memberCount; j++) {
                if (strcmp(grp.members[j]->getName(), contactName) == 0) {
                    // Shift members left
                    for (int k = j; k < grp.memberCount - 1; k++)
                        grp.members[k] = grp.members[k + 1];
                    grp.memberCount--;
                    cout << "Member removed!\n";
                    return;
                }
            }
        }
    }
    cout << "Member or group not found!\n";
}

// Function to display all contacts and groups
void displayGroups() {
    cout << "\n ALL CONTACTS \n";
    for (int i = 0; i < contactCount; i++)
        allContacts[i]->display(); // Display all contacts

    if (groupCount == 0) {
        cout << "\nNo groups available.\n";
        return;
    }

    // Display groups and their members
    cout << "\n Groups \n";
    for (int i = 0; i < groupCount; i++) {
        cout << "\nGroup: " << allGroups[i].groupName << endl;
        if (allGroups[i].memberCount == 0)
            cout << "  No members.\n";
        else
            for (int j = 0; j < allGroups[i].memberCount; j++)
                allGroups[i].members[j]->display();
    }
}

// Main function with menu interface
int main() {
    int choice;         // User menu choice
    char name1[30], name2[30]; // Names used for group and contact

    while (true) {
        // Display menu
        cout << "\n CONTACT & GROUP ORGANIZER \n";
        cout << "1. Add Contact\n2. Add Group\n3. Remove Group\n4. Add Member\n";
        cout << "5. Remove Member\n6. View Groups\n7. Exit\nChoice: ";
        cin >> choice;

        // Menu action based on user input
        switch (choice) {
            case 1: addContact(); break;
            case 2:
                cout << "Enter group name: ";
                cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                cin.getline(name1, 20);
                addGroup(name1);
                break;
            case 3:
                cout << "Enter group name to remove: ";
                cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                cin.getline(name1, 20);
                removeGroup(name1);
                break;
            case 4:
                cout << "Enter group name: ";
                cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                cin.getline(name1, 20);
                addMember(name1);
                break;
            case 5:
                cout << "Enter group name: ";
                cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                cin.getline(name1, 20);
                cout << "Enter contact name: ";
                cin.getline(name2, 30);
                removeMember(name1, name2);
                break;
            case 6:
                displayGroups(); // Show everything
                break;
            case 7:
                // Exit program and clean memory
                cout << "Exiting...\n";
                for (int i = 0; i < contactCount; ++i) delete allContacts[i];
                for (int i = 0; i < groupCount; ++i) delete[] allGroups[i].members;
                delete[] allGroups;
                delete[] allContacts;
                return 0;
            default:
                cout << "Invalid choice!\n"; // Handle invalid input
        }
    }
}
