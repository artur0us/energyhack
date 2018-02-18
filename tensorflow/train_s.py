import tensor

tensor.initialize('solar')

tensor.restore()

tensor.train(0.0005, 50000, 1000)