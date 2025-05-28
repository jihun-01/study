// ./src/components/counter.js
// import React, { useReducer } from "react";

// const initialState = { count: 0 };

// function reducer(state, action) {
//   switch (action.type) {
//     case "INCREMENT":
//       return { count: state.count + 1 };
//     case "DECREMENT":
//       return { count: state.count - 1 };
//     default:
//       throw new Error();
//   }
// }

// function Counter() {
//   const [state, dispatch] = useReducer(reducer, initialState);

//   return (
//     <div>
//       <p>Count: {state.count}</p>
//       <button onClick={() => dispatch({ type: "INCREMENT" })}>Increment</button>
//       <button onClick={() => dispatch({ type: "DECREMENT" })}>Decrement</button>
//     </div>
//   );
// }

// export default Counter;

import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { increment, decrement, toggleCounter } from "../actions/counterAction";
import ShowCounter from "./showCounter";

const Counter = () => {
    const counter = useSelector((state) => state.counter.counter);
    const showCounter = useSelector((state) => state.counter.showCounter);
    const dispatch = useDispatch();



    return (
        <div>
          <p>Counter 카운터 값</p>
          {(showCounter) && <p>카운터값: {counter}</p>}
          <ShowCounter />
          <h1>리덕스 카운터</h1>
      
          <button onClick={() => dispatch(increment(5))}>
            카운터 +5
          </button>
          <button onClick={() => dispatch(decrement(3))}>
            카운터 -3
          </button>
          <br/>
          <br/>
          <button onClick={() => dispatch(toggleCounter())}>
            {(showCounter) ? "카운터 숨기기" : "카운터 보이기"}
          </button>
        </div>

    );
};

export default Counter; 