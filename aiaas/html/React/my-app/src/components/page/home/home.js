// ../../components/page/home/home.js

import React, { useEffect, useState } from "react";
import Button from '../../common/button/button';
import { useHeader } from '../../../contexts/HeaderContext';

function Home() {
    
    const { changePage } = useHeader();

    useEffect(() => {
        changePage('home');
    }, [changePage]);

    // 슬라이드 상태 관리
    const [currentSlideIndex, setCurrentSlideIndex] = useState(0);
    const [slideTimer, setSlideTimer] = useState(null);
    const slideInterval = 3000; // 슬라이드 간격 (3초)

    // 슬라이드 표시 함수
    const showSlide = (index) => {
        if (index < 0) {
            index = 8; // 마지막 슬라이드로 이동
        } else if (index >= 9) {
            index = 0; // 첫 번째 슬라이드로 이동
        }
        setCurrentSlideIndex(index);
    };

    // 이전 슬라이드
    const showPrevSlide = () => {
        showSlide(currentSlideIndex - 1);
    };

    // 다음 슬라이드
    const showNextSlide = () => {
        showSlide(currentSlideIndex + 1);
    };

    // 자동 슬라이드 시작
    const startAutoSlide = () => {
        stopAutoSlide(); // 기존 타이머가 있다면 정지
        const timer = setInterval(showNextSlide, slideInterval);
        setSlideTimer(timer);
    };

    // 슬라이드 자동 전환 정지
    const stopAutoSlide = () => {
        if (slideTimer) {
            clearInterval(slideTimer);
            setSlideTimer(null);
        }
    };

    // 컴포넌트 마운트 시 초기화
    useEffect(() => {
        startAutoSlide();

        // 컴포넌트 언마운트 시 타이머 정리
        return () => {
            stopAutoSlide();
        };
    }, []);

    return (
        <>
            <main className="main">
                <section className="module_1_link">
                <a href="#" className="module_1_link_area">
                    <div className="module_1">
                        <div className="link">
                            <div className= "product_main">
                                <h2 className="module_1_title">iPhone</h2>
                                <p className="module_1_text">iPhone 16 라인업을 만나볼까요?</p>
                                <div className="button">
                                    <Button text="더 알아보기" type="blue" path="#" />
                                    <Button text="쇼핑하기" type="white" path="#" />
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
                            <div className="product_main">   
                                <div className="module_1_1_title"></div>
                                <p className="module_1_text">얇아진 두께. 더 커진 존재감.</p>
                                <div className="button">
                                    <Button text="더 알아보기" type="blue" path="#" />
                                    <Button text="구매하기" type="white" path="#" />
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
                <a href="#" className="module_1_link_area">
                    <div className="module_1_2">
                        <div className="link_3">
                            <div className="product_main">
                                <h2 className="module_1_2_title">어버이날</h2>
                                <div className="button_center">
                                    <Button text="쇼핑하기" type="blue" path="#" />
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
                                        <Button text="더 알아보기" type="blue" path="#" />
                                        <Button text="구입하기" type="white" path="#" />
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
                                        <Button text="더 알아보기" type="blue" path="#" />
                                        <Button text="구입하기" type="white" path="#"  />
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
                                        <Button text="더 알아보기" type="blue" path="#" />
                                        <Button text="구입하기" type="white" path="#" />
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
                                        <Button text="더 알아보기" type="blue" path="#" />
                                        <Button text="구입하기" type="white" path="#" />
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
                                        <Button text="더 알아보기" type="blue" path="#" />
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
                                        <Button text="견적 확인하기" type="blue" path="#" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                    </section>
                <section className="module_3" id="slideshow-container">            
                    <div className="slide-container">
                        <ul className="slide-container-ul" id="slide-list">
                            <li className={`slide ${currentSlideIndex === 0 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/HsJqgEXXaevqJ94-tyz0jQ/1250x703.jpg" alt="슬라이드 이미지 1"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 1 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/EviF5KEP5X6ycr0I5QR_IA/1250x703.jpg" alt="슬라이드 이미지 2"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 2 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/hCfBMF1R8mitgipZtRrJIw/1250x703.jpg" alt="슬라이드 이미지 3"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 3 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/vWrruv_JuOZkCwWQG6ZVWw/1250x703.jpg" alt="슬라이드 이미지 4"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 4 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/uemUr1iuDVlIR_UQxdOaeg/1250x703.jpg" alt="슬라이드 이미지 5"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 5 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/71SCc2C4bOuYVD9-3P-PQw/1250x703.jpg" alt="슬라이드 이미지 6"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 6 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/SSVr2ZxJ3bUc655YFoRy1Q/1250x703.jpg" alt="슬라이드 이미지 7"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 7 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/PpNA7zp0nJJN23khb-XDUw/1250x703.jpg" alt="슬라이드 이미지 8"/>
                                </a>
                            </li>
                            <li className={`slide ${currentSlideIndex === 8 ? 'active' : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/xO0BO6SH877VpYQg4t5yjw/1250x703.jpg" alt="슬라이드 이미지 9"/>
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div 
                        className="slide-preview-prev" 
                        onClick={showPrevSlide}
                        onMouseEnter={stopAutoSlide}
                        onMouseLeave={startAutoSlide}
                    ></div>
                    <div 
                        className="slide-preview-next" 
                        onClick={showNextSlide}
                        onMouseEnter={stopAutoSlide}
                        onMouseLeave={startAutoSlide}
                    ></div>
                    <div className="slide-nav" id="slide-nav">
                        {[...Array(9)].map((_, index) => (
                            <div
                                key={index}
                                className={`nav-dot ${currentSlideIndex === index ? 'active' : ''}`}
                                onClick={() => showSlide(index)}
                                onMouseEnter={stopAutoSlide}
                                onMouseLeave={startAutoSlide}
                            />
                        ))}
                    </div>
                </section>
            </main>
        </>
    );
}

export default Home;