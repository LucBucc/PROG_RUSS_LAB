class CSVFile():
  def __init__(self, name):
    self.name=name

  def get_data(self):
    try:
      file= open(self.name, 'r')
      values=[]
      for line in file:
        elements=line.strip('\n').split(',')
        if elements[0]!='Date':
          values.append(elements)
      file.close()
      print (values)
    except Exception as e:
      print('Errore {}'.format(e))

    return values


csv = CSVFile('shampoo_sales.csv')
csv.get_data()
print("Elisabeth dovresti aprirti un centro scommesse così poi lo chiami ELISA BET\n")

print(csv)