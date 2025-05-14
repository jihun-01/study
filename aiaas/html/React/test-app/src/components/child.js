import React from "react";
// Child.js
function Child() {
    console.log("자식 컴포넌트 렌더링");
  
    return (
      <div style={{ border: "10px solid red", marginTop: "50px" }}>
        <h1>자식 컴포넌트</h1>
      </div>
    );
  }
  
  export default React.memo(Child);