import tensor

tensor.initialize('solar')

#tensor.restore()

tensor.train(0.002, 50000, 1000)