// ../../components/page/home/home.js

import React, { useEffect, useState } from "react";
import Button from '../../common/button/button';
import { useHeader } from '../../../contexts/HeaderContext';
import style from './home.module.css';

function Home() {
    
  
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
            {/* 헤더 섹션 */}
            <main className={style.homepage}>
                <section className={style.homepage_header_section}>
                    <a href="#">
                        <div className={style.homepage_link_section_card_iphone}>
                            <div className={style.link}>
                                <div className= {style.product_main}>
                                <h2 className={style.title_section_1}>iPhone</h2>
                                <p className={style.text_section_1}>iPhone 16 라인업을 만나볼까요?</p>
                                <div className={style.button}>
                                    <Button text="더 알아보기" type="blue" path="#" />
                                    <Button text="쇼핑하기" type="white" path="#" />
                                </div>
                                <p className={style.AI_text}>Apple Intelligence를 위한 탄생.</p>
                                <p className={style.AI_text_describe}>Apple Intelligence, 현재 한국어로 서비스 중</p>
                            </div>
                        </div>
                    </div>
                </a>
                <a href="#">
                    <div className={style.homepage_link_section_card_watch}>
                        <div className={style.link}>
                            <div className={style.product_main}>   
                                <div className={style.product_watch_title}></div>
                                <p className={style.text_section_1}>얇아진 두께. 더 커진 존재감.</p>
                                <div className={style.button}>
                                    <Button text="더 알아보기" type="blue" path="#" />
                                    <Button text="구매하기" type="white" path="#" />
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
                <a href="#">
                    <div className={style.homepage_link_section_card_mothersday}>
                        <div className="link_3">
                            <div className={style.product_main}>
                                <h2 className={style.title_section_1}>어버이날</h2>
                                <div className={style.button_center}>
                                    <Button text="쇼핑하기" type="blue" path="#" />
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
                </section>
                {/* 메인 섹션 */}
                <section className={style.homepage_main_section}>
                    <a href="#" className={style.homepage_main_section_link_area}>
                        <div className={style.homepage_link_section_card_macbookair}>
                            <div className={style.homepage_link_section_card_layout}>
                                <div className={style.homepage_card_macbookair_title}>
                                    <div className={style.homepage_card_macbookair}>
                                        <h2 className={style.title_section2_black}>MacBook Air</h2>
                                        <p className={style.text_section_2_black}>하늘빛 새 컬러. <br /> M4 칩 탑재로 성능도 하늘 높이.</p>
                                        <div className={style.button}>
                                            <Button text="더 알아보기" type="blue" path="#" />
                                            <Button text="구입하기" type="white" path="#" />
                                        </div>
                                    </div>
                                    <div className={style.homepage_main_AI_text}>
                                        <p className={style.AI_text}>Apple Intelligence를 위한 탄생.</p>
                                        <p className={style.AI_text_describe}>Apple Intelligence, 현재 한국어로 서비스 중</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                    <a href="#" className={style.homepage_main_section_link_area}>
                        <div className={style.homepage_link_section_card_ipadair}>
                            <div className={style.homepage_link_section_card_layout}>
                                <div className={style.homepage_card_ipadair}>
                                    <h2 className={style.title_product_ipadair}></h2>
                                    <p className={style.text_section_2_black}>이제 막강한 성능의 M3 칩 탑재.</p>
                                    <div className={style.button}>
                                        <Button text="더 알아보기" type="blue" path="#" />
                                        <Button text="구입하기" type="white" path="#"  />
                                    </div>
                                    <div className={style.homepage_main_AI_text_ipadair}>
                                        <p className={style.AI_text}>Apple Intelligence를 위한 탄생.</p>
                                        <p className={style.AI_text_describe}>Apple Intelligence, 현재 한국어로 서비스 중</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                    <a href="#" className={style.homepage_main_section_link_area}>
                        <div className={style.homepage_link_section_card_ipadpro}>
                            <div className={style.homepage_link_section_card_layout}>
                                <div className={style.homepage_card_ipadpro}>
                                    <h2 className={style.title_section2_white}>iPad Pro</h2>
                                    <p className={style.text_section_2_white}>놀라우리만치 얇다. 엄청나게 강력하다.</p>
                                    <div className={style.button}>
                                        <Button text="더 알아보기" type="blue" path="#" />
                                        <Button text="구입하기" type="white" path="#" />
                                    </div>
                                    <div className={style.homepage_main_AI_text}>
                                        <p className={style.AI_text}>Apple Intelligence를 위한 탄생.</p>
                                        <p className={style.AI_text_describe}>Apple Intelligence, 현재 한국어로 서비스 중</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                    <a href="#" className={style.homepage_main_section_link_area}>
                        <div className={style.homepage_link_section_card_airpods}>
                            <div className={style.homepage_link_section_card_layout}>
                                <div className={style.homepage_card_airpods}>

                                <div className={style.button}>
                                        <Button text="더 알아보기" type="blue" path="#" />
                                        <Button text="구입하기" type="white" path="#" />
                                    </div>
                                <p className={style.text_section_2_white}>아이콘의 귀환. 사운드의 진화.<br /> 액티브 노이즈 캔슬링 탑재.</p>
                                    <h2 className={style.title_section2_white}>AirPods 4</h2>     
                                </div>
                            </div>
                        </div>
                    </a>
                    <a href="#" className={style.homepage_main_section_link_area}>
                        <div className={style.homepage_link_section_card_mac}>
                            <div className={style.homepage_link_section_card_layout}>
                                <div className={style.homepage_card_mac}>
                                    <div className={style.homepage_card_mac_title}></div>
                                    <p className={style.homepage_card_text}>Mac으로 갈아타기, 참 쉽습니다.</p>
                                    <div className={style.button_center}>
                                        <Button text="더 알아보기" type="blue" path="#" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                    <a href="#" className={style.homepage_main_section_link_area}>
                        <div className={style.homepage_link_section_card_tradein}>
                            <div className={style.homepage_link_section_card_layout}>
                                <div className={style.homepage_card_tradein}>
                                    <div className={style.homepage_card_tradein_title}></div>
                                    <p className={style.text_section_2_black}>iPhone 12 이상의 모델을 보상 판매하면<br />₩200,000-₩1,000,000<br />상당의 크레딧이.</p>
                                    <div className={style.button_center}>
                                        <Button text="견적 확인하기" type="blue" path="#" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                    </section>
                    {/* 슬라이드 섹션 */}
                <section className={style.homepage_footer_section} id="slideshow-container">            
                    <div className={style.slide_container}>
                        <ul className={style.slide_container_ul} id="slide-list">
                            <li className={`${style.slide} ${currentSlideIndex === 0 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/HsJqgEXXaevqJ94-tyz0jQ/1250x703.jpg" alt="슬라이드 이미지 1"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 1 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/EviF5KEP5X6ycr0I5QR_IA/1250x703.jpg" alt="슬라이드 이미지 2"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 2 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/hCfBMF1R8mitgipZtRrJIw/1250x703.jpg" alt="슬라이드 이미지 3"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 3 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/vWrruv_JuOZkCwWQG6ZVWw/1250x703.jpg" alt="슬라이드 이미지 4"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 4 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/uemUr1iuDVlIR_UQxdOaeg/1250x703.jpg" alt="슬라이드 이미지 5"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 5 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/71SCc2C4bOuYVD9-3P-PQw/1250x703.jpg" alt="슬라이드 이미지 6"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 6 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/SSVr2ZxJ3bUc655YFoRy1Q/1250x703.jpg" alt="슬라이드 이미지 7"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 7 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/PpNA7zp0nJJN23khb-XDUw/1250x703.jpg" alt="슬라이드 이미지 8"/>
                                </a>
                            </li>
                            <li className={`${style.slide} ${currentSlideIndex === 8 ? `${style.active}` : ''}`}>
                                <a href="#">
                                    <img src="https://is1-ssl.mzstatic.com/image/thumb/xO0BO6SH877VpYQg4t5yjw/1250x703.jpg" alt="슬라이드 이미지 9"/>
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div 
                        className={style.slide_preview_prev} 
                        onClick={showPrevSlide}
                        onMouseEnter={stopAutoSlide}
                        onMouseLeave={startAutoSlide}
                    ></div>
                    <div 
                        className={style.slide_preview_next} 
                        onClick={showNextSlide}
                        onMouseEnter={stopAutoSlide}
                        onMouseLeave={startAutoSlide}
                    ></div>
                    <div className={style.slide_nav} id="slide-nav">
                        {[...Array(9)].map((_, index) => (
                            <div
                                key={index}
                                className={`${style.nav_dot} ${currentSlideIndex === index ? 'active' : ''}`}
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