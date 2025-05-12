const menuItems = document.querySelectorAll('.top_nav ul li');
const menuBars = document.querySelectorAll('.menu_bar');
const header = document.querySelector('.header');
const slideList = document.getElementById('slide_list');
const slides = document.querySelectorAll('.slide');
const slideNav = document.getElementById('slide_nav');
const prevButton = document.querySelector('.slide-preview-prev');
const nextButton = document.querySelector('.slide-preview-next');

// 현재 활성화된 메뉴 바 인덱스를 추적
let currentSlideIndex = 0;
let slideTimer;
const slideInterval = 3000; // 슬라이드 간격 (3초)

let activeMenuIndex = -1;
let showTimer = null;
let hideTimer = null;

// 초기에 모든 메뉴 바 숨기기
menuBars.forEach(menuBar => {
  menuBar.style.display = 'none';
  menuBar.classList.remove('active');
});

// 메뉴 항목에 마우스 올릴 때 이벤트
menuItems.forEach((item, index) => {
  item.addEventListener('mouseenter', () => {
    // 숨김 타이머가 있다면 취소
    if (hideTimer) {
      clearTimeout(hideTimer);
      hideTimer = null;
    }
    
    // 표시 타이머 설정
    if (showTimer) {
      clearTimeout(showTimer);
    }
    
    showTimer = setTimeout(() => {
      // 이미 활성화된 메뉴가 있고, 인덱스가 다르다면
      if (activeMenuIndex !== -1 && activeMenuIndex !== index && activeMenuIndex < menuBars.length) {
        // 활성화된 메뉴를 비활성화
        menuBars[activeMenuIndex].classList.remove('active');
        
        // 약간의 딜레이 후에 display 속성 변경
        setTimeout(() => {
          if (activeMenuIndex !== index) { // 중간에 바뀌었는지 확인
            menuBars[activeMenuIndex].style.display = 'none';
          }
        }, 10);
      }
      
      // 새 메뉴 표시
      if (index < menuBars.length) {
        menuBars[index].style.display = 'flex';
        
        setTimeout(() => {
          menuBars[index].classList.add('active');
        }, 10);
        
        activeMenuIndex = index;
      }
    }, 100);
  });
});

// 헤더 영역에서 마우스가 떠날 때
header.addEventListener('mouseleave', () => {
  if (showTimer) {
    clearTimeout(showTimer);
    showTimer = null;
  }
  
  hideTimer = setTimeout(() => {
    if (activeMenuIndex !== -1 && activeMenuIndex < menuBars.length) {
      menuBars[activeMenuIndex].classList.remove('active');
      
      // 애니메이션 끝난 후 숨기기
      setTimeout(() => {
        if (!menuBars[activeMenuIndex].classList.contains('active')) {
          menuBars[activeMenuIndex].style.display = 'none';
        }
      }, 300);
      
      activeMenuIndex = -1;
    }
  }, 200);
});

// 각 메뉴 바에 마우스 진입 시 숨김 방지
menuBars.forEach((menuBar, index) => {
  menuBar.addEventListener('mouseenter', () => {
    if (hideTimer) {
      clearTimeout(hideTimer);
      hideTimer = null;
    }
    
    menuBar.style.display = 'flex';
    menuBar.classList.add('active');
    activeMenuIndex = index;
  });
  
  // 메뉴 바에서 마우스 떠날 때
  menuBar.addEventListener('mouseleave', () => {
    hideTimer = setTimeout(() => {
      menuBar.classList.remove('active');
      
      setTimeout(() => {
        if (!menuBar.classList.contains('active')) {
          menuBar.style.display = 'none';
          activeMenuIndex = -1;
        }
      }, 300);
    }, 200);
  });
});

// 슬라이드쇼
// 페이지 로드 시 초기화
document.addEventListener('DOMContentLoaded', () => {
  // 첫 번째 슬라이드 활성화
  if (slides.length > 0) {
      slides[0].classList.add('active');
  }
  
  initSlide();
});
// 페이지 로드 초기화
function initSlide() {
  createNavDots();

  //첫번째 슬라이드 활성화
  if (slides.length > 0) {
    slides[0].classList.add('active');
    document.querySelectorAll('.nav-dot')[0].classList.add('active');
}


  // 이벤트 리스너
  prevButton.addEventListener('click', showPrevSlide);
  nextButton.addEventListener('click', showNextSlide);
// 자동 슬라이드 시작
  startAutoSlide();

  document.querySelector('.module_3').addEventListener('mouseenter', stopAutoSlide);
  document.querySelector('.module_3').addEventListener('mouseleave', startAutoSlide);

}

function createNavDots() {
  for (let i = 0; i < slides.length; i++) {
    const dot = document.createElement('div');
    dot.classList.add('nav-dot');
    dot.setAttribute('data-index', i);

    dot.addEventListener('click', () => {
      showSlide(i);
    });

    slideNav.appendChild(dot);
  }
}
// 슬라이드 표시
function showSlide(index) {
  if (index < 0 ) {
    index = slides.length - 1; // 마지막 슬라이드로 이동
  } else if (index >= slides.length) {
    index = 0; // 첫 번째 슬라이드로 이동
  }

  slides[currentSlideIndex].classList.remove('active');
  document.querySelectorAll('.nav-dot')[currentSlideIndex].classList.remove('active');

  currentSlideIndex = index;
  slides[currentSlideIndex].classList.add('active');
  document.querySelectorAll('.nav-dot')[currentSlideIndex].classList.add('active');
}

function showPrevSlide() {
  showSlide(currentSlideIndex - 1);
}

function showNextSlide() {
  showSlide(currentSlideIndex + 1);
}

function startAutoSlide() {
  stopAutoSlide(); // 기존 타이머가 있다면 정지

  slideTimer = setInterval(showNextSlide, slideInterval);
}

// 슬라이드 자동 전환 정지
function stopAutoSlide() {
  if (slideTimer) {
    clearInterval(slideTimer);
    slideTimer = null;
  }
}
document.addEventListener('DOMContentLoaded', initSlide);

