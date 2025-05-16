//components/common/itemcard/card480.js
import React from 'react';
import styles from './card480.module.css';

const Card480 = ({text, name,describe,image,path,cardType}) => {

    const getCardClass = (cardType) => {
        switch(cardType) {
            case 'small':
                return styles.image_card_info_small;
            default:
                return styles.image_card_info;
        }
    };
    return (
        <div className={styles.image_card}>
            <a href={path}>
                <img src={image} alt={name} />
                <div className={getCardClass(cardType)}>
                    <div className={styles.image_card_info_text}>
                        {text}
                    </div>
                    <div className={styles.image_card_info_body}>
                        <span className={styles.image_card_info_body_name}>
                            <p>{name}</p>
                        </span>
                        <span className={styles.image_card_info_body_describe}>
                            {describe}
                        </span>
                    </div>
                </div>
            </a>
        </div>
    )
}

export default Card480;
