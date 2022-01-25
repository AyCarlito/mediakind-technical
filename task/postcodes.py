from math import sqrt
import csv
import argparse


def get_arguments():
    """Command line argument parsing. 
    Returns:
        [Argparse Object]: Object containing command line arguments
    """
    parser = argparse.ArgumentParser(description='Mediakind Technical Task. Distance between two postcodes')
    parser.add_argument("p", help="Postcode", type=str)
    return parser.parse_args()

def get_postcode_data(postcode):
    """Get data for postcode from CSV file

    Data for all postcodes in single CSV file.
    Data for UK office in seperate CSV file for optimisation. O(n) -> O(1).
    
    CSV file, based on input string, is opened and linear search performed. 

    Args:
        postcode (String): Standard UK Postcode

    Returns:
        [Mixed]: Data for postcode. All fields returned. 
    """
    fname = "open_postcode_geo"
    if postcode == "SO30 4DA":
        fname = "office"
        
    with open(f"data/{fname}.csv", "r") as f:
        csv_file = csv.reader(f, delimiter=",")
        for row in csv_file:
            if row[0] == postcode:
                print(f"Found postcode: {postcode}")
                return row
        return None

def get_distance(p1, p2):
    """Calculate distance between two postcodes 

    Easting and Northing are projected planar coordinates (on an x,y grid).
    We can use Pythagoras' Theorem: c^2 = a^2 + b^2.
    Where c is the distance between the two points, a is difference in x (easting) coords and b is difference in y (northing) coords.
    
    Indexes 3 and 4 are easting and northing respectively.

    Args:
        p1 ([Mixed]): List of fields for first postcode.
        p2 ([Mixed]): List of fields for second postcode.
    """
    
    distance = sqrt(abs(int(p1[3]) - int(p2[3])) ** 2 + abs((int(p1[4]) - int(p2[4]))) ** 2)
    print(f"Distance between {p1[0]} and {p2[0]}: {distance}m")  
    return distance
    
def main():
    """Main Function

    Parse User arguments. 
    Get postcode data for UK office and user specified postcode.
    If postcode found is no longer active then stop execution.
    Calculate distance between the two postcodes.
    """
    
    args = get_arguments()
    office_data = get_postcode_data("SO30 4DA")
    user_postcode_data = get_postcode_data(args.p)

    if user_postcode_data is None:
        print(f"Postcode not found: {args.p}")
    elif user_postcode_data[1] == "terminated":
        print(f"{args.p} has been terminated")
    else:
        get_distance(office_data, user_postcode_data)


if __name__ == "__main__":
    main()