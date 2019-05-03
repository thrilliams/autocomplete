file = open('history.html', 'r')
data = file.read()
file.close()

data = data.split('<body>')[1].split('</body>')[0]
data = data.split