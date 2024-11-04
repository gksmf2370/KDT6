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

    plot_loss_score(LOSS_HISTORY, ACCURACY_HISTORY, 'accuracy')