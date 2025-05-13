import React from 'react';
import './card400.css';
const Card400 = ({product_name, product_text, product_price, product_image}) => {
    return (
        <div className="product_card">
            <a href="#">
            <img src={product_image} alt={product_name} />
            <div className="product_card_info">
                <div className="product_card_info_header">
                    {product_name}
                </div>
                <div className="product_card_info_body">
                    <span className="product_card_info_body_text">{product_text}</span>
                    <span className="product_card_info_body_price">{product_price}</span>
                </div>
            </div>
            </a>
        </div>
    )
}


export default Card400;
