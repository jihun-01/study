// src/components/common/scrollbutton/ScrollButton.js

import React, { useState, useRef } from 'react';
import styles from './scrollbutton.module.css';

/**
 * 스크롤 버튼 컴포넌트
 * @param {Object} props
 * @param {React.ReactNode} props.children - 스크롤할 컨텐츠
 * @param {string} props.className - 추가할 클래스명
 * @param {number} props.scrollAmount - 한 번에 스크롤할 픽셀 양 (기본값: 400)
 */
const ScrollButton = ({ children, className, scrollAmount = 400 }) => {
    const containerRef = useRef(null);
    const [showLeftButton, setShowLeftButton] = useState(false);
    const [showRightButton, setShowRightButton] = useState(true);

    // 스크롤 버튼 클릭 핸들러
    const handleScroll = (direction) => {
        if (containerRef.current) {
            const container = containerRef.current;
            const scrollPosition = direction === 'left' 
                ? container.scrollLeft - scrollAmount 
                : container.scrollLeft + scrollAmount;
            
            container.scrollTo({
                left: scrollPosition,
                behavior: 'smooth'
            });

            // 스크롤 후 버튼 표시 여부 업데이트
            setTimeout(() => {
                setShowLeftButton(container.scrollLeft > 0);
                setShowRightButton(
                    container.scrollLeft < container.scrollWidth - container.clientWidth
                );
            }, 500);
        }
    };

    // 스크롤 이벤트 핸들러
    const handleScrollEvent = () => {
        if (containerRef.current) {
            const container = containerRef.current;
            setShowLeftButton(container.scrollLeft > 0);
            setShowRightButton(
                container.scrollLeft < container.scrollWidth - container.clientWidth
            );
        }
    };

    return (
        <div className={`${styles.scrollContainer} ${className}`}>
            {showLeftButton && (
                <button 
                    className={`${styles.scrollButton} ${styles.leftButton}`}
                    onClick={() => handleScroll('left')}
                    aria-label="왼쪽으로 스크롤"
                >
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <path d="M15 18L9 12L15 6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                </button>
            )}
            <div 
                ref={containerRef}
                className={styles.contentContainer}
                onScroll={handleScrollEvent}
            >
                {children}
            </div>
            {showRightButton && (
                <button 
                    className={`${styles.scrollButton} ${styles.rightButton}`}
                    onClick={() => handleScroll('right')}
                    aria-label="오른쪽으로 스크롤"
                >
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <path d="M9 6L15 12L9 18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                </button>
            )}
        </div>
    );
};

export default ScrollButton;