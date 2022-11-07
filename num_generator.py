import random

import pandas as pd

excel_data = pd.read_csv(
  "https://www.texaslottery.com/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv"
)

# # loc [row, column] index first row = 0,
# excel_data.loc[,4]="num1"
# excel_data.loc[0,5]="num2"
# excel_data.loc[0,6]="num3"
# excel_data.loc[0,7]="num4"
# excel_data.loc[0,8]="num5"
# excel_data.loc[0,9]="power"
#

#getting columns

num1 = excel_data['37'].tolist()
num2 = excel_data['52'].tolist()
num3 = excel_data['22'].tolist()
num4 = excel_data['36'].tolist()
num5 = excel_data['17'].tolist()
power = excel_data['24'].tolist()
len = len(num5) - 1


def num_generate():
  select1 = random.choice(num1)
  select2 = random.choice(num2)
  select3 = random.choice(num3)
  select4 = random.choice(num4)
  select5 = random.choice(num5)
  powerSelect = random.choice(power)

  return (
    f"{select1}, {select2}, {select3}, {select4}, {select5}, [{powerSelect}]")
