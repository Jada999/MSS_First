"""
You are required to look through xlwings Doc at:
https://docs.xlwings.org/en/stable/quickstart.html
in 5 minutes and give an output like the picture
here: https://github.com/PercyCheng/Jacaranda-E/blob/master/William.png




You will have 10 minutes to finish your answer.

Submission: Python file or text file are accepted when you submit your answer.
You can submit directly with python file or text file using file name as "yourname_answer.py" or "yourname_answer.txt". eg: laowang_answer.py
Please submit directly to “Genevievechen1996@hotmail.com”
"""

# TODO: import xlwings libarary
import xlwings as xw
import pandas as pd

# TODO: initialize sheets(Sheet name is “[your name] + "_answer"” for example "Bob_answer")
wb = xw.Book()
sheet = wb.sheets['Jada_answer']

# TODO: finish Your Code

df = pd.DataFrame([['Liam','Noah','William','James','Logan','Benjamin','Mason','Elijah','Oliver','Jacob'],[1,2,3,4,5,6,7,8,9,10]],
                 index = ['name','student number'])

sheet.range('Jada_answer').value= df
sheet.range('Jada_answer').options(pd.DataFrame, expand='table').value

#Today I am writing code with Serena and Jada