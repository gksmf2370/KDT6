# ---------------------------------------------------------------------------
# 함수명   : plot_loss_score
# 기능     : 학습 후 loss와 score의 변화를 시각화하는 함수
# ---------------------------------------------------------------------------
# 입력값 :
#   - LOSS_HISTORY : [train_loss, val_loss] 형태의 리스트
#   - SCORE_HISTORY :  [train_score, val_score] 형태의 리스트
#   - THRESHOLD : 시각화할 epoch의 수 (기본값:데이터의 길이)
# ---------------------------------------------------------------------------
# 출력값 : 
#   - None (그래프를 출력)
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
def plot_loss_score(LOSS_HISTORY, SCORE_HISTORY, title, THRESHOLD = None):

    if THRESHOLD is None:
        THRESHOLD=len(LOSS_HISTORY[1])
    

    fg, axes=plt.subplots(1,2,figsize=(10,5))
    axes[0].plot(range(1, THRESHOLD+1), LOSS_HISTORY[0][:THRESHOLD], label='Train')
    axes[0].plot(range(1, THRESHOLD+1), LOSS_HISTORY[1][:THRESHOLD], label='Val')
    axes[0].grid()
    axes[0].legend()
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('Epoch&Loss')

    axes[1].plot(range(1, THRESHOLD+1), SCORE_HISTORY[0][:THRESHOLD], label='Train')
    axes[1].plot(range(1, THRESHOLD+1), SCORE_HISTORY[1][:THRESHOLD], label='Val')
    axes[1].grid()
    axes[1].legend()
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel(title)
    axes[1].set_title(f'Epoch&{title}')
    plt.tight_layout()
    plt.show()




# ---------------------------------------------------------------------------
# 함수명   : predict_data
# 기능     : 데이터를 가지고 모델에서 예측을 하는 함수
# ---------------------------------------------------------------------------
# 입력값 :
#   - model :  학습된 모델
#   - data : [feature1, feature2...] 형태의 리스트
#   - multi : bool , 다중분류면 True (기본값 False)
# ---------------------------------------------------------------------------
# 출력값 : 
#   - pre_val : 예측결과값 출력
#   - idx : 다중분류의 가장큰 인덱스값 출력
# ---------------------------------------------------------------------------
import torch
def predict_data(model, data, multi=False):
    dataTS = torch.FloatTensor(data).reshape(1,-1)
    dataTS.shape, dataTS

    # 새로운 데이터에 대한 예측 즉, predict
    model.eval()
    with torch.no_grad():

        # 추론/평가
        pre_val=model(dataTS)
        if multi :
            idx = torch.argmax(pre_val, dim=1).item()
            return pre_val, idx
        else:
            return pre_val