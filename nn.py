from torch import nn

model = nn.Sequential(
    nn.Linear(in_features=758, out_features=128),
    nn.ReLU(),
    nn.Linear(in_features=128, out_features=64),
    nn.Sigmoid(),
    nn.Linear(in_features=64, out_features=9),

)

