import numpy as np
import matplotlib.pyplot as plt

#creating a 120X120 gradient image
#np.linspace is used to create evenly spaced arrays
grad = np.linspace(0,1,120)

# np.outer does the outer vector product of m,n
# create a matrix of size mxn 
grad_img = np.outer(grad,grad)

#create QR like image
qr_img = np.random.randint(0,2,size=(120,120))

#subplots returns tuple of figure object and array of axes
fig, ax=  plt.subplots(1,4,figsize=(7,7))

# change cmap for different color gradients
ax[0].imshow(grad_img,cmap='gray')
ax[0].set_title('120x120 gradient image',fontsize=8)

ax[1].imshow(grad_img,cmap='Reds')
ax[1].set_title('120x120 gradient image',fontsize=8)

# change cmap for diffenent color qr's
ax[2].imshow(qr_img,cmap='binary')
ax[2].set_title('120x120 QR code image',fontsize=8)

ax[3].imshow(qr_img,cmap='Purples')
ax[3].set_title('120x120 QR code image',fontsize=8)


plt.tight_layout()
plt.show()
