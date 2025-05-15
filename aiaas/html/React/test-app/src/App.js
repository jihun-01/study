import React, { useState } from "react";
import ChildComponent from "./components/childComponent";

function ParentComponent() {
  const [parentState, setParentState] = useState("초기 값");

  // 자식에서 호출할 수 있는 함수
  const handleChange = (newValue) => {
    setParentState(newValue);
  };

  return (
    <div>
      <h1>부모 상태: {parentState}</h1>
      <ChildComponent onChange={handleChange} />
    </div>
  );
}

export default ParentComponent;