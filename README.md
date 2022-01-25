# Mediakind Technical Task - Daniel Hislop

Program to calculate distance between Mediakind UK office and user specified postcode using northing and easting coordinates. 


Optimisation discussion can be found in ```optimisation.md```

## Prerequisites

Python Version: 3.8.10 or greater

Pip Version : 20.0.2 or greater

## Installation 

Clone repository:
```
git clone https://github.com/AyCarlito/mediakind-technical
```

In root directory, the required libraries can be installed using the command:

```
pip3 install -r requirements.txt
```

Grab dataset and replace existing files in ```data``` folder:
```
https://www.getthedata.com/downloads/open_postcode_geo.csv.zip
```

## Usage
In root directory:
```
python3 -m task.postcodes <postcode>
```

In root directory. Access help information:
```
python3 -m task.postcodes -h
```

## Testing

In root directory:
```
pytest tests/tests.py
```


**NB: If using windows, use the py alias for python. If on Linux, use python3. If neither of these work or apply then use the alias you have set on your system.**