Writing rules :

1 : Comments should always start by %
2 : if you are commenting a particular line, it should be be on a line before the commanted line, 
exemple :
% this is a commant on the line bellow
data: data
Since the script is reading the file line by line,,  a commant on the same line could be intrepreted as data, or even ignored.

3 : use ":" to separate your data from it's value
exemple
my_data:data_value

4 : write your timing and date in the same line as followed  (24H format):
timing:yyyy/mm/dd:HH-mm


5 : when writting the data for a cell in the division section, follow this :
## DIVISIONS
# name_of_cell
data_name:data_value

Here the space between the "#" and the name of the cells is important to identify that we are treating a new cell.