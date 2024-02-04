import os
from openai import OpenAI
from errorResult import ErrorResult
from result import Result
import re
import pyodbc

class openAIHelper:
  def __init__(self, message) -> None:
    self.apiKey = os.getenv("api_secret")
    self.message = message

  def getScript(self) -> object:
    try:
      client = OpenAI(api_key=self.apiKey)
      response = client.chat.completions.create(
      model= "gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": '''Given the following SQL tables, 
                        your job is to write queries given a user’s request.
                        
                        CREATE TABLE Orders (
                          OrderID int,
                          CustomerID int,
                          OrderDate datetime,
                          OrderTime varchar(8),
                          PRIMARY KEY (OrderID)
                        );
                        
                        CREATE TABLE OrderDetails (
                          OrderDetailID int,
                          OrderID int,
                          ProductID int,
                          Quantity int,
                          PRIMARY KEY (OrderDetailID)
                        );

                        CREATE TABLE Products (
                          ProductID int,
                          ProductName varchar(50),
                          Category varchar(50),
                          UnitPrice decimal(10, 2),
                          Stock int,
                          PRIMARY KEY (ProductID)
                        );

                        CREATE TABLE Customers (
                          CustomerID int,
                          FirstName varchar(50),
                          LastName varchar(50),
                          Email varchar(100),
                          Phone varchar(20),
                          PRIMARY KEY (CustomerID)
                        );
                        '''
        },
        {
          "role": "user",
          "content": "return just T-SQL"
        }, 
        {
          "role": "user",
          "content": "please write T-sql script between ```sql and ```"
        },
        {
          "role": "user",
          "content": self.message
        }
      ])
      
      script = ''
      gpt_result = response.choices[0].message.content
      print(f'response.choices len: {len(response.choices)}')
      scripts = re.findall(rf'{"###"}(.*?){"###"}', gpt_result.replace('\n','#N#').replace('```','###').replace('###sql','###'))
      if len(scripts) == 0:
        script = gpt_result
      else:
        script = scripts[0].upper().replace('#N#',' ').replace('#N',' ')
      
      if("DELETE" in script or "UPDATE" in script or "INSERT" in script):
        return Result.fail(ErrorResult("متن شما شامل دستور غیرمجاز است"))
      
      return Result.success({
                  'main_result' : gpt_result,
                  'script':script
                  })
    except Exception as err:
      return Result.fail(ErrorResult(err))
    
  def getDataFormDB(self) -> object:
    result = {
        "t-sql": "",
        "gpt-result" : "",
        "data": []
      }
     
    try:
      script_result = self.getScript()
      if not script_result.succeed:
        return Result.fail(ErrorResult(script_result), result)
      
      result["t-sql"] = script_result.data['script']
      result["gpt-result"] = script_result.data['main_result']
      script = script_result.data['script']

      con = pyodbc.connect(driver="{SQL Server}", server=".\\SQL2022", database="TestGPT", uid="sa", pwd="sas")
      cur = con.cursor()
      db_cmd = script
      res = cur.execute(db_cmd)
      desc = res.description
      column_names = [col[0] for col in desc]
      # result["data"] = [dict(zip(column_names, row)) for row in res.fetchall()]
      for row in res.fetchall():
        obj = {}
        column_index = 0
        for column in column_names:
          obj[column] = str(row[column_index])
          column_index += 1
        result["data"].append(obj)

      # Do something with your result set, for example print out all the results:
      return Result.success(result)
    except Exception as err:
      return Result.fail(ErrorResult(err), result)