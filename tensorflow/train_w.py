import tensor

tensor.initialize(5, 10, 1, 'wind')

#tensor.restore()

tensor.train(0.015, 1000000, 10000)
