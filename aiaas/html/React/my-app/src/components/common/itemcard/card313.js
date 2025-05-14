//components/common/itemcard/card313.js

import React from 'react';
import './card313.css';

const Card313 = ({name, text, price, image, path}) => {
    return (
        <div className="card313">
            <a href={path}>
                <div className="card313_image">
                    <img src={image} alt={name} />
                </div>
                    
                <div className="card313_info">
                    <div className="card313_colorimage">
                        <ul className="card313_colorimage">
                            <li className="card313_colorimage_item"><img/>    </li>
                            <li className="card313_colorimage_item">    </li>
                            <li className="card313_colorimage_item">    </li>
                            <li className="card313_colorimage_item">    </li>
                            <li className="card313_colorimage_item">    </li>
                            <li className="card313_colorimage_item">    </li>
                            <li className="card313_colorimage_item">    </li>
                            <li className="card313_colorimage_item">    </li>
                        </ul>
                    </div>
                    <div className="card313_info_main">
                        <span className="card313_info_text">
                            {text}
                        </span>
                        <span className="card313_info_name">
                            <p>{name}</p>
                        </span>
                    </div>
                    <div className="card313_info_price">
                        <p>{price}</p>
                    </div>
                </div>
            </a>
        </div>
    )
}

export default Card313;
