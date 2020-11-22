"""generates number"""

import sys

from number_generator import ContactGetter


def main(num=100):
#     print(num)
    x = ContactGetter(int(num))

    path_to_data = 'data/contact.txt'

    contact_list = x.get_dataset(path_to_data)
    
    print('\nDone')
    print('_'*10)
    print(f'\nLength of dataset -> {len(contact_list)}')
    
                               # check to see if we have the data
    print(f'\nPreview sample: {contact_list[:5]}\n')
    
if __name__ == '__main__':
    main(sys.argv[-1])