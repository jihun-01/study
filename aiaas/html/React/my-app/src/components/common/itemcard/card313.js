import React from 'react';
import styles from './card313.module.css';
import { useFetch } from '../../../customhook/useFetch';

const Card313 = ({ category }) => {
    const { data, error, loading } = useFetch('/card313.json');

    if (loading) return <div>로딩 중...</div>;
    if (error) return <div>에러 발생: {error}</div>;
    if (!data) return null;

    const categoryCards = data[category]?.cards || [];

    if (categoryCards.length === 0) {
        return <div>해당 카테고리의 제품이 없습니다.</div>;
    }

    return (
        <div className={styles.card313_container}>
            {categoryCards.map((card) => (
                <div key={card.id} className={styles.card313}>
                    <a href={card.path}>
                        <div className={styles.card313_image}>
                            <img src={card.image} alt={card.name} />
                        </div>
                        <div className={styles.card313_info}>
                            <div className={styles.card313_colorimage}>
                                <ul className={styles.card313_colorimage}>
                                    {card.colors.map((color, index) => (
                                        <li key={index} className={styles.card313_colorimage_item}>
                                            <img src={color} alt={`Color ${index}`} />
                                        </li>
                                    ))}
                                </ul>
                            </div>
                            <div className={styles.card313_info_main}>
                                <span className={styles.card313_info_text}>
                                    {card.text}
                                </span>
                                <span className={styles.card313_info_name}>
                                    <p>{card.name}</p>
                                </span>
                            </div>
                            <div className={styles.card313_info_price}>
                                <p>{card.price}</p>
                            </div>
                        </div>
                    </a>
                </div>
            ))}
        </div>
    );
};

export default Card313;