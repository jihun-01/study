import React from 'react';
import styles from './button.module.css';

const WhiteButton = ({text, onClick, path}) => {
    const handleClick = (e) => {
        e.stopPropagation();
        if (path) {
            window.location.href = path;
        }
        if (onClick) {
            onClick(e);
        }
    };

    return (
        <button className={styles.button_white} onClick={handleClick}>{text}</button>
    )
}

const BlueButton = ({text, onClick, path}) => {
    const handleClick = (e) => {
        e.stopPropagation();
        if (path) {
            window.location.href = path;
        }
        if (onClick) {
            onClick(e);
        }
    };

    return (
        <button className={styles.button_blue} onClick={handleClick}>{text}</button>
    )
}

export {WhiteButton, BlueButton};