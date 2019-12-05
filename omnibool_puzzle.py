class Omnibool:
    def __eq__(self, other):
        return True


omnibool = Omnibool()
print(omnibool == True)
print(omnibool == False)