// ./src/actions/counterAction.js

export const increment = (value) => ({
    type: "INCREMENT",
    payload: value

});

export const decrement = (value) => ({
    type: "DECREMENT",
    payload: value

});

export const toggleCounter = (value) => ({
    type: "TOGGLE_COUNTER",
    payload : value

});

