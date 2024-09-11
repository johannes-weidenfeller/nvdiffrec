import numpy as np
data = np.load('data/tets/32_tets.npz')
print(data['vertices'].shape)
print(data['vertices'][2,:]-data['vertices'][3,:])
print(data['vertices'])
print(data['vertices'].max())
print(data['vertices'].min())
print(data['indices'].shape)
print(data['indices'])