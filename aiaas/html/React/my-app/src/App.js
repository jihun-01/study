import React from 'react';
import './App.css';

function App() {
  const handleShopClick = (e) => {
    e.stopPropagation();
    window.location.href = 'shop.html';
  };

  return (
    <>
    <header className="header">
        <nav className="top_nav">

            <ul>
                <a href="#"><svg height="48" viewBox="0 0 17 36" width="17" xmlns="http://www.w3.org/2000/svg"><path d="m15.5752 19.0792a4.2055 4.2055 0 0 0 -2.01 3.5376 4.0931 4.0931 0 0 0 2.4908 3.7542 9.7779 9.7779 0 0 1 -1.2755 2.6351c-.7941 1.1431-1.6244 2.2862-2.8878 2.2862s-1.5883-.734-3.0443-.734c-1.42 0-1.9252.7581-3.08.7581s-1.9611-1.0589-2.8876-2.3584a11.3987 11.3987 0 0 1 -1.9373-6.1487c0-3.61 2.3464-5.523 4.6566-5.523 1.2274 0 2.25.8062 3.02.8062.734 0 1.8771-.8543 3.2729-.8543a4.3778 4.3778 0 0 1 3.6822 1.841zm-6.8586-2.0456a1.3865 1.3865 0 0 1 -.2527-.024 1.6557 1.6557 0 0 1 -.0361-.337 4.0341 4.0341 0 0 1 1.0228-2.5148 4.1571 4.1571 0 0 1 2.7314-1.4078 1.7815 1.7815 0 0 1 .0361.373 4.1487 4.1487 0 0 1 -.9867 2.587 3.6039 3.6039 0 0 1 -2.5148 1.3236z"></path></svg></a>
                <li><a href="#">스토어</a></li>
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
                    <svg xmlns="http://www.w3.org/2000/svg" width="15px" height="44px" viewBox="0 0 15 36">
                    <path d="M14.298,27.202l-3.87-3.87c0.701-0.929,1.122-2.081,1.122-3.332c0-3.06-2.489-5.55-5.55-5.55c-3.06,0-5.55,2.49-5.55,5.55 c0,3.061,2.49,5.55,5.55,5.55c1.251,0,2.403-0.421,3.332-1.122l3.87,3.87c0.151,0.151,0.35,0.228,0.548,0.228 s0.396-0.076,0.548-0.228C14.601,27.995,14.601,27.505,14.298,27.202z M1.55,20c0-2.454,1.997-4.45,4.45-4.45 c2.454,0,4.45,1.997,4.45,4.45S8.454,24.45,6,24.45C3.546,24.45,1.55,22.454,1.55,20z"></path>
                    </svg></a></li>
                <li><a href="#">
                    <svg height="44" viewBox="0 0 14 36" width="14" xmlns="http://www.w3.org/2000/svg"><path d="m11.3535 16.0283h-1.0205a3.4229 3.4229 0 0 0 -3.333-2.9648 3.4229 3.4229 0 0 0 -3.333 2.9648h-1.02a2.1184 2.1184 0 0 0 -2.117 2.1162v7.7155a2.1186 2.1186 0 0 0 2.1162 2.1167h8.707a2.1186 2.1186 0 0 0 2.1168-2.1167v-7.7155a2.1184 2.1184 0 0 0 -2.1165-2.1162zm-4.3535-1.8652a2.3169 2.3169 0 0 1 2.2222 1.8652h-4.4444a2.3169 2.3169 0 0 1 2.2222-1.8652zm5.37 11.6969a1.0182 1.0182 0 0 1 -1.0166 1.0171h-8.7069a1.0182 1.0182 0 0 1 -1.0165-1.0171v-7.7155a1.0178 1.0178 0 0 1 1.0166-1.0166h8.707a1.0178 1.0178 0 0 1 1.0164 1.0166z"></path></svg></a></li>
            </ul>
        </nav>
        
        <div className="menu_bar">
            <div className="menu_category_title">
                <div className="menu_category">
                    <ul className="menu_category_main_ul">
                        <h4 className="menu_category_title">쇼핑하기</h4>
                        <li className="menu_category_li"><a href="#"><h2>최신 제품 쇼핑하기</h2></a></li>
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
            <div className="menu_category_title">
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
    <main className="main">
        <section className="module_1_link">
        <a href="#" className="module_1_link_area">
            <div className="module_1">
                <div className="link">
                    <div>
                        <h2 className="module_1_title">iPhone</h2>
                        <p className="module_1_text">iPhone 16 라인업을 만나볼까요?</p>
                        <div className="button">
                            <button className="button_blue">더 알아보기</button>
                            <button className="button_white" onClick={handleShopClick}>쇼핑하기</button>
                        </div>
                        <p className="AI_text">Apple Intelligence를 위한 탄생.</p>
                        <p className="AI_text_describe">Apple Intelligence, 현재 한국어로 서비스 중</p>
                    </div>
                </div>
            </div>
        </a>
        <a href="#" className="module_1_link_area">
            <div className="module_1_1">
                <div className="link">
                    <div>
                        <div className="module_1_1_title"></div>
                        <p className="module_1_text">얇아진 두께. 더 커진 존재감.</p>
                        <div className="button">
                            <button className="button_blue">더 알아보기</button>
                            <button className="button_white" onClick={handleShopClick}>구매하기</button>
                        </div>
                    </div>
                </div>
            </div>
        </a>
        <a href="#" className="module_1_link_area">
            <div className="module_1_2">
                <div className="link_3">
                    <div>
                        <h2 className="module_1_2_title">어버이날</h2>
                        <p className="module_1_text">얇아진 두께. 더 커진 존재감.</p>
                        <div className="button">
                            <button className="button_blue">쇼핑하기</button>
                        </div>
                    </div>
                </div>
            </div>
        </a>
        </section>
        <section className="module_2_link">
            <a href="#" className="module_2_link_area">
                <div className="module_2">
                    <div className="link">
                        <div>
                            <h2 className="module_2_title">MacBook Air</h2>
                            <p className="module_2_text">하늘빛 새 컬러. <br /> M4 칩 탑재로 성능도 하늘 높이.</p>
                            <div className="button_module_2">
                                <button className="button_blue_module_2">더 알아보기</button>
                                <button className="button_white_module_2" onClick={handleShopClick}>구입하기</button>
                            </div>
                            <div className="module_2_AI_text">
                                <p className="AI_text">Apple Intelligence를 위한 탄생.</p>
                                <p className="AI_text_describe">Apple Intelligence, 현재 한국어로 서비스 중</p>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            <a href="#" className="module_2_link_area">
                <div className="module_2_1">
                    <div className="link">
                        <div>
                            <h2 className="module_2_title_ipadair"></h2>
                            <p className="module_2_text">이제 막강한 성능의 M3 칩 탑재.</p>
                            <div className="button_module_2">
                                <button className="button_blue_module_2">더 알아보기</button>
                                <button className="button_white_module_2" onClick={handleShopClick}>구입하기</button>
                            </div>
                            <div className="module_2_AI_text_ipadair">
                                <p className="AI_text">Apple Intelligence를 위한 탄생.</p>
                                <p className="AI_text_describe">Apple Intelligence, 현재 한국어로 서비스 중</p>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            <a href="#" className="module_2_link_area">
                <div className="module_2_2">
                    <div className="link">
                        <div>
                            <h2 className="module_2_2_title">iPad Pro</h2>
                            <p className="module_2_2_text">놀라우리만치 얇다. 엄청나게 강력하다.</p>
                            <div className="button_module_2">
                                <button className="button_blue_module_2">더 알아보기</button>
                                <button className="button_white_module_2" onClick={handleShopClick}>구입하기</button>
                            </div>
                            <div className="module_2_AI_text">
                                <p className="AI_text">Apple Intelligence를 위한 탄생.</p>
                                <p className="AI_text_describe">Apple Intelligence, 현재 한국어로 서비스 중</p>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            <a href="#" className="module_2_link_area">
                <div className="module_2_3">
                    <div className="link">
                        <div className="module_2_3_title">
                            <h2 className="module_2_2_title">AirPods 4</h2>
                            <p className="module_2_2_text">아이콘의 귀환. 사운드의 진화.<br /> 액티브 노이즈 캔슬링 탑재.</p>
                            <div className="button_module_2">
                                <button className="button_blue_module_2">더 알아보기</button>
                                <button className="button_white_module_2" onClick={handleShopClick}>구입하기</button>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            <a href="#" className="module_2_link_area">
                <div className="module_2_4">
                    <div className="link">
                        <div className="module_2_title">
                            <div className="module_2_title_mac"></div>
                            <p className="module_2_text">Mac으로 갈아타기, 참 쉽습니다.</p>
                            <div className="button_module_2">
                                <button className="button_blue_module_2">더 알아보기</button>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            <a href="#" className="module_2_link_area">
                <div className="module_2_5">
                    <div className="link">
                        <div className="module_2_title">
                            <div className="module_2_title_tradein"></div>
                            <p className="module_2_text">iPhone 12 이상의 모델을 보상 판매하면<br />₩200,000-₩1,000,000<br />상당의 크레딧이.</p>
                            <div className="button_module_2">
                                <button className="button_blue_module_2">견적 확인하기</button>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            </section>
        <section className="module_3" id="slideshow-container">            
            <div className="slide-container">
                <ul className="slide-container-ul" id="slide-list">
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/HsJqgEXXaevqJ94-tyz0jQ/1250x703.jpg" alt="슬라이드 이미지 1"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/EviF5KEP5X6ycr0I5QR_IA/1250x703.jpg" alt="슬라이드 이미지 2"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/hCfBMF1R8mitgipZtRrJIw/1250x703.jpg" alt="슬라이드 이미지 3"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/vWrruv_JuOZkCwWQG6ZVWw/1250x703.jpg" alt="슬라이드 이미지 4"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/uemUr1iuDVlIR_UQxdOaeg/1250x703.jpg" alt="슬라이드 이미지 5"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/71SCc2C4bOuYVD9-3P-PQw/1250x703.jpg" alt="슬라이드 이미지 6"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/SSVr2ZxJ3bUc655YFoRy1Q/1250x703.jpg" alt="슬라이드 이미지 7"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/PpNA7zp0nJJN23khb-XDUw/1250x703.jpg" alt="슬라이드 이미지 8"/>
                        </a>
                    </li>
                    <li className="slide">
                        <a href="#">
                            <img src="https://is1-ssl.mzstatic.com/image/thumb/xO0BO6SH877VpYQg4t5yjw/1250x703.jpg" alt="슬라이드 이미지 9"/>
                        </a>
                    </li>
                </ul>
            </div>
            <div className="slide-preview-prev"></div>
            <div className="slide-preview-next"></div>
            <div className="slide-nav" id="slide-nav"></div>
        </section>
    </main>
    <footer className="footer">
        <div className="footer_content">
            <section className="footer_title">
                <ul>
                    <li>1. Apple Intelligence는 Siri 및 기기 언어를 한국어, 중국어(간체), 영어(오스트레일리아, 캐나다, 인도, 아일랜드, 뉴질랜드, 싱가포르, 남아프리카 공화국, 영국, 미국), 프랑스어, 독일어, 이탈리아어, 일본어, 포르투갈어(브라질), 스페인어로 설정한 iPhone 16 전체 모델, iPhone 15 Pro, iPhone 15 Pro Max, iPad mini(A17 Pro 모델) 그리고 M1 이후 iPad 및 Mac 모델에서 베타로 사용할 수 있으며, iOS 18, iPadOS 18, macOS Sequoia 소프트웨어 업데이트를 통해 제공됩니다. 올해 안으로 계속해서 베트남어를 비롯한 지원 언어를 추가해 나갈 예정입니다. 일부 기능은 한국어로 제공되지 않습니다.</li>
                    <br />
                    <li>2. 두 가지 모델로 제공: AirPods 4 및 AirPods 4 액티브 노이즈 캔슬링 모델.</li>
                    <br />
                    <li>3. ₩1,000,000은 iPhone 15 Pro Max 1TB 모델의 보상 판매 금액으로, 보상 판매 서비스는 Apple의 보상 판매 파트너사를 통해 제공됩니다. Apple 및 Apple의 계열사는 고객과 파트너 간 계약의 당사자가 아닙니다. 보상 판매 견적액은 예상 금액일 뿐이며, 실제 보상 판매 금액이 예상 금액보다 낮을 수도 있습니다. 보상 판매 금액은 보상 판매 대상이 되는 제품의 상태, 연도, 모델, 그리고 보상 판매 대상이 되는 제품이 최초 판매된 국가/지역에 따라 달라집니다. 일부 기기는 보상 판매 대상이 아닙니다. 기기를 보상 판매하기 위해서는 민법상 성년이어야 합니다. 보상 판매 금액은 적용 가능한 새 기기 구입 시 적용하거나 Apple Store Gift Card로 받을 수 있습니다. 새 Apple 기기 구매 시, 현재 소유한 기기의 가치만큼 할인을 받을 수도 있습니다. 최종 확정 금액은 보상 판매 대상 기기를 수령한 후, 예상 금액 산정 시 제시한 기기의 설명과 일치하는지 비교 검수 후 정해집니다. 부가세는 새로 구입한 기기의 총액을 바탕으로 부과됩니다. 일부 매장에서는 보상 판매를 제공하지 않으며, 매장 내 보상 판매와 온라인 보상 판매 프로그램 간 내용에 차이가 있을 수 있습니다. 일부 매장은 추가 요구 사항이 있을 수 있습니다. Apple의 보상 판매 파트너는 보상 판매 거래를 거부, 취소하거나 보상 판매 수량을 제한할 권리를 보유합니다. 적용 대상 기기의 보상 판매 및 재활용에 대한 자세한 내용은 Apple의 보상 판매 파트너사에서 확인할 수 있습니다. 규제 및 제한이 적용될 수 있습니다.</li>
                    <br />
                    <li>Apple TV+ 이용을 위해서는 구독이 필요합니다.</li>
                    <br />
                    <li>기능은 변경될 수 있습니다. 일부 기능, 애플리케이션 및 서비스를 이용할 수 없는 국가나 언어도 있습니다.</li>
                    <br />
                </ul>
                
            </section>
            <section className="footer_nav">
                <div className="footer_column">
                  <h3>쇼핑 및 알아보기</h3>
                  <ul>
                    <li><a href="#">스토어</a></li>
                    <li><a href="#">Mac</a></li>
                    <li><a href="#">iPad</a></li>
                    <li><a href="#">iPhone</a></li>
                    <li><a href="#">Watch</a></li>
                    <li><a href="#">Vision</a></li>
                    <li><a href="#">AirPods</a></li>
                    <li><a href="#">TV 및 홈</a></li>
                    <li><a href="#">AirTag</a></li>
                    <li><a href="#">액세서리</a></li>
                  </ul>
                  <h3>Apple 지갑</h3>
                  <ul>
                    <li><a href="#">지갑</a></li>
                    <li><a href="#">Apple Pay</a></li>
                  </ul>
                </div>
                  
                  <div className="footer_column">
                    <h3>계정</h3>
                    <ul>
                      <li><a href="#">Apple 계정 관리</a></li>
                      <li><a href="#">Apple Store 계정</a></li>
                      <li><a href="#">iCloud.com</a></li>
                    </ul>
                    <h3>엔터테인먼트</h3>
                    <ul>
                      <li><a href="#">Apple One</a></li>
                      <li><a href="#">Apple TV+</a></li>
                      <li><a href="#">Apple Music</a></li>
                      <li><a href="#">Apple Arcade</a></li>
                      <li><a href="#">Apple 팟캐스트</a></li>
                      <li><a href="#">Apple Books</a></li>
                      <li><a href="#">App Store</a></li>
                    </ul>
                  </div>
                  
                  <div className="footer_column">
                    <h3>Apple Store</h3>
                    <ul>
                      <li><a href="#">매장 찾기</a></li>
                      <li><a href="#">Genius Bar</a></li>
                      <li><a href="#">Today at Apple</a></li>
                      <li><a href="#">그룹 예약</a></li>
                      <li><a href="#">Apple 캠프</a></li>
                      <li><a href="#">Apple Store 앱</a></li>
                      <li><a href="#">인증 리퍼비쉬 제품</a></li>
                      <li><a href="#">Apple Trade In</a></li>
                      <li><a href="#">할부 방식</a></li>
                      <li><a href="#">주문 상태</a></li>
                      <li><a href="#">쇼핑 도움말</a></li>
                    </ul>
                  </div>
                  
                  <div className="footer_column">
                    <h3>비즈니스</h3>
                    <ul>
                      <li><a href="#">Apple과 비즈니스</a></li>
                      <li><a href="#">비즈니스를 위한 제품 쇼핑하기</a></li>
                    </ul>
                    <h3>교육</h3>
                    <ul>
                      <li><a href="#">Apple과 교육</a></li>
                      <li><a href="#">초중고재 제품 쇼핑하기</a></li>
                      <li><a href="#">대학 생활을 위한 제품 쇼핑하기</a></li>
                    </ul>
                  </div>
                  
                  <div className="footer_column">
                    <h3>Apple의 가치관</h3>
                    <ul>
                      <li><a href="#">손쉬운 사용</a></li>
                      <li><a href="#">교육</a></li>
                      <li><a href="#">환경</a></li>
                      <li><a href="#">개인정보 보호</a></li>
                      <li><a href="#">공급망</a></li>
                    </ul>
                    <h3>Apple 정보</h3>
                    <ul>
                      <li><a href="#">Newsroom</a></li>
                      <li><a href="#">Apple 리더십</a></li>
                      <li><a href="#">채용 안내</a></li>
                      <li><a href="#">윤리 및 규정 준수</a></li>
                      <li><a href="#">이벤트</a></li>
                      <li><a href="#">일자리 창출</a></li>
                      <li><a href="#">Apple 연락처</a></li>
                    </ul>
                  </div>
                </section>
            <section className="footer_bottom">
                <div className="footer_bottom_describe">
                  <p>다양한 쇼핑 방법: <a href="#">Apple Store를 방문하거나</a>, <a href="#">리셀러</a>를 찾아보거나, <a href="#">080-123-4567</a>번으로 전화하세요.</p>
                </div>
            </section>
            <section className="footer_bottom_nav">
                <div className="footer_bottom_nav_1">
                    <p>Copyright © 2025 모든 권리 보유.</p>
                    <ul>
                        <li><a href="#">개인정보 처리방침</a></li>
                        <li><a href="#">웹 사이트 이용 약관</a></li>
                        <li><a href="#">판매 및 환불</a></li>
                        <li><a href="#">법적 고지</a></li>
                        <li><a href="#">사이트 맵</a></li>
                    </ul>
                    <ul className="footer_global">
                        <li><a href="#">대한민국</a></li>
                    </ul>
                </div>

                <div className="footer_bottom_describe">
                    <p>애플코리아 | 대표이사: 예제 | 주소: 서울특별시 강남구 | 전화: 080-123-4567 | <a href="#">https://support.apple.com/ko-kr</a> | 사업자등록번호: 123-45-67890 | 통신판매업신고번호: 제2025-서울예제-0123호 | 호스팅 서비스 제공: 예제 | <a href="#">사업자정보</a> |사업자등록번호: 123-45-67890 | 통신판매업신고번호: 제2025-서울예제-0123호 |호스팅 서비스 제공: 예제
                    <a href="#">사업자정보</a>
                    </p>
                </div>
            </section>
        </div>
    </footer>
    </>
  );
}

export default App;
