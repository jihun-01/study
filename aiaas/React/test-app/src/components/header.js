// components/header.js

//const Header = () => {
 //   return (
 //     <header className="header">
 //       <p>
 //         <span>홍길동</span>님 환영합니다.{" "}
 //       </p>
 //     </header>
 //   );
 // };
  
 // export default Header;

 // Header.js
import React, { useContext } from "react";
import { UserContext } from "../store/UserContext";

const Header = () => {
  const name = useContext(UserContext);

  return (
        <header className="header">
          <p>
            <span>{name}</span>님 환영합니다.
          </p>
        </header>
  );
};

export default Header;