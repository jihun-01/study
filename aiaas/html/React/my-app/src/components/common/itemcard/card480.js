//components/common/itemcard/card480.js
import './card480.css';

const Card480 = ({text, name,describe,image,path}) => {
    
    return (
        <div className="image_card">
            <a href={path}>
                <img src={image} alt={name} />
                <div className="image_card_info">
                    <div className="image_card_info_text">
                        {text}
                    </div>
                    <div className="image_card_info_body">
                        <span className="image_card_info_body_name">
                            <p>{name}</p>
                        </span>
                        <span className="image_card_info_body_describe">
                            {describe}
                        </span>
                    </div>
                </div>
            </a>
        </div>
    )
}

export default Card480;
