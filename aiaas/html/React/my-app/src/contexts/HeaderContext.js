// src/contexts/HeaderContext.js
import React, { createContext, useState, useContext } from 'react';

const HeaderContext = createContext();

export const HeaderProvider = ({ children }) => {
    // 현재 페이지 상태
    const [currentPage, setCurrentPage] = useState('home');
    // 헤더 스타일 상태
    const [headerStyle, setHeaderStyle] = useState({
        background: 'transparent',
        textColor: '#1d1d1f',
        isTransparent: true
    });

    // 페이지별 헤더 스타일 정의
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

    // 페이지 변경 시 헤더 스타일 업데이트
    const changePage = (page) => {
        setCurrentPage(page);
        setHeaderStyle(headerStyles[page] || headerStyles.home);
    };

    // 스크롤에 따른 헤더 스타일 변경
    const handleScroll = (scrollY) => {
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
    };

    return (
        <HeaderContext.Provider value={{ 
            currentPage, 
            headerStyle, 
            changePage, 
            handleScroll 
        }}>
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