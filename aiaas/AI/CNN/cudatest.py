import torch
import time
import numpy as np
import matplotlib.pyplot as plt

def check_cuda_availability():
    """CUDA 사용 가능 여부 확인"""
    print(f"PyTorch 버전: {torch.__version__}")
    print(f"CUDA 사용 가능: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA 버전: {torch.version.cuda}")
        print(f"GPU 개수: {torch.cuda.device_count()}")
        print(f"현재 GPU: {torch.cuda.get_device_name(0)}")
    print("-" * 50)

def format_time(seconds):
    """시간을 읽기 쉬운 형태로 포맷팅"""
    if seconds >= 1:
        return f"{seconds:.3f}초"
    elif seconds >= 0.001:
        return f"{seconds*1000:.1f}ms"
    else:
        return f"{seconds*1000000:.1f}μs"

def format_time_for_plot(times):
    """플롯용 시간 단위 자동 선택 및 변환"""
    max_time = max(times)
    if max_time >= 1:
        return [t for t in times], "초"
    elif max_time >= 0.001:
        return [t * 1000 for t in times], "밀리초"
    else:
        return [t * 1000000 for t in times], "마이크로초"

def benchmark_tensor_operations(size, iterations=100):
    """텐서 연산 벤치마크"""
    print(f"\n📊 행렬 크기: {size:,} × {size:,} (반복: {iterations}회)")
    print("─" * 60)
    
    # CPU 벤치마크
    print("🔄 CPU에서 행렬곱셈 실행 중...")
    a_cpu = torch.randn(size, size)
    b_cpu = torch.randn(size, size)
    
    start_time = time.time()
    for _ in range(iterations):
        c_cpu = torch.mm(a_cpu, b_cpu)
    cpu_time = time.time() - start_time
    
    avg_cpu_time = cpu_time / iterations
    
    # CUDA 벤치마크 (CUDA 사용 가능한 경우)
    if torch.cuda.is_available():
        print("🚀 GPU에서 행렬곱셈 실행 중...")
        device = torch.device('cuda')
        a_gpu = torch.randn(size, size, device=device)
        b_gpu = torch.randn(size, size, device=device)
        
        # GPU warm-up
        for _ in range(10):
            torch.mm(a_gpu, b_gpu)
        torch.cuda.synchronize()
        
        start_time = time.time()
        for _ in range(iterations):
            c_gpu = torch.mm(a_gpu, b_gpu)
        torch.cuda.synchronize()
        gpu_time = time.time() - start_time
        
        avg_gpu_time = gpu_time / iterations
        speedup = cpu_time / gpu_time
        
        # 결과 출력
        print("\n📈 실행 결과:")
        print(f"   💻 CPU 총 시간     : {format_time(cpu_time)}")
        print(f"   💻 CPU 평균 시간   : {format_time(avg_cpu_time)}")
        print(f"   🎮 GPU 총 시간     : {format_time(gpu_time)}")
        print(f"   🎮 GPU 평균 시간   : {format_time(avg_gpu_time)}")
        print(f"   ⚡ 속도 향상       : {speedup:.1f}배 빠름")
        
        return cpu_time, gpu_time
    else:
        print("\n⚠️  CUDA를 사용할 수 없습니다.")
        print(f"   💻 CPU 총 시간     : {format_time(cpu_time)}")
        print(f"   💻 CPU 평균 시간   : {format_time(avg_cpu_time)}")
        return cpu_time, None

def benchmark_neural_network(batch_size=64, input_size=784, hidden_size=512, 
                           output_size=10, iterations=100):
    """신경망 순전파 벤치마크"""
    print(f"\n신경망 벤치마크 (배치 크기: {batch_size})")
    
    # 간단한 MLP 모델 정의
    class SimpleMLP(torch.nn.Module):
        def __init__(self, input_size, hidden_size, output_size):
            super(SimpleMLP, self).__init__()
            self.fc1 = torch.nn.Linear(input_size, hidden_size)
            self.fc2 = torch.nn.Linear(hidden_size, hidden_size)
            self.fc3 = torch.nn.Linear(hidden_size, output_size)
            self.relu = torch.nn.ReLU()
        
        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.fc3(x)
            return x
    
    # CPU 벤치마크
    model_cpu = SimpleMLP(input_size, hidden_size, output_size)
    data_cpu = torch.randn(batch_size, input_size)
    
    start_time = time.time()
    for _ in range(iterations):
        output_cpu = model_cpu(data_cpu)
    cpu_time = time.time() - start_time
    
    print(f"CPU 신경망 순전파 시간: {format_time(cpu_time)}")
    
    # CUDA 벤치마크
    if torch.cuda.is_available():
        model_gpu = SimpleMLP(input_size, hidden_size, output_size).cuda()
        data_gpu = torch.randn(batch_size, input_size, device='cuda')
        
        # GPU warm-up
        for _ in range(10):
            model_gpu(data_gpu)
        torch.cuda.synchronize()
        
        start_time = time.time()
        for _ in range(iterations):
            output_gpu = model_gpu(data_gpu)
        torch.cuda.synchronize()
        gpu_time = time.time() - start_time
        
        print(f"GPU 신경망 순전파 시간: {format_time(gpu_time)}")
        print(f"속도 향상: {cpu_time/gpu_time:.1f}배")
        
        return cpu_time, gpu_time
    else:
        return cpu_time, None

def comprehensive_benchmark():
    """종합적인 벤치마크 실행"""
    check_cuda_availability()
    
    # 다양한 크기의 텐서로 벤치마크 (크기 증가)
    sizes = [256, 512, 768, 1024, 1536, 2048, 3072, 4096, 5120, 6144, 7168, 8192]
    cpu_times = []
    gpu_times = []
    
    print("=" * 80)
    print("🔥 행렬 곱셈 성능 벤치마크")
    print("=" * 80)
    
    for size in sizes:
        cpu_time, gpu_time = benchmark_tensor_operations(size, iterations=30)
        cpu_times.append(cpu_time)
        if gpu_time is not None:
            gpu_times.append(gpu_time)
    
    # 신경망 벤치마크
    print("\n" + "=" * 60)
    print("신경망 벤치마크")
    print("=" * 60)
    
    batch_sizes = [16, 32, 48, 64, 96, 128, 192, 256, 384, 512]
    nn_cpu_times = []
    nn_gpu_times = []
    
    for batch_size in batch_sizes:
        print(f"\n배치 크기 {batch_size} 테스트:")
        cpu_time, gpu_time = benchmark_neural_network(batch_size=batch_size, iterations=50)
        nn_cpu_times.append(cpu_time)
        if gpu_time is not None:
            nn_gpu_times.append(gpu_time)
    
    # 결과 시각화
    if torch.cuda.is_available() and gpu_times:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        plt.rc('font', family='Malgun Gothic')
        
        # 행렬 곱셈 결과 - 절대 시간
        cpu_plot_times, cpu_time_unit = format_time_for_plot(cpu_times)
        gpu_plot_times, gpu_time_unit = format_time_for_plot(gpu_times)
        
        ax1.semilogy(sizes, cpu_plot_times, 'b-o', label=f'CPU ({cpu_time_unit})', linewidth=2, markersize=6)
        ax1.semilogy(sizes, gpu_plot_times, 'r-o', label=f'GPU ({gpu_time_unit})', linewidth=2, markersize=6)
        ax1.set_xlabel('행렬 크기', fontsize=12)
        ax1.set_ylabel(f'실행 시간 ({cpu_time_unit})', fontsize=12)
        ax1.set_title('행렬 곱셈 절대 실행시간 비교', fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3)
        ax1.set_xticks(sizes[::2])  # 일부 x축 라벨만 표시
        
        # 행렬 곱셈 속도 향상 비율
        speedups = [cpu/gpu for cpu, gpu in zip(cpu_times, gpu_times)]
        ax2.plot(sizes, speedups, 'g-o', linewidth=3, markersize=7, color='darkgreen')
        ax2.set_xlabel('행렬 크기', fontsize=12)
        ax2.set_ylabel('속도 향상 (배)', fontsize=12)
        ax2.set_title('행렬 곱셈 GPU 속도 향상', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.set_xticks(sizes[::2])
        # 속도 향상 값을 각 점에 표시
        for i, (x, y) in enumerate(zip(sizes, speedups)):
            if i % 2 == 0:  # 일부만 표시
                ax2.annotate(f'{y:.1f}x', (x, y), textcoords="offset points", 
                           xytext=(0,10), ha='center', fontsize=9, fontweight='bold')
        
        # 신경망 결과 - 절대 시간
        nn_cpu_plot_times, nn_cpu_time_unit = format_time_for_plot(nn_cpu_times)
        nn_gpu_plot_times, nn_gpu_time_unit = format_time_for_plot(nn_gpu_times)
        
        ax3.plot(batch_sizes, nn_cpu_plot_times, 'b-o', label=f'CPU ({nn_cpu_time_unit})', linewidth=2, markersize=6)
        ax3.plot(batch_sizes, nn_gpu_plot_times, 'r-o', label=f'GPU ({nn_gpu_time_unit})', linewidth=2, markersize=6)
        ax3.set_xlabel('배치 크기', fontsize=12)
        ax3.set_ylabel(f'실행 시간 ({nn_cpu_time_unit})', fontsize=12)
        ax3.set_title('신경망 순전파 절대 실행시간 비교', fontsize=14, fontweight='bold')
        ax3.legend(fontsize=11)
        ax3.grid(True, alpha=0.3)
        ax3.set_xticks(batch_sizes[::2])
        
        # 신경망 속도 향상 비율
        nn_speedups = [cpu/gpu for cpu, gpu in zip(nn_cpu_times, nn_gpu_times)]
        ax4.plot(batch_sizes, nn_speedups, 'g-o', linewidth=3, markersize=7, color='purple')
        ax4.set_xlabel('배치 크기', fontsize=12)
        ax4.set_ylabel('속도 향상 (배)', fontsize=12)
        ax4.set_title('신경망 GPU 속도 향상', fontsize=14, fontweight='bold')
        ax4.grid(True, alpha=0.3)
        ax4.set_xticks(batch_sizes[::2])
        # 속도 향상 값을 각 점에 표시
        for i, (x, y) in enumerate(zip(batch_sizes, nn_speedups)):
            if i % 2 == 0:  # 일부만 표시
                ax4.annotate(f'{y:.1f}x', (x, y), textcoords="offset points", 
                           xytext=(0,10), ha='center', fontsize=9, fontweight='bold')
        
        plt.tight_layout(pad=3.0)
        plt.show()
        
        # 속도 향상 요약
        print("\n" + "=" * 80)
        print("📋 성능 요약 보고서")
        print("=" * 80)
        speedups = [cpu/gpu for cpu, gpu in zip(cpu_times, gpu_times)]
        nn_speedups = [cpu/gpu for cpu, gpu in zip(nn_cpu_times, nn_gpu_times)]
        
        print("\n🔢 행렬 곱셈 성능:")
        print("   크기        CPU 시간      GPU 시간      속도향상")
        print("   " + "─" * 50)
        for size, cpu_t, gpu_t, speedup in zip(sizes, cpu_times, gpu_times, speedups):
            print(f"   {size:,}×{size:,}    {format_time(cpu_t):>10}    {format_time(gpu_t):>10}    {speedup:>6.1f}배")
        
        print(f"\n📊 평균 속도 향상: {np.mean(speedups):.1f}배")
        
        print("\n🧠 신경망 성능:")
        print("   배치크기    CPU 시간      GPU 시간      속도향상")
        print("   " + "─" * 50)
        for batch_size, cpu_t, gpu_t, speedup in zip(batch_sizes, nn_cpu_times, nn_gpu_times, nn_speedups):
            print(f"   {batch_size:>8}    {format_time(cpu_t):>10}    {format_time(gpu_t):>10}    {speedup:>6.1f}배")
        
        print(f"\n📈 평균 속도 향상: {np.mean(nn_speedups):.1f}배")

def memory_usage_comparison():
    """메모리 사용량 비교"""
    if not torch.cuda.is_available():
        print("CUDA를 사용할 수 없어 메모리 비교를 건너뜁니다.")
        return
    
    print("\n" + "=" * 60)
    print("메모리 사용량 비교")
    print("=" * 60)
    
    sizes = [1000, 2000, 4000, 8000]
    
    for size in sizes:
        # GPU 메모리 초기화
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        
        # GPU에서 텐서 생성
        tensor_gpu = torch.randn(size, size, device='cuda')
        
        # 메모리 사용량 측정
        memory_allocated = torch.cuda.memory_allocated() / 1024**2  # MB
        memory_reserved = torch.cuda.memory_reserved() / 1024**2   # MB
        
        print(f"크기 {size}x{size}:")
        print(f"  할당된 메모리: {memory_allocated:.2f} MB")
        print(f"  예약된 메모리: {memory_reserved:.2f} MB")
        
        del tensor_gpu
        torch.cuda.empty_cache()

if __name__ == "__main__":
    # 전체 벤치마크 실행
    comprehensive_benchmark()
    
    # 메모리 사용량 비교
    memory_usage_comparison()
    
    print("\n🎉 벤치마크 완료!")
    print("💡 팁: GPU 성능은 행렬 크기가 클수록 더 큰 향상을 보입니다.")