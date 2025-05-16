// ./src/store.js
import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./reducers/counterReducer";
import authSlice from "./reducers/authSlice";


const store = configureStore({
    reducer: {
        counter: counterReducer,
        auth: authSlice,
    }
});

export default store;