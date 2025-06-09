import platform
import subprocess

def check_gpu_info():
    print(f"운영체제: {platform.system()} {platform.release()}")

    try:
        # nvidia-smi 실행
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        if result.returncode == 0:
            print("NVIDIA GPU 감지됨")
            print("GPU 정보:")
            print(result.stdout)
        else:
            print("NVIDIA GPU가 없거나 드라이버 문제")
    except FileNotFoundError:
        print("NVIDIA 드라이버가 설치되지 않음")

check_gpu_info()

import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device_cpu = torch.device('cpu')

print(device)
print(device_cpu)