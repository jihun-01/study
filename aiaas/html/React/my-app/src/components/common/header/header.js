import React, { useState, useEffect } from "react";


function Header() {

    const [activeMenuIndex, setActiveMenuIndex] = useState(-1);
    const [showTimer, setShowTimer] = useState(null);
    const [hideTimer, setHideTimer] = useState(null);

    useEffect(() => {
        const menuItems = document.querySelectorAll('.top_nav ul li');
        const menuBars = document.querySelectorAll('.menu_bar');
        const header = document.querySelector('.header');

        // 초기에 모든 메뉴 바 숨기기
        menuBars.forEach(menuBar => {
            menuBar.style.display = 'none';
            menuBar.classList.remove('active');
        });

        // 메뉴 항목에 마우스 올릴 때 이벤트
            menuItems.forEach((item, index) => {
                item.addEventListener('mouseenter', () => {
                // 숨김 타이머가 있다면 취소

                
                // 표시 타이머 설정
                if (showTimer) {
                    clearTimeout(showTimer);
                }
                
                const newShowTimer = setTimeout(() => {
                    // 이미 활성화된 메뉴가 있고, 인덱스가 다르다면
                    if (activeMenuIndex !== -1 && activeMenuIndex !== index && activeMenuIndex < menuBars.length) {
                        // 활성화된 메뉴를 비활성화
                        menuBars[activeMenuIndex].classList.remove('active');
                        
                        // 약간의 딜레이 후에 display 속성 변경
                        setTimeout(() => {
                            if (activeMenuIndex !== index) { // 중간에 바뀌었는지 확인
                                menuBars[activeMenuIndex].style.display = 'none';
                            }
                        }, 5);
                    }
                    
                    // 새 메뉴 표시
                    if (index < menuBars.length) {
                        menuBars[index].style.display = 'flex';
                        
                        setTimeout(() => {
                            menuBars[index].classList.add('active');
                        }, 5);
                        
                        setActiveMenuIndex(index);
                    }
                }, 50);

                setShowTimer(newShowTimer);
            });
        });

        // 헤더 영역에서 마우스가 떠날 때
        header.addEventListener('mouseleave', () => {
            if (showTimer) {
                clearTimeout(showTimer);
                setShowTimer(null);
            }

            const newHideTimer = setTimeout(() => {
                if (activeMenuIndex !== -1 && activeMenuIndex < menuBars.length) {
                    menuBars[activeMenuIndex].classList.remove('active');
                    
                    // 애니메이션 끝난 후 숨기기
                    setTimeout(() => {
                        if (!menuBars[activeMenuIndex].classList.contains('active')) {
                            menuBars[activeMenuIndex].style.display = 'none';
                        }
                    }, 300);
                    
                    setActiveMenuIndex(-1);
                }
            }, 200);

            setHideTimer(newHideTimer);
        });

        // 각 메뉴 바에 마우스 진입 시 숨김 방지
        menuBars.forEach((menuBar, index) => {
            menuBar.addEventListener('mouseenter', () => {
                if (hideTimer) {
                    clearTimeout(hideTimer);
                    setHideTimer(null);
                }
                
                menuBar.style.display = 'flex';
                menuBar.classList.add('active');
                setActiveMenuIndex(index);
            });
            
            // 메뉴 바에서 마우스 떠날 때
            menuBar.addEventListener('mouseleave', () => {
                const newHideTimer = setTimeout(() => {
                    menuBar.classList.remove('active');
                    
                    setTimeout(() => {
                        if (!menuBar.classList.contains('active')) {
                            menuBar.style.display = 'none';
                            setActiveMenuIndex(-1);
                        }
                    }, 200);
                }, 100);

                setHideTimer(newHideTimer);
            });
        });

        return () => {
            // 이벤트 리스너 정리
            menuItems.forEach(item => {
                item.removeEventListener('mouseenter', () => {});
            });
            header.removeEventListener('mouseleave', () => {});
            menuBars.forEach(menuBar => {
                menuBar.removeEventListener('mouseenter', () => {});
                menuBar.removeEventListener('mouseleave', () => {});
            });
        };
    }, [activeMenuIndex, showTimer, hideTimer]);


    return (
        <>
            <header className="header">
                <nav className="top_nav">
                    <ul>
                        <a href="/"><svg  height="44" viewBox="0 0 15 44" width="13" xmlns="http://www.w3.org/2000/svg"><path d="m15.5752 19.0792a4.2055 4.2055 0 0 0 -2.01 3.5376 4.0931 4.0931 0 0 0 2.4908 3.7542 9.7779 9.7779 0 0 1 -1.2755 2.6351c-.7941 1.1431-1.6244 2.2862-2.8878 2.2862s-1.5883-.734-3.0443-.734c-1.42 0-1.9252.7581-3.08.7581s-1.9611-1.0589-2.8876-2.3584a11.3987 11.3987 0 0 1 -1.9373-6.1487c0-3.61 2.3464-5.523 4.6566-5.523 1.2274 0 2.25.8062 3.02.8062.734 0 1.8771-.8543 3.2729-.8543a4.3778 4.3778 0 0 1 3.6822 1.841zm-6.8586-2.0456a1.3865 1.3865 0 0 1 -.2527-.024 1.6557 1.6557 0 0 1 -.0361-.337 4.0341 4.0341 0 0 1 1.0228-2.5148 4.1571 4.1571 0 0 1 2.7314-1.4078 1.7815 1.7815 0 0 1 .0361.373 4.1487 4.1487 0 0 1 -.9867 2.587 3.6039 3.6039 0 0 1 -2.5148 1.3236z"></path></svg></a>
                        <li><a href="/store">스토어</a></li>
                        <li><a href="#">Mac</a></li>
                        <li><a href="#">Ipad</a></li>
                        <li><a href="#">Iphone</a></li>
                        <li><a href="#">Watch</a></li>
                        <li><a href="#">Vision</a></li>
                        <li><a href="#">AirPods</a></li>
                        <li><a href="#">TV 및 홈</a></li>
                        <li><a href="#">엔터테인먼트</a></li>
                        <li><a href="#">액세서리</a></li>
                        <li><a href="#">고객지원</a></li>
                        <li><a href="#">
                            <svg xmlns="http://www.w3.org/2000/svg" width="15px" height="44px" viewBox="0 0 15 44">
                            <path d="M14.298,27.202l-3.87-3.87c0.701-0.929,1.122-2.081,1.122-3.332c0-3.06-2.489-5.55-5.55-5.55c-3.06,0-5.55,2.49-5.55,5.55 c0,3.061,2.49,5.55,5.55,5.55c1.251,0,2.403-0.421,3.332-1.122l3.87,3.87c0.151,0.151,0.35,0.228,0.548,0.228 s0.396-0.076,0.548-0.228C14.601,27.995,14.601,27.505,14.298,27.202z M1.55,20c0-2.454,1.997-4.45,4.45-4.45 c2.454,0,4.45,1.997,4.45,4.45S8.454,24.45,6,24.45C3.546,24.45,1.55,22.454,1.55,20z"></path>
                            </svg></a></li>
                        <li><a href="#">
                            <svg height="44" viewBox="0 0 14 44" width="14" xmlns="http://www.w3.org/2000/svg"><path d="m11.3535 16.0283h-1.0205a3.4229 3.4229 0 0 0 -3.333-2.9648 3.4229 3.4229 0 0 0 -3.333 2.9648h-1.02a2.1184 2.1184 0 0 0 -2.117 2.1162v7.7155a2.1186 2.1186 0 0 0 2.1162 2.1167h8.707a2.1186 2.1186 0 0 0 2.1168-2.1167v-7.7155a2.1184 2.1184 0 0 0 -2.1165-2.1162zm-4.3535-1.8652a2.3169 2.3169 0 0 1 2.2222 1.8652h-4.4444a2.3169 2.3169 0 0 1 2.2222-1.8652zm5.37 11.6969a1.0182 1.0182 0 0 1 -1.0166 1.0171h-8.7069a1.0182 1.0182 0 0 1 -1.0165-1.0171v-7.7155a1.0178 1.0178 0 0 1 1.0166-1.0166h8.707a1.0178 1.0178 0 0 1 1.0164 1.0166z"></path></svg></a></li>
                    </ul>
                </nav>
                
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">쇼핑하기</h4>
                                <li className="menu_category_li"><a href="/store"><h2>최신 제품 쇼핑하기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Mac</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPad</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPhone</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Vision Pro</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>액세서리</h2></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">빠른 링크</h4>
                                <li className="menu_category_sub_li"><a href="#">매장 찾기</a></li>
                                <li className="menu_category_sub_li"><a href="#">주문 상태</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Trade In</a></li>
                                <li className="menu_category_sub_li"><a href="#">할부 방식</a></li>
                                <li className="menu_category_sub_li"><a href="#">개인 맞춤 설정</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">특별 할인 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">인증 리퍼비쉬 제품</a></li>
                                <li className="menu_category_sub_li"><a href="#">교육</a></li>
                                <li className="menu_category_sub_li"><a href="#">비즈니스</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">Mac 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>Mac 모두 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>MacBook Air</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>MacBook Pro</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iMac</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Mac mini</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Mac Studio</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Mac Pro</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>디스플레이</h2></a></li>
                                <li className="menu_category_li"><a href="#"><p>Mac 비교하기</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>Pc 에서 Mac으로 갈아타기</p></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">Mac 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">Mac 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">Mac 액세서리</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Trade In</a></li>
                                <li className="menu_category_sub_li"><a href="#">할부 방식</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">그 외 Mac 관련 항목</h4>
                                <li className="menu_category_sub_li"><a href="#">Mac 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">Mac을 위한 AppleCare+</a></li>
                                <li className="menu_category_sub_li"><a href="#">macOS Sequoia</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Intelligence</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple이 만든 앱</a></li>
                                <li className="menu_category_sub_li"><a href="#">연속성</a></li>
                                <li className="menu_category_sub_li"><a href="#">iCloud+</a></li>
                                <li className="menu_category_sub_li"><a href="#">Mac과 비즈니스</a></li>
                                <li className="menu_category_sub_li"><a href="#">교육</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">iPad 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>iPad 모두 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPad Pro</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPad Air</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPad</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPad mini</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Pencil</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>키보드</h2></a></li>
                                <li className="menu_category_li"><a href="#"><p>iPad 비교하기</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>iPad를 선택하는 이유</p></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">iPad 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">iPad 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">iPad 액세서리</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Trade In</a></li>
                                <li className="menu_category_sub_li"><a href="#">할부 방식</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">그 외 iPad 관련 항목</h4>
                                <li className="menu_category_sub_li"><a href="#">iPad 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">ipad를 위한 AppleCare+</a></li>
                                <li className="menu_category_sub_li"><a href="#">iPadOS 18</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Intelligence</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple이 만든 앱</a></li>
                                <li className="menu_category_sub_li"><a href="#">iCloud+</a></li>
                                <li className="menu_category_sub_li"><a href="#">교육</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">iPhone 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>iPhone 모두 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPhone 16 Pro</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPhone 16</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPhone 16e</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPhone 15</h2></a></li>
                                <li className="menu_category_li"><a href="#"><p>iPhone 비교하기</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>안드로이드에서 갈아타기</p></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">iPhone 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">iPhone 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">iPhone 액세서리</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Trade In</a></li>
                                <li className="menu_category_sub_li"><a href="#">할부 방식</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">그 외 iPhone 관련 항목</h4>
                                <li className="menu_category_sub_li"><a href="#">iPhone 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">iPhone을 위한 AppleCare+</a></li>
                                <li className="menu_category_sub_li"><a href="#">iOS 18</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Intelligence</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple이 만든 앱</a></li>
                                <li className="menu_category_sub_li"><a href="#">Iphone의 개인정보 보호</a></li>
                                <li className="menu_category_sub_li"><a href="#">iCloud+</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple 지갑, Apple Pay</a></li>
                                <li className="menu_category_sub_li"><a href="#">Siri</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">Watch 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch 모두 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch Series 10</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch Ultra 2</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch SE</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch Nike</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch Hermès</h2></a></li>
                                <li className="menu_category_li"><a href="#"><p> Watch 비교하기</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>Apple Watch를 선택하는 이유</p></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">watch 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple watch 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple watch Studio</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple watch 밴드</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple watch 액세서리</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Trade In</a></li>
                                <li className="menu_category_sub_li"><a href="#">할부 방식</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">그 외 Watch 관련 항목</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple Watch 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">AppleCare+</a></li>
                                <li className="menu_category_sub_li"><a href="#">WatchOS 11</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple이 만든 앱</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">Vision 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>Apple Vision Pro 모두 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><p>가이드 동영상</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>제품 사양</p></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">Vision 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple Vision Pro 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Vision Pro 액세서리</a></li>
                                <li className="menu_category_sub_li"><a href="#">체험 예약하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">할부 방식</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">그 외 Vision 관련 항목</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple Vision Pro 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">AppleCare+</a></li>
                                <li className="menu_category_sub_li"><a href="#">VisionOS 2</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">AirPods 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>AirPods 모두 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>AirPods 4</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>AirPods Pro2</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>AirPods Max</h2></a></li>
                                <li className="menu_category_li"><a href="#"><p>AirPods 비교하기</p></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">AirPods 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">AirPods 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">AirPods 액세서리</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">그 외 AirPods 관련 항목</h4>
                                <li className="menu_category_sub_li"><a href="#">AirPods 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">헤드폰을 위한 AppleCare+</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Music</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">Tv 및 홈 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>Tv 및 홈 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple TV 4K</h2></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">Tv 및 홈 쇼핑하기</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple TV 4K 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">Siri Remote 쇼핑하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">TV 및 홈 액세서리</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">그 외 Tv 및 홈 관련 항목</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple TV 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">AppleCare+</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple TV 앱</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple TV+</a></li>
                                <li className="menu_category_sub_li"><a href="#">홈 앱</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Music</a></li>
                                <li className="menu_category_sub_li"><a href="#">Siri</a></li>
                                <li className="menu_category_sub_li"><a href="#">AirPlay</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">엔터테인먼트 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>엔터테인먼트 살펴보기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple One</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple TV+</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Music</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Arcade</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple 팟캐스트</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Books</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Store</h2></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">지원</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple TV+ 지원</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple Music 지원</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">액세서리 쇼핑하기</h4>
                                <li className="menu_category_li"><a href="#"><h2>액세서리 모두 쇼핑하기</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Mac</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPad</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPhone</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Watch</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Apple Vision Pro</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>AirPods</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>TV 및 홈</h2></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">액세서리 살펴보기</h4>
                                <li className="menu_category_sub_li"><a href="#">Apple 제작 정품</a></li>
                                <li className="menu_category_sub_li"><a href="#">Beats by Dr. Dre </a></li>
                                <li className="menu_category_sub_li"><a href="#">AirTag</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <h4 className="menu_category_title">지원 상황 살펴보기</h4>
                                <li className="menu_category_li"><a href="#"><h2>iPhone</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Mac</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>iPad</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Watch</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Vision Pro</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>AirPods</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>Music</h2></a></li>
                                <li className="menu_category_li"><a href="#"><h2>TV</h2></a></li>
                                <li className="menu_category_li"><a href="#"><p>지원상황 살펴보기</p></a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">도움 받기</h4>
                                <li className="menu_category_sub_li"><a href="#">커뮤니티</a></li>
                                <li className="menu_category_sub_li"><a href="#">보장 상태 확인하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">수리</a></li>
                            </ul>
                        </div>
                        <div className="menu_category">
                            <ul className="menu_category_sub_ul">
                                <h4 className="menu_category_title">유용한 주제</h4>
                                <li className="menu_category_sub_li"><a href="#">AppleCare+ 구입하기</a></li>
                                <li className="menu_category_sub_li"><a href="#">Apple 계정 및 암호</a></li>
                                <li className="menu_category_sub_li"><a href="#">청구 및 구독</a></li>
                                <li className="menu_category_sub_li"><a href="#">손쉬운 사용</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <span className="menu_category_title_search">
                                    <li className="menu_category_li"> <svg xmlns="http://www.w3.org/2000/svg" width="15px" height="44px" viewBox="0 0 15 36">
                                        <path d="M14.298,27.202l-3.87-3.87c0.701-0.929,1.122-2.081,1.122-3.332c0-3.06-2.489-5.55-5.55-5.55c-3.06,0-5.55,2.49-5.55,5.55 c0,3.061,2.49,5.55,5.55,5.55c1.251,0,2.403-0.421,3.332-1.122l3.87,3.87c0.151,0.151,0.35,0.228,0.548,0.228 s0.396-0.076,0.548-0.228C14.601,27.995,14.601,27.505,14.298,27.202z M1.55,20c0-2.454,1.997-4.45,4.45-4.45 c2.454,0,4.45,1.997,4.45,4.45S8.454,24.45,6,24.45C3.546,24.45,1.55,22.454,1.55,20z"></path></svg>
                                        <span className="menu_category_title_search_input">
                                            <input type="text" placeholder="Apple.com 검색하기" required />
                                        </span>
                                    </li>
                                </span>
                                <li className="menu_category_li"><h4>빠른 링크</h4></li>
                                <li className="menu_category_li"><a href="#"><p>→ Apple Store Online에서 쇼핑하기</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>→ Apple Vision Pro</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>→ AirPods</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>→ Apple Intelligence</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>→ Apple Trade In</p></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="menu_bar">
                    <div className="menu_category_card">
                        <div className="menu_category">
                            <ul className="menu_category_main_ul">
                                <span className="menu_category_title_cart">
                                <li className="menu_category_li"><h2>장바구니가 비어 있습니다.</h2></li>
                                </span>
                                <span className="menu_category_title_cart_text">
                                <li className="menu_category_li"><h4>저장해둔 항목이 있는지 확인하려면 <a href="#">로그인</a>하세요.</h4></li>
                                </span>
                                <span className="menu_category_title_cart_link">
                                <li className="menu_category_li"><h4>빠른 링크</h4></li>
                                <li className="menu_category_li">
                                    <span className="menu_category_title_cart_link_icon">
                                        <svg xmlns="www.w3.org/2000/svg" width="15" height="25" viewBox="0 0 11 16">
                                            <path id="art_" d="M9.4128,4.2466,6.2484,2.4615a1.5,1.5,0,0,0-1.474,0L1.61,4.2466a1.5,1.5,0,0,0-.763,1.3065v3.51A1.5,1.5,0,0,0,1.61,10.37l3.1645,1.7851a1.5,1.5,0,0,0,1.474,0L9.4128,10.37a1.5,1.5,0,0,0,.763-1.3065v-3.51A1.5,1.5,0,0,0,9.4128,4.2466ZM5.2043,3.2237a.6252.6252,0,0,1,.6141,0L8.8787,4.95l-1.18.6736L4.2966,3.7358Zm.3069,3.6491L2.1441,4.95l1.2576-.7094L6.81,6.1314ZM2.04,9.6078a.626.626,0,0,1-.3179-.5443V5.7163L5.0737,7.6308v3.6885Zm6.9431,0L5.9487,11.3194V7.6308L9.3008,5.7165v3.347A.6258.6258,0,0,1,8.9829,9.6078Z" fill="6E6E73"></path>
                                        </svg>
                                    <a href="#"><p>주문</p></a>
                                    </span>
                                </li>
                                </span>
                                <li className="menu_category_li"><a href="#"><p>관심 목록</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>계정</p></a></li>
                                <li className="menu_category_li"><a href="#"><p>로그인</p></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </header>

        </>
    );
}

export default Header;