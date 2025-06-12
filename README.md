**PROJECT NAME: CONTACTS AND GROUP ORGANIZER PROJECT**


This document serves as a complete and explanation of how the project works, outlining its purpose, structure, and the steps taken to implement its core features. 
Through this README, you will gain a clear understanding of the system’s objectives, the technical approach used, and how each part of the program contributes to the final outcome in the following ways:


**ASSIGNED TASK**

The assigned task was to design and implement a C++ program that can manage a list of contacts and organize them into groups. The program should allow users to:

- Add and categorize contacts as either *Family* or *Professional*
- Create custom groups to organize contacts
- Add or remove contacts from any group
- Delete entire groups when needed
- View all contacts and see their group affiliations


The objective of the task was to apply core principles of **object-oriented programming (OOP)**—such as inheritance, polymorphism, encapsulation, and dynamic memory management—to build a **fully functional, interactive system**.



This task also aimed to assess the developer's ability to work with:

- Abstract classes and virtual functions
- Structs for composite data organization
- Menu-driven interfaces
- Dynamic arrays and memory allocation in C++



How the Task Was Completed:
  -The solution was implemented entirely in C++ using an **object-oriented and modular design**. Here’s a breakdown of how the task was completed:


CONTACT MANAGEMENT 
 - Two specialized classes **FamilyContact** and **ProfessionalContact** were created to represent different types of contacts.
 - These classes inherit from an abstract base class **ContactBase**, which defines virtual functions for displaying and retrieving contact names.


GROUP MANAGEMENT
- Groups are implemented as a dynamic structure using a **Group** struct.
- Each group holds a dynamic array of pointers to contact objects (polymorphic), allowing flexible group composition.


**CORE FUNCTIONALITIES IMPLIMENTED**
Functionality              Implementation Details                                                                 

 Add Contact              : Prompts user to enter contact info and type (Family or Professional), stores dynamically 

 Add Group                : Dynamically adds a group with space to hold future members  
                            
 Remove Group             : Deletes a group and its associated members from memory  
                                
 Add Member to Group      :User selects an existing contact to assign to a selected group    
                      
 Remove Member from Group : Removes a specific contact from a group without deleting the contact itself
            
 Display All              :Lists all contacts and displays each group with its current members 

                    

Dynamic Memory Management
 - All contacts and groups are stored in dynamically allocated arrays that resize when capacity is exceeded.
 - Proper deallocation **(delete[],delete)** is handled before program termination to avoid memory leaks.
   

User Interface
 - A simple console-based menu is provided.
 - Input handling includes clearing input buffers to avoid data skipping or crashing.
 - All user operations are driven by intuitive prompts and clean display formatting.


