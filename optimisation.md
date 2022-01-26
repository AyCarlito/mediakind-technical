# Optimisation Discussion


* Search Algorithm - Currently, the program performs a linear search through the CSV file. This is O(n) time complexity in the worst case. Since the CSV file is alphabetically sorted we could perform a binary search having time complexity O(log n). A drawback of this approach is the overhead of loading into memory. We could further reduce the time complexity to O(1) through preprocessing the dataset into JSON format. Again this has the drawback of needing to load into memory first as opposed to the linear search which simply iterates through the CSV file. Scalability may be a concern when loading into memory if the functionality of the program is extended to use a dataset of world postcodes in place of ONS UK figures. Additionally, to alleviate the concerns with loading into memory, preprocess the data to focus on relevant columns ("postcode", "status", "northing" and "easting") by dropping redundant columns.

* Execution Order - Find user-specified postcode before progressing. If the user-specified postcode does not exist, end execution. User-specified -> UK Office instead of UK office -> User specified. Additionally, check the status field of user-specified postcode following retrieval. End execution if postcode is terminated.

* Input Validation - A UK postcode is one of five standard formats. We could use regex to validate the format of the input string to eliminate the subsequent linear search for a postcode in an invalid format. Note that this would only validate the format of the input string and not whether the postcode exists. Promote better usability of the program by showing the five formats in the terminal when the "-h" flag is used. 

* CSV Files - The UK Office postcode is consistent and required on each run of the program. Optimise by extracting it and placing it in a separate  CSV file. Additionally, we could create CSV files for each letter that a postcode starts with (26 in total - each file occupying ~3.85% of the dataset - if normally distributed -(a histogram would provide the accurate distribution)). For a postcode "F" we search in the "F" file where previously "A-E" would be iterated through first. 




