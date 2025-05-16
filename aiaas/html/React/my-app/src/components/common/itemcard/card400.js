//components/common/itemcard/card400.js
import React from 'react';
import styles from './card400.module.css';

const Card400 = ({text, name, describe, image, path, price, describeType, nameType, priceType}) => {
    // 텍스트 스타일 결정 함수
    const getDescribeClass = (describeType) => {
        switch(describeType) {
            case 'white':
                return styles.product_card_info_body_text_white;
            case 'black':
                return styles.product_card_info_body_text_black;
            default:
                return styles.product_card_info_body_text;
        }
    };

    const getNameClass = (nameType) => {
        switch(nameType) {
            case 'white':
                return styles.product_card_info_header_text_white;
            default:
                return styles.product_card_info_header_text;
        }
    };

    const getPriceClass = (priceType) => {
        switch(priceType) {
            case 'white':
                return styles.product_card_info_body_price_white;
            default:
                return styles.product_card_info_body_price;
        }
    };
    

    return (
        <div className={styles.product_card}>
            <a href={path}>
                <img src={image} alt={name} />
                <div className={styles.product_card_info}>
                    <div className={styles.product_card_info_header}>
                        <span className={styles.product_card_info_header_txt}>{text}</span>
                        <span className={getNameClass(nameType)}>{name}</span>
                    </div>
                    <div className={styles.product_card_info_body}>
                        <span className={getDescribeClass(describeType)}><p>{describe}</p></span>
                        <span className={getPriceClass(priceType)}>{price}</span>
                    </div>
                </div>
            </a>
        </div>
    );
};

export default Card400;
