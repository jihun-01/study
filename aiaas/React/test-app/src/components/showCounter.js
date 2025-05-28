// ./src/components/showCounter.js
import { useSelector } from "react-redux";

const ShowCounter = () => {
    const counter = useSelector((state) => state.counter.counter);
    return (
        <>
        <p>showCounter 카운터 값</p>
        <p>카운터값: {counter}</p>
        </>
    );
};

export default ShowCounter;