import { useEffect, useState } from "react";

// 마우스 오버/아웃 감지를 위한 커스텀 훅
const useDetectClose = (elem, initialState) => {
  const [isOpen, setIsOpen] = useState(initialState);

  useEffect(() => {
    const node = elem.current;
    if (!node) return;

    const handleMouseEnter = () => setIsOpen(true);
    const handleMouseLeave = () => setIsOpen(false);

    node.addEventListener("mouseenter", handleMouseEnter);
    node.addEventListener("mouseleave", handleMouseLeave);

    return () => {
      node.removeEventListener("mouseenter", handleMouseEnter);
      node.removeEventListener("mouseleave", handleMouseLeave);
    };
  }, [elem]);

  return [isOpen, setIsOpen];
};

export default useDetectClose;