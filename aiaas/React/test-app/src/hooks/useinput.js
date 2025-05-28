import { useState } from "react";

// input에 들어갈 초깃값 전달 (initValue)
export function useInput(initValue) {
  // 공통로직으로 빼고싶은 코드를 가져왔음
    const [inputValue, setInputValue] = useState(initValue); // 전달받은 초깃값을 넣음

    const handleChange = (e) => {
        setInputValue(e.target.value);
    };

    const handleSubmit = () => {
        if (inputValue !== "") {
          window.alert("전송 완료");
        }
      };

  return [inputValue, handleChange, handleSubmit]; // return 값으로 input state와 handleChange를 넣어줌
}

export default useInput;