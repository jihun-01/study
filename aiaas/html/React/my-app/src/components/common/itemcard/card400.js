//components/common/itemcard/card400.js
import React from 'react';
import styles from './card400.module.css';
const Card400 = ({name, describe, image, path, price}) => {
    return (
        <div className={styles.product_card}>
            <a href={path}>
            <img src={image} alt={name} />
            <div className={styles.product_card_info}>
                <div className={styles.product_card_info_header}>
                    {name}
                </div>
                <div className={styles.product_card_info_body}>
                    <span className={styles.product_card_info_body_text}><p>{describe}</p></span>
                    <span className={styles.product_card_info_body_price}>{price}</span>
                </div>
            </div>
            </a>
        </div>
    )
}


export default Card400;
