from scipy.io import loadmat, savemat
annots = loadmat('../data/color150.mat')
annots['colors'] = annots['colors'][2:4]
print(annots['colors'])
savemat("../data/color2.mat", annots)
