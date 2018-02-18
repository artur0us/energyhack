import tensor

tensor.initialize('wind')

#tensor.restore()

tensor.train(0.00001, 50000, 1000)
