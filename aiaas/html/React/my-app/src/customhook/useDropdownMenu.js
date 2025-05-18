// useDropdownMenu.js
import { useState, useRef, useEffect } from "react";

function useDropdownMenu(closeDelay = 200) {
  const [activeCategory, setActiveCategory] = useState(null);
  const timeoutRef = useRef(null);
  
  const handleMouseEnter = (category) => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    setActiveCategory(category);
  };
  
  const handleMouseLeave = () => {
    timeoutRef.current = setTimeout(() => {
      setActiveCategory(null);
    }, closeDelay);
  };
  
  // 컴포넌트 언마운트 시 타임아웃 정리
  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, []);
  
  return {
    activeCategory,
    handleMouseEnter,
    handleMouseLeave,
    setActiveCategory
  };
}

export default useDropdownMenu;