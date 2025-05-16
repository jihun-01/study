// src/contexts/HeaderContext.js
import React, { createContext, useState, useContext, useCallback, useMemo } from 'react';

const HeaderContext = createContext();

// 페이지별 헤더 스타일 정의를 컴포넌트 외부로 이동
const headerStyles = {
    home: {
        background: 'transparent',
        textColor: '#1d1d1f',
        isTransparent: true
    },
    store: {
        background: '#ffffff',
        textColor: '#1d1d1f',
        isTransparent: false
    },
    product: {
        background: '#f5f5f7',
        textColor: '#1d1d1f',
        isTransparent: false
    }
};

export const HeaderProvider = ({ children }) => {
    // 현재 페이지 상태
    const [currentPage, setCurrentPage] = useState('home');
    // 헤더 스타일 상태
    const [headerStyle, setHeaderStyle] = useState(headerStyles.home);

    // 페이지 변경 시 헤더 스타일 업데이트
    const changePage = useCallback((page) => {
        if (currentPage !== page) {  // 현재 페이지와 다른 경우에만 업데이트
            setCurrentPage(page);
            setHeaderStyle(headerStyles[page] || headerStyles.home);
        }
    }, [currentPage]);

    // 스크롤에 따른 헤더 스타일 변경
    const handleScroll = useCallback((scrollY) => {
        if (currentPage === 'home') {
            if (scrollY > 50) {
                setHeaderStyle({
                    background: '#ffffff',
                    textColor: '#1d1d1f',
                    isTransparent: false
                });
            } else {
                setHeaderStyle(headerStyles.home);
            }
        }
    }, [currentPage]);

    // Context 값 메모이제이션
    const contextValue = useMemo(() => ({
        currentPage,
        headerStyle,
        changePage,
        handleScroll
    }), [currentPage, headerStyle, changePage, handleScroll]);

    return (
        <HeaderContext.Provider value={contextValue}>
            {children}
        </HeaderContext.Provider>
    );
};

export const useHeader = () => {
    const context = useContext(HeaderContext);
    if (!context) {
        throw new Error('useHeader must be used within a HeaderProvider');
    }
    return context;
};