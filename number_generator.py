# import necessary packages
import random

class ContactGetter:
    """ This the Class of Random contacts"""
    
    
    def __init__(self, maxLen):
        self.maxLen = maxLen
    
    
    def gen_phone(self):
        """generate random contacts and also makes random noise to the numbers"""
        first = str(random.choice([54, 26]))
        second = str(random.randint(0, 998)).zfill(3)
        last = str(random.randint(0, 9998)).zfill(4)

        return '+233-{}- {} -{}'.format(first, second, last)
    
    def make_dataset(self):
        """This function creates the contact list"""

        contacts = [self.gen_phone() for _ in range(self.maxLen)]

        with open("data/contact.txt", "w") as f:
               for item in contacts:
                    f.write("%s\n"%item)
        f.close()
    
    def get_dataset(self, path_data):
        """This function get and cleans the dataset"""
        self.make_dataset()
        file = open(path_data, "r")
        contact_list = file.readlines()

        contacts = []
        for i in range(len(contact_list)):
            contacts.append(("".join(contact_list [i].split('\n')[0].replace(" ", ""))))

        return contacts
        file.close()
        
    def length(self):
        return self.maxLen