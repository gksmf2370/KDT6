# 모델 관련 모듈 로딩
import torch
import torch.nn as nn
import torch.nn.functional as F

# 다중분류 -------------------------------
class MCFmodel(nn.Module):
    def __init__(self, in_in, out_out, h_list=[]):
        super().__init__()

        self.input_layer = nn.Linear(in_in,h_list[0])      #입력은 피쳐수
        self.h_layers = nn.ModuleList()

        for i in range(len(h_list)-1):
            self.h_layers.append(nn.Linear(h_list[i],h_list[i+1]))
        
        self.out_layers = nn.Linear(h_list[-1], out_out)  # 타겟수
    
    def forward(self, x):
        y = F.relu(self.input_layer(x))  

        for h_layer in self.h_layers:
            y=F.relu(h_layer(y))   
        
        return self.out_layers(y) # 다중분류