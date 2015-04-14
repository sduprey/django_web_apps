'''
Created on 14 Apr 2015

@author: sduprey
'''
from comparator.datacollector import Datacollector
def main():
    # parse command line options
    my_sku = "TOS3700722498563"
    my_cds_pictures,my_kriter_pictures = Datacollector.get_pictures(my_sku)
    print my_cds_pictures
    print my_kriter_pictures
if __name__ == "__main__":
     main()