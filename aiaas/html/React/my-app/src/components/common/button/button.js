import React from 'react';
import './button.css';

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
        <button className="button_white" onClick={handleClick}>{text}</button>
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
        <button className="button_blue" onClick={handleClick}>{text}</button>
    )
}

export {WhiteButton, BlueButton};