"""
8. Using convolutions to generalize
"""

from torch import nn
import torchvision

# dataset
trainset = torchvision.datasets.CIFAR10(
    root='../../data', train=True, download=True)

print(trainset.meta)

# ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
# {'airplane': 0, 'automobile': 1, 'bird': 2, 'cat': 3, 'deer': 4, 'dog': 5, 'frog': 6, 'horse': 7, 'ship': 8, 'truck': 9}
print(trainset.classes)
print(trainset.class_to_idx)

img, label = trainset[1]
print(img.size, label)  # (32, 32), 9


class Net(nn.Module):
  """
  Net

  Input: (3, 32x32)
  Output: (2)
  """

  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)  # (16, 32, 32)
    self.act1 = nn.Tanh()
    self.pool1 = nn.MaxPool2d(2)

    self.conv2 = nn.Conv2d(16, 8, kernel_size=3, padding=1)
    self.act2 = nn.Tanh()
    self.pool2 = nn.MaxPool2d(2)

    self.fc1 = nn.Linear(8*8*8, 32)
    self.act3 = nn.Tanh()
    self.fc2 = nn.Linear(32, 2)

  def forward(self, x):
    """forward"""
    out = self.pool1(self.act1(self.conv1(x)))
    out = self.pool2(self.act2(self.conv2(out)))
    out = out.view(-1, 8*8*8)
    out = self.act3(self.fc1(out))
    out = self.fc2(out)
    return out


model = Net()
print(model)
