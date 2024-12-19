import torch
import torch.nn as nn
from torchvision.models import resnet50, ResNet50_Weights

class CombinedModel(nn.Module):
    def __init__(self, sensor_input_dim, cnn_output_dim=2048, hidden_dim=512, num_classes=5):

        super(CombinedModel, self).__init__()

        # ResNet50 (사전 학습된 모델 사용)
        self.cnn = resnet50(weights=ResNet50_Weights.DEFAULT)
        self.cnn.fc = nn.Identity()  # Fully connected layer 제거 (특징 추출만 수행)
        for param in self.cnn.parameters():
            param.requires_grad = False

        # DNN for sensor data
        self.sensor_fc = nn.Sequential(
            nn.Linear(sensor_input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )

        # 최종 결합층
        self.fc = nn.Sequential(
            nn.Linear(cnn_output_dim + hidden_dim // 2, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, num_classes)  # 출력 클래스 개수
        )

    def forward(self, image_data, sensor_data):
        # 이미지 데이터 처리
        cnn_features = self.cnn(image_data)

        # 센싱 데이터 처리
        sensor_features = self.sensor_fc(sensor_data)

        # CNN과 DNN 출력 결합
        combined_features = torch.cat((cnn_features, sensor_features), dim=1)

        # 최종 출력층
        output = self.fc(combined_features)
        return output
