import React, { useState } from "react";
import Counter from "./components/counter";
function ParentComponent() {
  const [parentState, setParentState] = useState("초기 값");


  return (
    <Counter />
  );
}

export default ParentComponent;