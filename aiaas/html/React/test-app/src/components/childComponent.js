import React from "react";

function ChildComponent({ onChange }) {
  const handleInputChange = (e) => {
    onChange(e.target.value); // 부모 상태를 변경하기 위해 호출
  };

  return (
    <div>
      <input type="text" onChange={handleInputChange} />
    </div>
  );
}

export default ChildComponent;