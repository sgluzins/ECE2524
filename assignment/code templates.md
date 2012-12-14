Name of source file: currency.py

Your program should accept the following command line arguments (CLAs):
-h, --help: display usage instructions and exit
-r, --rate: display the exchange rate that you have choosen with a subparser of the country
-c, --convert: convert the specified amount and currencies

Here are examples of an ideal correct program operation:

./currency.py -r US
1 US Dollar
1074.65 Korea Won
0.76 Europe Euro
83.87 Japan Yen
5.70 Denmark Danish Krone

./currency.py -r Korea
1000 Korea Won
0.71 Europe Euro
0.93 US Dollar
78.07 Japan Yen
5.30 Danish Krone

./currency.py -c 1000 Dollar Won
1,074,650

