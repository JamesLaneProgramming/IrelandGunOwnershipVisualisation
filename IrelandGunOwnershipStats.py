import numpy as np
import matplotlib.pyplot as plt
import csv

#59588 entries

'''The CSV file contains a location field.
This field is redacted for security.'''
ages = []
genders = []
numberOfGuns = []
types = []

def retrieveCSVData():
    '''
    Extracts data from a CSV file and

    Raises
    ------
    IOError:
        If the file cannot be opened with read privileges.
    EOFError:
        If the file encounters an unexpected End Of Line
    
    Returns
    -------
        Array:
            The extracted ages from the CSV file
        Array:
            The extracted genders from the CSV file
        Array:
            The extracted numberOfGuns from the CSV file
        Array:
            The extracted types from the CSV file
    '''
    stream = None
    try:
        stream = open('gunOwnershipData', 'r')
    except IOError as error:
        raise error
        print(error.args)
        #Handle IOErrors here
    try:
        reader = csv.reader(stream)
    except EOFError as error:
        raise error
        print(error.args)
        #Handle EOFErrors here.
    for row in reader:
        ages.append(row[1])
        genders.append(row[2])
        numberOfGuns.append(row[3])
        types.append(row[4])
    stream.close()
    try:
        assert(len(ages) != 0)
        assert(len(genders) != 0)
        assert(len(numberOfGuns) != 0)
        assert(len(types) != 0)
    except AssertionError:
        print """No IOError or EOFError occured but could not extract data,
        please ensure that the file is not empty"""
        raise
    return ages, genders, numberOfGuns, types

def seperateGunTypes():
    '''
    Iterates through license types and cleans data.
    Holders can own multiple license types

    Raises
    ------
    TypeError
        If the global types is not of type list
    ValueError
        If the global types has a length of 0
    '''
    global types
    if(type(types) != list):
        raise TypeError
    assert(len(types) != 0)
    splitLicenseTypes = list()
    for licenseTypes in types:
        assert(type(licenseTypes) == str)
        licenses = licenseTypes.split('+')
        for license in licenses:
            splitLicenseTypes.append(license)
    types = splitLicenseTypes

#These graphs plot gun ownership of Ireland residents.
def renderGraphs():
    x = ages
    y = numberOfGuns

    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'o-')
    plt.title('Number of Guns over age of owner')
    plt.ylabel('Number of guns')

    #Save the graph to a file.
    plt.savefig('barGraph.png')

    '''
    Extract the unique elements within the gun license classes as well as the 
    frequency of occurence
    '''
    unique_elements, element_counts = np.unique(types, return_counts = True)

    fig1, ax1 = plt.subplots()
    ax1.pie(element_counts, labels=unique_elements, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #Save the graph to a file.
    plt.savefig('pieGraph.png') 

def main():
    ages, genders, numberOfGuns, types = retrieveCSVData()
    seperateGunTypes()
    renderGraphs()
    plt.show()

#If this is not run then main is being run through a different namespace
if __name__ == '__main__':
    main()
else:
    print("The main method is being called externally")
