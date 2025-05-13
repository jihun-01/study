import React from 'react';
import './card480.css';

const Card480 = ({head, text, describe,image,link}) => {
    return (
        <div className="image_card">
            <a href={link}>
                <img src={image} alt={head} />
                <div className="image_card_info">
                    <div className="image_card_info_header">
                        {head}
                    </div>
                    <div className="image_card_info_body">
                        <span className="image_card_info_body_text">
                            <p>{text}</p>
                        </span>
                        <span className="image_card_info_body_describe">
                            <p>{describe}</p>
                        </span>
                    </div>
                </div>
            </a>
        </div>
    )
}

export default Card480;
