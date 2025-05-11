const menuItems = document.querySelectorAll('.top_nav ul li');
const menuBars = document.querySelectorAll('.menu_bar');
const header = document.querySelector('.header');

// 현재 활성화된 메뉴 바 인덱스를 추적
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