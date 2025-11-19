# a more robust data profiler function for the week 2 assignment
import pandas as pd


def data_profiler():

  path_csv = str(input('Enter file path: '))
  
  try: 
    df = pd.read_csv(path_csv)

  except FileNotFoundError:
    print(f"Error: File not found at {path_csv}")
    return None
  except pd.errors.ParserError: # the except for parsing issues (looked up in the pandas documentation)
    print('Parse error')
    return None
  except Exception as e: # this was recommended as a friendlier catch-all for any other exceptions
    print(f'An error occurred: {e}')
    return None
  else:                           
    shape = df.shape
    data_types = df.dtypes
    null_check = df.isnull().sum()
    desc_stats = df.describe()
    cat_summary = df.describe(include="object")    


    # I still want to print the info out to the console
    print(f'Data source: \n {path_csv}\n')
    print(f'Shape:\n {shape}')
    print('\nColumn Names and Data Types: \n')
    print(data_types)
    print('\nNull Values per Column:\n')
    print(null_check)
    print('\nDescriptive Statistics for Numerical Columns:\n')
    print(desc_stats)
    print('\nCategorical Summary:\n')
    print(cat_summary)

    
    # I guess this could be cleaned up but was testing formatting of the output
    output_path = 'output.txt'
    with open(output_path, "w", newline='') as fs:
      fs.write('Data source: \n')
      fs.write(path_csv)
      fs.write('\n \n')
      fs.write('Dataframe Shape:')
      fs.write('\n \n')
      fs.write(str(shape))
      fs.write('\n \n \n')
      fs.write('Column Names and Data Types:')
      fs.write('\n \n')
      fs.write(str(data_types))
      fs.write('\n \n \n')
      fs.write('Null Values per Column: \n \n')
      fs.write(str(null_check))
      fs.write('\n \n \n')
      fs.write('Descriptive Statistics for Numerical Columns:\n \n')
      fs.write(str(desc_stats))
      fs.write('\n \n \n')
      fs.write('Categorical Summary:\n \n')
      fs.write(str(cat_summary))
      fs.write('\n \n \n')

    # Let the user know where the file is saved
    print(f"\nYour file is saved to {output_path}")
    


data_profiler()