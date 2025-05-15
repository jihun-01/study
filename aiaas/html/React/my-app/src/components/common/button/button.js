// ../../components/common/button/button.js
import React from 'react';
import styles from './button.module.css';


const Button = ({text, type = 'white', onClick, path}) => {
    const handleClick = (e) => {
        e.stopPropagation();
        if (path) {
            window.location.href = path;
        }
        if (onClick) {
            onClick(e);
        }
    };

    // 버튼 타입에 따른 클래스명 결정
    const getButtonClass = () => {
        switch(type) {
            case 'blue':
                return styles.button_blue;
            case 'black':
                return styles.button_black;
            case 'white':
            default:
                return styles.button_white;
        }
    };

    return (
        <button className={getButtonClass()} onClick={handleClick}>{text}</button>
    );
};

export default Button;