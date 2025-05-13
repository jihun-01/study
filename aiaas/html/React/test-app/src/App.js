import logo from './logo.svg';
import './App.css';
import NameChanger from './components/nameCanger';
import Counter from './components/counter';
import LifeCycleDemo from './components/lifeSycle';
function App() {
  let score = 0;

  const clickHandler = () => {
    score += 1;
    console.log(score);
  };

  return (
    <div className="App">
      <h1>{score}</h1>
      <button onClick={clickHandler}>증가</button>
    </div>
  );
}

export default App;
