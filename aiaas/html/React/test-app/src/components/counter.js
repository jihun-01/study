import React from "react";

class Counter extends React.Component {
  constructor(props) {
    super(props);
    // 초기 상태 설정
    this.state = {
      count: 0,
    };

    // 메서드 바인딩
    this.handleIncrement = this.handleIncrement.bind(this);
    this.handleDecrement = this.handleDecrement.bind(this);
  }

  // 메서드 정의
  handleIncrement() {
    this.setState((prevState) => ({
      count: prevState.count + 1,
    }));
  }

  handleDecrement() {
    this.setState((prevState) => ({
      count: prevState.count - 1,
    }));
  }

  render() {
    return (
      <div>
        <h1>Counter: {this.state.count}</h1>
        <button onClick={this.handleIncrement}>Increment</button>
        <button onClick={this.handleDecrement}>Decrement</button>
      </div>
    );
  }
}

export default Counter;