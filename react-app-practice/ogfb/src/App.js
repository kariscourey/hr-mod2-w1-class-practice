import logo from './old_fb_banner.png';
import './App.css';
import NewsFeed from './containers/NewsFeed';

function App(props) {

  console.log(props);

  const {numbers, colors} = props;
  console.log(numbers);
  console.log(colors);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Hello World!</h1>
        <NewsFeed/>
        <ul>
          {numbers.map(num, index =>
              return (<li key={index}>{num}</li>)
             )}

           {/* map loops through list and applies function to each item */}
        </ul>

        <ol>
          {colors.map(col, index =>
              <li key={index}>{col}</li>
             )}
        </ol>
      </header>
    </div>
  );
}

export default App;
