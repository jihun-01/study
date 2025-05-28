import React, { Component } from "react";

class NameChanger extends Component {
  constructor(props) {
    super(props);
    // 초기 상태 설정
    this.state = {
      name: "나리",
    };
  }

  changeName = () => {
    // 잘못된 방법 (state를 직접 수정)
    this.state = {
      name: "둘리",
    };

    // 올바른 방법
    this.setState({
      name: "둘리",
    });
  };

  render() {
    return (
      <div>
        <p>현재 이름: {this.state.name}</p>
        <button onClick={this.changeName}>이름 변경</button>
      </div>
    );
  }
}

export default NameChanger;