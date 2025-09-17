# Programming-Assignment-3
## Experiment 3 - Python Data Analysis (PANDAS)
### Intended Learning Outcomes
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library
### Given Problems
1. PROBLEM 1
2. PROBLEM 2
------------------------------------------
## PROBLEM 1
Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas

b. Display the first five and last five rows of the resulting cars.

### My Code (Part A)
```python
import pandas as pd
```
```python
#load the corresponding .csv file

cars = pd.read_csv('cars.csv') 
cars
```
```python
#displays the first five rows

cars.head()
```
<img width="557" height="173" alt="image" src="https://github.com/user-attachments/assets/4556ee9b-b83e-49dc-8c5b-e70463520616" />

### My Code (Part B)
```python
#displays the last five rows

cars.tail()
```
<img width="535" height="177" alt="image" src="https://github.com/user-attachments/assets/d2bdd4eb-be78-4580-9127-53e5820dd436" />

### Explanation
1. **Accessing Pandas Library** - 
To access Pandas library, the import convention must be used: import numpy as pd.
2. **Loading the Corresponding .csv File** -
To load the .csv file, we use the code: cars = pd.read_csv('cars.csv'). This will display the dataframe
3. **Display the First 5 Rows** -
To display the first five rows, we use the code: cars.head(). By default, this will display the first five rows, but can be changed once you specify the number of rows you want by inputting a number between the parenthesis.
4. **Display the Last 5 Rows** -
To display the last five rows, we use the code: cars.tail(). By default, same with the code cars.head(), cars.tail() will display the last five rows but can be changed once you specify the number of rows you want by also inputting a number between the parenthesis.
------------------------------------------
## PROBLEM 2
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### My Code
```python
import pandas as pd
```
```python
#load the corresponding .csv file

cars = pd.read_csv('cars.csv') 
cars
```
### My Code (Part A)
```python
#filters the dataframe to only display the first five rows with odd numbered columns

cars.iloc[:5, ::2] 
```
<img width="319" height="177" alt="image" src="https://github.com/user-attachments/assets/7768ed86-92b1-40d8-ab4c-6bca2e8066ad" />

### My Code (Part B)
```python
#filters the dataframe to display the row that contains the Mazda RX4 Model

cars.loc[cars['Model']=='Mazda RX4']
```

<img width="506" height="59" alt="image" src="https://github.com/user-attachments/assets/a1e36039-1afe-4e95-abea-5fbc2dc9be4f" />

### My Code (Part C)
```python
#filters the dataframe to only display the cyl of the Camaro Z28 model 

cars.loc[(cars['Model']=='Camaro Z28'),['cyl']]
```

<img width="58" height="53" alt="image" src="https://github.com/user-attachments/assets/de63afdb-e328-4d2f-a80e-619bfd77c5ca" />

### My Code (Part D)
```python
#filters the dataframe to only display what the cyl and gear each model has

cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']] 
```

<img width="206" height="114" alt="image" src="https://github.com/user-attachments/assets/fc7393b1-7742-42e7-af5f-77ab04940849" />

### Explanation
1. **Accessing Pandas Library** - 
To access Pandas library, the import convention must be used: import numpy as pd.
2. **Loading the Corresponding .csv File** -
To load the .csv file, we use the code: cars = pd.read_csv('cars.csv'). This will display the dataframe
3. **Display the First 5 Rows with Odd Numbered Columns** -
To display the first five rows with odd numbers columns, we use the code: cars.iloc[:5, ::2]. This filters the data to display the first five rows (:5) and will display the odd numbered columns (::2, this commands the code to take every 2nd column of the data frame)
4. **Display the Model of Mazda RX4** -
To display the model of Mazda RX4, we use the code: cars.loc[cars['Model']=='Mazda RX4']. This will display the row that contains the Mazda RX4 Model and its features.
5. **Display the cyl of the Camaro Z28 Model** -
To display the cylinders of Camaro Z28 Model, we use the code: cars.loc[(cars['Model']=='Camaro Z28'),['cyl']]. This will display the cylinders of the Camaro Z28 car model. 
6. **Display the cyl and gear of the specified car models** -
To display the cylinders and gear of the specified car models, namely, the Mazda RX4 Wag, Ford Pantera L, and Honda Civic, we use the code: cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]. This will display the row that contains the needed car models and their cylinders and gears.











