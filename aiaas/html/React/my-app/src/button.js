function Button(props) {

    console.log(props);

    return (
        <button>
            {props.btnName}
        </button>
    )
}

export default Button;